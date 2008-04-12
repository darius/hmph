import cgi

from envs import Env, global_env
from parser import parse
from registry import get_editor, get_uri
import rest


class Expression:

    def __init__(self, text, inner_map=None):
        if inner_map is None:
            inner_map = {}
        self.text = text
        self.inner_map = inner_map

    def uneval(self, context, label):
        return context.uncall('actors.Expression', 
                              text=self.text, 
                              inner_map=self.inner_map)

    def __repr__(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def set_inner(self, name, script):
        self.inner_map[name] = script

    def ensure_inner(self, name):
        if name not in self.inner_map:
            self.inner_map[name] = Script([])

    def eval(self, env, actor):
        return evaluate(self.text, self.inner_map, env, actor)

    def mark_up(self, env):
        return mark_up_expression(self.text, self.inner_map, env)


def evaluate(e, inner_map, env, actor):
    code, decorators = parse(e, inner_map)
    return code.run(actor, env)

def mark_up_expression(text, inner_map, env):
    try:
        code, decorators = parse(text, inner_map)
    except:
        return escape_with_lines(text)  # XXX indicate syntax error somehow
    result = ''
    i = 0
    for ((lo, hi), formatter) in decorators:
        result += escape_with_lines(text[i:lo])
        result += formatter(text[lo:hi], env, inner_map)
        i = hi
    result += escape_with_lines(text[i:])
    return result

def escape_with_lines(text):
    text = cgi.escape(text)
    return '<br>\n'.join(text.split('\n'))


# Now for the actual actor stuff.

class Element:

    def __init__(self, serial_id=None):
        if serial_id is not None:
            self.serial_id = serial_id

    def show(self, script, actor, editable):
        if editable:
            maybe_edit = \
                rest.element_edit_form(actor or script, self.serial_id)
            maybe_delete = \
                rest.element_delete_form(actor or script, self.serial_id)
        else:
            maybe_edit = ''
            maybe_delete = ''
        return '''
<table>
 <tr><td>%(maybe_edit)s
     <td>%(maybe_delete)s
 <tr><td colspan="2">%(body)s
</table>''' % { 'maybe_edit': maybe_edit,
                'maybe_delete': maybe_delete,
                'body': self.show_body(actor) }


class Text(Element):

    def __init__(self, body, serial_id=None):
        Element.__init__(self, serial_id)
        self.selector = None
        self.body = body

    def uneval(self, context, label):
        return context.uncall('actors.Text', 
                              body=self.body,
                              serial_id=self.serial_id)

    def get_body(self):
        return self.body
    
    def set_body(self, body):
        self.body = body
    
    def get_heading(self):
        return ''

    def show_bare(self, script, actor):
        return self.show(script, actor, False)

    def show_body(self, actor):
        return escape_with_lines(self.body)


class Example(Element):

    def __init__(self, expression, serial_id=None):
        Element.__init__(self, serial_id)
        if type(expression) == type(''):
            self.expression = Expression(expression)
        else:
            self.expression = expression
        self.results = {}
        self.selector = None

    def uneval(self, context, label):
        buildme = context.uncall('actors.Example', 
                                 expression=self.expression,
                                 serial_id=self.serial_id)
        additions = [context.uncall('_add_result', 
                                    actor=actor, 
                                    result=self.results[actor])
                     for actor in self.results]
        return context.unsequence(buildme, label, additions)
    
    def _add_result(self, actor, result):
        self.results[actor] = result

    def get_body(self):
        return self.expression.text
    
    def set_body(self, body):
        self.expression.set_text(body)
        self.results = {}
    
    def get_heading(self):
        return ''

    def show_bare(self, script, actor):
        # XXX OK to show more, just minus the markup?
        return ''

    def show_body(self, actor):
        # XXX the env should be a sprout of the actor's env
        #     shared by its other examples
        # XXX skip result if actor is None
        if actor not in self.results:
            self._add_result(actor, self._run(actor))
        result = self.results[actor]
        if type(result) == type(''):
            result_html = cgi.escape(result)
        else:
            # XXX we don't necessarily have editor privileges on the result
            result_html = '<a href="%s">%s</a>' % (get_uri(get_editor(result)),
                                                   result.link_caption())
        return '? %s<br>%s' % (self.expression.mark_up(actor.get_env()), 
                               result_html)

    def _run(self, actor):
        try:
            return self.expression.eval(actor.get_env(), actor)
        except:
            import sys
            exception_type, exception_value = sys.exc_info()[:2]
            complaint = 'Error: %s: %s' % (exception_type, exception_value)
            return complaint


class Method(Element):

    # XXX callers should supply a tuple of parameters, not a list
    def __init__(self, selector, parameters, body, serial_id=None):
        Element.__init__(self, serial_id)
        self.selector = selector
        self.parameters = parameters
        if type(body) == type(''):
            self.body = Expression(body)
        else:
            self.body = body

    def uneval(self, context, label):
        return context.uncall('actors.Method', 
                              selector=self.selector, 
                              parameters=self.parameters, 
                              body=self.body,
                              serial_id=self.serial_id)
    
    def get_body(self):
        return self.body.text
    
    def set_body(self, body):
        self.body.set_text(body)

    def get_heading(self):
        return '<h3>%s</h3>' % cgi.escape(self.get_signature())

    def set_inner(self, name, script):
        self.body.set_inner(name, script)

    def ensure_inner(self, name):
        self.body.ensure_inner(name)

    def mark_up_body(self, env):
        return self.body.mark_up(env)

    def get_signature(self):
        parts = self.selector.split(':')
        if 1 < len(parts):
            colon = ':'
        else:
            colon = ''
        if parts[-1] == '':
            del parts[-1]
        i = 0
        result = ''
        while i < max(len(parts), len(self.parameters)):
            if i < len(parts):
                result += ' ' + parts[i] + colon
            if i < len(self.parameters):
                result += ' ' + self.parameters[i]
            i += 1
        return result.lstrip()

    def _argument_field(self):
        if len(self.parameters) == 0:
            return ''
        result = 'with'
        for p in self.parameters:
            result += ' %s=<input name="%s">' % (p, p)
        return result

    def show_bare(self, script, actor):
        heading = self.get_heading()
        if actor is None:
            return heading
        else:
            call = rest.method_call_form(actor or script,
                                         self.selector, 
                                         self._argument_field())
            return '''
<table>
 <tr>
  <td>%(call)s
 <tr>
  <td>
   %(signature)s
</table>''' % { 'call': call,
                'signature': heading }

    def show(self, script, actor, editable):
        # XXX some code duplication wrt Element.show()
        if actor is None:
            maybe_call = ''
            env = global_env
        else:
            maybe_call = \
                rest.method_call_form(actor or script,
                                      self.selector, 
                                      self._argument_field())
            env = actor.get_env()
        if editable:
            maybe_edit = \
                rest.element_edit_form(actor or script, self.serial_id)
            maybe_delete = \
                rest.element_delete_form(actor or script, self.serial_id)
        else:
            maybe_edit = ''
            maybe_delete = ''
        return '''
<table>
 <tr>
  <td>%(maybe_edit)s
  <td>%(maybe_delete)s
  <td>%(maybe_call)s
 <tr>
  <td colspan="3">
   %(signature)s
   <blockquote>%(body)s</blockquote>
</table>''' % { 'maybe_edit': maybe_edit,
                'maybe_delete': maybe_delete,
                'maybe_call': maybe_call,
                'signature': self.get_heading(),
                'body': self.mark_up_body(env) }

    def call(self, actor, selector, arguments):
        return self.body.eval(Env(actor.get_env(), 
                                  bind(self.parameters, arguments)),
                              actor)

class OtherwiseMethod:

    def __init__(self, method):
        self.method = method
        
    def call(self, actor, selector, arguments):
        new_arguments = list_to_actor([string_to_actor(selector)] + arguments)
        return self.method.call(self, selector, new_arguments)


def bind(vars, vals):
    if len(vars) != len(vals):
        raise 'Argument count mismatch', (vars, vals)
    result = {}
    for var, val in zip(vars, vals):
        result[var] = val
    return result


class ActorEditor:

    def __init__(self, actor, editable):
        assert actor.__class__ != ActorEditor
        self.actor = actor
        self.editable = editable
        self.primitive_data = None

    def uneval(self, context, label):
        return context.uncall('actors.ActorEditor', 
                              actor=self.actor,
                              editable=self.editable)

    def get_env(self):
        return self.actor.get_env()

    def get_script(self):
        return self.actor.get_script()

    def get_element(self, serial_id):
        return self.actor.get_element(serial_id)

    def get_method(self, selector):
        return self.actor.get_method(selector)

    def delete_element(self, serial_id):
        if not self.editable:
            raise 'Not editable'
        return self.actor.get_script().delete_element(serial_id)

    def set_method_body(self, selector, body):
        if not self.editable:
            raise 'Not editable'
        return self.actor.get_script().set_method_body(selector, body)

    def add_element(self, element):
        if not self.editable:
            raise 'Not editable'
        return self.actor.get_script().add_element(element)

    def add_example(self, expression):
        if not self.editable:
            raise 'Not editable'
        example = Example(expression)
        self.add_element(example)
        return example

    def add_method(self, selector, parameters):
        if not self.editable:
            raise 'Not editable'
        return self.actor.get_script().add_method(selector, parameters)

    def add_text(self, body):
        if not self.editable:
            raise 'Not editable'
        return self.actor.get_script().add_text(body)

    def show(self):
        to_bare = '<a href="%s">[Seal]</a><hr>' % get_uri(self.actor)
        return to_bare + self.actor.show_data() + \
            self.actor.get_script().show(self, self.editable)

    def show_editable(self, serial_id):
        if not self.editable:
            raise 'Not editable'
        return self.actor.get_script().show_editable(serial_id, self)

    def call(self, selector, arguments):
        # XXX This should only *try* to get an editor view on the 
        # result, using a can-opener capability.  Might not succeed.
        return get_editor(self.actor.call(selector, arguments))


def _unused_element_id(elements):
    result = 0
    for elt in elements:
        if hasattr(elt, 'serial_id'):
            result = max(result, elt.serial_id + 1)
    return result

class Script:

    # Pre: elements aren't in any other script
    def __init__(self, elements, stamps=(), next_serial_id=None):
        self.stamps = stamps
        if next_serial_id is None:
            self.next_serial_id = _unused_element_id(elements)
        else:
            self.next_serial_id = next_serial_id
        self.elements = []
        for element in elements:
            self.add_element(element)

    def uneval(self, context, label):
        return context.uncall('actors.Script', 
                              next_serial_id=self.next_serial_id,
                              elements=self.elements)
    
    def may_edit(self):
        # XXX I'm assuming a predefined immutable script like for
        # the Number type never gets in a position where it's asked
        # this question -- you're always looking at a specific number
        # whose actor class handles this.  Scripts only get linked to
        # directly from expressions like "make Foo".
        # (This raises the question whether there's a *need* for an
        # ActorEditor wrapper around a script -- perhaps the script
        # object should handle that responsibility directly?)
        return True

    def get_element(self, serial_id):
        for elt in self.elements:
            if elt.serial_id == serial_id:
                return elt
        raise 'Element not found', serial_id

    def delete_element(self, serial_id):
        previous_element = None
        for i in range(len(self.elements)):
            if self.elements[i].serial_id == serial_id:
                del self.elements[i]
                return previous_element
            previous_element = self.elements[i]
        raise 'Element not found', serial_id

    def get_method(self, selector):
        for elt in self.elements:
            if elt.selector == selector:
                return elt
        return None

    def set_method_body(self, selector, body):
        self.get_method(selector).set_body(body)

    def add_element(self, element):
        if not hasattr(element, 'serial_id'):
            element.serial_id = self.next_serial_id
            self.next_serial_id += 1
        self.elements.append(element)

    def add_example(self, expression):
        example = Example(expression)
        self.add_element(example)
        return example

    def add_method(self, selector, parameters):
        if not self.get_method(selector):
            self.add_element(Method(selector, parameters, ''))

    def add_text(self, body):
        text = Text(body)
        self.add_element(text)
        return text

    def _adder_form(self, actor):
        return rest.adder_form(actor or self)

    def show_bare(self, actor=None):
        parts = ['<a name="%s">%s</a>' % (elt.serial_id, 
                                          elt.show_bare(self, actor)) \
                 for elt in self.elements]
        # XXX leave out <hr>'s for empty elements 
        return '<hr>\n'.join(parts)

    # N.B. editable=True for the same reason self.may_edit() = True
    def show(self, actor=None, editable=True):
        parts = ['<a name="%s">%s</a>' % (elt.serial_id, 
                                          elt.show(self, actor, editable)) \
                 for elt in self.elements]
        html = '<hr>\n'.join(parts)
        if editable: 
            html += self._adder_form(actor)
        return html

    def show_editable(self, serial_id, actor=None):
        parts = []
        for element in self.elements:
            if element.serial_id == serial_id:
                part = self._element_editor_form(serial_id, actor)
            else:
                part = element.show(self, actor, True)
            parts.append('<a name="%s">%s</a>' % (element.serial_id, part))
        return '<hr>\n'.join(parts)   # + self._adder_form(actor)
        
    def _element_editor_form(self, serial_id, actor):
        element = self.get_element(serial_id)
        heading = element.get_heading()
        form = rest.element_editor_form(actor or self, 
                                        serial_id, 
                                        element.get_body())
        if heading != '':
            return '<h3>%s</h3>%s' % (heading, form)
        return form

    def dispatch(self, selector):
        for elt in self.elements:
            if elt.selector == selector:
                return elt
        for elt in self.elements:
            if elt.selector == 'otherwise':
                return OtherwiseMethod(elt)
        raise 'No matching method', selector

    def call(self, selector, arguments):
        raise 'This is a script, not an actor'


class Actor:

    def __init__(self, env, script, primitive_data=None):
        self.env = env
        self.script = script
        self.primitive_data = primitive_data

    def uneval(self, context, label):
        if self.primitive_data is None:
            return context.uncall('actors.Actor', 
                                  env=self.env,
                                  script=self.script)
        else:
            return context.uncall('actors.Actor', 
                                  env=self.env,
                                  script=self.script,
                                  primitive_data=self.primitive_data)

    def bears_stamp(self, stamp):
        return False

    def link_caption(self):
        return 'result'

    def may_edit(self):
        return True

    def get_env(self):
        return self.env

    def get_script(self):
        return self.script

    def get_element(self, serial_id):
        return self.get_script().get_element(serial_id)

    def get_method(self, selector):
        return self.get_script().get_method(selector)

    def show_data(self):
        return ''

    def show(self):
        to_editor = '<a href="%s">[Unseal]</a><hr>' % get_uri(get_editor(self))
        return to_editor + self.show_data() + self.get_script().show_bare(self)

    def call(self, selector, arguments):
        return self.get_script().dispatch(selector).call(self, selector, arguments)


class StampedActor:             # XXX inherit from an abstract Actor class

    # XXX maybe we should take a tuple of stamps instead
    def __init__(self, actor, stamp):
        self.actor = actor
        self.stamp = stamp

    def uneval(self, context, label):
        return context.uncall('actors.StampedActor', 
                              actor=self.actor,
                              stamp=self.stamp)

    def bears_stamp(self, stamp):
        return self.stamp == stamp

    # Everything below here just forwards to self.actor

    def link_caption(self):
        return self.actor.link_caption()

    def may_edit(self):
        return self.actor.may_edit()

    def get_env(self):
        return self.actor.get_env()

    def get_script(self):
        return self.actor.get_script()

    def get_element(self, serial_id):
        return self.actor.get_element(serial_id)

    def get_method(self, selector):
        return self.actor.get_method(selector)

    def show_data(self):
        return self.actor.show_data()

    def show(self):
        return self.actor.show()

    def call(self, selector, arguments):
        return self.actor.call(selector, arguments)


# XXX mutable global env
void_actor = Actor(global_env, Script([]))
