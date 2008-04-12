import cgi

from actors   import Actor, Example, Method, Script, StampedActor, Text, \
                     void_actor
from envs     import Env, global_env
from parser   import Parser
from registry import get_editor, get_uri


number_script = \
    Script([Method('+', ['n'], 'primitive add'),
	    Method('-', ['n'], 'primitive subtract'),
	    Method('*', ['n'], 'primitive multiply'),
	    Method('/', ['n'], 'primitive divide'),
	    Method('**', ['n'], 'primitive power'),
	    Method('<', ['n'], 'primitive lessthan'),
	    Method('=', ['n'], 'primitive equals')])

class Number(Actor):

    def __init__(self, n):
	# XXX global_env is mutable
	Actor.__init__(self, global_env, number_script, n)

    def uneval(self, context, label):
	return context.uncall('builtin.Number', 
			      n=self.primitive_data)
    
    def link_caption(self):
	return str(self.primitive_data)

    def may_edit(self):
	return False

    def __repr__(self):
	return '<<Number %s>>' % self.primitive_data

    def bears_stamp(self, stamp):
	return stamp == type(0)

    def show_data(self):
	return """Value: %s\n<hr>\n""" % self.primitive_data

    def get_n(self, env):
	n = env.must_get('n')
	if not is_number(n):
	    raise 'Not a number', n
	return n.primitive_data

    def prim_add(self, env):
	return Number(self.primitive_data + self.get_n(env))

    def prim_subtract(self, env):
	return Number(self.primitive_data - self.get_n(env))

    def prim_multiply(self, env):
	return Number(self.primitive_data * self.get_n(env))

    def prim_divide(self, env):
	return Number(self.primitive_data / self.get_n(env))

    def prim_power(self, env):
	return Number(self.primitive_data ** self.get_n(env))

    def prim_lessthan(self, env):
	return make_boolean(self.primitive_data < self.get_n(env))

    def prim_equals(self, env):
	return make_boolean(self.primitive_data == self.get_n(env))

def is_number(actor):
    # XXX need to allow an ActorEditor of a Number, too
    # and similarly for other primitive types
    return actor.__class__ == Number

def eqv(actor1, actor2):
    if actor1 == actor2:
	return True
    if is_number(actor1) and is_number(actor2):
	return actor1.primitive_data == actor2.primitive_data
    return False


class Boolean(Actor):

    def __init__(self, script, value):
	# XXX global_env is mutable
	Actor.__init__(self, global_env, script, value)

    def uneval(self, context, label):
	return context.uncall('builtin.Boolean', 
			      script=self.script,
			      value=self.primitive_data)
    
    def link_caption(self):
	return str(self.primitive_data).lower()

    def may_edit(self):
	return False

    def __repr__(self):
	return '<<Boolean %s>>' % self.primitive_data

    def bears_stamp(self, stamp):
	return stamp == type(True)

    def show_data(self):
	return """Value: %s\n<hr>\n""" % self.primitive_data

true_elements = \
    [Method('not', [], 'false'),
     Method('iftrue:iffalse:', ['truevalue', 'falsevalue'], 'truevalue')]
false_elements = \
    [Method('not', [], 'true'),
     Method('iftrue:iffalse:', ['truevalue', 'falsevalue'], 'falsevalue')]

true_actor = Boolean(Script(true_elements), True)
false_actor = Boolean(Script(false_elements), False)
global_env.define('true', true_actor)
global_env.define('false', false_actor)

def is_boolean(actor):
    return actor == true_actor or actor == false_actor

def make_boolean(value):
    if value:
	return true_actor
    else:
	return false_actor


if_script = Script([Method('true:then:else:', ['test', 'yes', 'no'],
			   'booleanguard check: test. (test iftrue: yes iffalse: no) run')])
global_env.define('if', Actor(global_env, if_script))


class Box(Actor):

    def __init__(self, initial_value):
	# XXX global_env is mutable
	Actor.__init__(self, global_env, box_script, initial_value)

    def uneval(self, context, label):
	return context.uncall('builtin.Box', 
			      initial_value=self.primitive_data)
    
    def __repr__(self):
	return '<<Box %s>>' % self.primitive_data

    def may_edit(self):
	return False

    def show_data(self):
	return """Contents: <a href="%s">contents</a>\n<hr>\n""" % \
	    get_uri(self.primitive_data)

    def prim_get(self, env):
	return self.primitive_data

    def prim_set(self, env):
	new_value = env.must_get('newvalue')
	self.primitive_data = new_value
	return void_actor

box_script = Script([Text("""This is a box holding a value.  "box get" returns the value, while "box <- newvalue" replaces it."""),
		     Method('get', [], 'primitive get'),
		     Method('<-', ['newvalue'], 'primitive set')])


class BoxMaker(Actor):
    # XXX the only reason we need this whole class is in order to
    # restrict the prim_makebox... Maybe we should allow 'global'
    # primitives too.

    def __init__(self):
	# XXX global_env is mutable
	Actor.__init__(self, global_env, box_maker_script, True)

    def uneval(self, context, label):
	return context.uncall('builtin.BoxMaker')
    
    def __repr__(self):
	return '<<BoxMaker>>'

    def may_edit(self):
	return False

    def prim_makebox(self, env):
	initial_value = env.must_get('initialvalue')
	return Box(initial_value)

box_maker_script = Script([Text("""Make a new box initially holding initialvalue:"""),
			   Method('holding:', ['initialvalue'],
				  'primitive makebox')])
global_env.define('makebox', BoxMaker())


list_script = \
    Script([Text("""Return the number of elements in this list:"""),
	    Method('length', [], 'primitive length'),
	    Text("""Return my element at the given position:"""),
	    Method('at:', ['position'], 'primitive at'),
	    Text("""Return a sublist of this list. For example, "['a','b','c'] from: 2 to: 3" is ['b','c']."""),
	    Method('from:to:', ['startposition', 'endposition'],
		   'primitive fromto'),
	    Method('from:', ['startposition'], 'primitive from'),
	    Text("""Return the concatenation of two lists. For example, "[1,2] + [3,4]" is [1,2,3,4]."""),
	    Method('+', ['list'], 'primitive catenate'),
	    Text("""Call function left: x right: y for ..."""),
	    Method('foldr:initially:', ['function', 'initialvalue'],
		   'primitive foldr')
	    ])

class List(Actor):

    def __init__(self, elements):
	# XXX global_env is mutable
	Actor.__init__(self, global_env, list_script, tuple(elements))

    def uneval(self, context, label):
	return context.uncall('builtin.List', 
			      elements=self.primitive_data)
    
    def link_caption(self):
	return 'list'

    def __repr__(self):
	return '<<List %s>>' % self.primitive_data

    def bears_stamp(self, stamp):
	return stamp == type(())

    def may_edit(self):
	return False

    def show_data(self):
	# XXX extraneous markup in the elements' show_data()
	elements = [elt.show_data() for elt in self.primitive_data]
	return """Value: [%s]\n<hr>\n""" % ', '.join(elements)

    def prim_length(self, env):
	return Number(len(self.primitive_data))

    def prim_at(self, env):
	pos = env.must_get('position')
	if not is_number(pos):
	    raise 'Not a number', pos
	p = int(pos.primitive_data)
	return self.primitive_data[p-1]

    def prim_fromto(self, env):
	start = env.must_get('startposition')
	if not is_number(start):
	    raise 'Not a number', start
	end = env.must_get('endposition')
	if not is_number(end):
	    raise 'Not a number', end
	s = int(start.primitive_data)
	e = int(end.primitive_data)
	return List(self.primitive_data[(s-1):e])

    def prim_from(self, env):
	start = env.must_get('startposition')
	if not is_number(start):
	    raise 'Not a number', start
	s = int(start.primitive_data)
	return List(self.primitive_data[(s-1):])

    def prim_catenate(self, env):
	x = env.must_get('list')
	if not is_list(x):
	    raise 'Not a list', x
	return List(self.primitive_data + x.primitive_data)

    def prim_foldl(self, env):	# XXX untried
	function = env.must_get('function')
	initialvalue = env.must_get('initialvalue')
	def f(x, y):
	    return function.call('left:right:', [x, y])
	return reduce(f, self.primitive_data, initialvalue)

    def prim_foldr(self, env):
	function = env.must_get('function')
	initialvalue = env.must_get('initialvalue')
	accum = initialvalue
	L = self.primitive_data
	n = len(L)
	for i in range(n):
	    left = L[n-1-i]
	    accum = function.call('left:right:', [left, accum])
	return accum

def is_list(actor):
    return actor.__class__ == List

string_script = \
    Script([Text("""Return the number of characters in this string:"""),
	    Method('length', [], 'primitive length'),
	    Text("""Return a substring of this string. For example, "'hello' from: 1 to: 4" is 'hell'."""),
	    Method('from:to:', ['startposition', 'endposition'],
		   'primitive fromto'),
	    Text("""Return the concatenation of two strings. For example, "'ab' + 'cd'" is 'abcd'."""),
	    Method('+', ['string'], 'primitive catenate'),
	    Text("""HTML escape"""),
	    Method('htmlescaped', [], 'primitive htmlescaped')
	    ])

class String(Actor):

    def __init__(self, str):
	# XXX global_env is mutable
	Actor.__init__(self, global_env, string_script, str)

    def uneval(self, context, label):
	return context.uncall('builtin.String', 
			      str=self.primitive_data)
    
    def link_caption(self):
	s = self.primitive_data
	return cgi.escape(quoted_string(abbreviate_string(s)))

    def __repr__(self):
	return '<<String %s>>' % self.primitive_data

    def bears_stamp(self, stamp):
	return stamp == type('')

    def may_edit(self):
	return False

    def show_data(self):
	return """Value: '%s'\n<hr>\n""" % \
	    cgi.escape(self.primitive_data)  # XXX escape quotes

    def prim_length(self, env):
	return Number(len(self.primitive_data))

    def prim_fromto(self, env):
	start = env.must_get('startposition')
	if not is_number(start):
	    raise 'Not a number', start
	end = env.must_get('endposition')
	if not is_number(end):
	    raise 'Not a number', end
	s = int(start.primitive_data)
	e = int(end.primitive_data)
	return String(self.primitive_data[(s-1):e])

    def prim_catenate(self, env):
	str = env.must_get('string')
	if not is_string(str):
	    raise 'Not a string', str
	return String(self.primitive_data + str.primitive_data)

    def prim_htmlescaped(self, env):
	return String(cgi.escape(self.primitive_data, True))

def is_string(actor):
    return actor.__class__ == String

def eqv(actor1, actor2):
    if actor1 == actor2:
	return True
    if is_number(actor1) and is_number(actor2):
	return actor1.primitive_data == actor2.primitive_data
    if is_string(actor1) and is_string(actor2):
	return actor1.primitive_data == actor2.primitive_data
    return False

def quoted_string(s):
    return "'%s'" % s		# XXX escape quotes, etc.

def abbreviate_string(s):
    if len(s) <= 62: 
	return s
    return '%s...%s' % (s[:30], s[-30:])


class TypeGuard(Actor):

    def __init__(self, sample_instance):
	# XXX global_env is mutable
	Actor.__init__(self, global_env, type_guard_script, sample_instance)

    def uneval(self, context, label):
	return context.uncall('builtin.TypeGuard',
			      sample_instance=self.primitive_data)
    
    def __repr__(self):
	return '<<TypeGuard>>'

    def may_edit(self):
	return False

    def prim_check(self, env):
	object = env.must_get('object')
	if object.bears_stamp(type(self.primitive_data)):
	    return void_actor
	# XXX we should tell the user what type we're looking for
	raise 'Bad type', object

    def prim_passes(self, env):
	object = env.must_get('object')
	return make_boolean(object.bears_stamp(type(self.primitive_data)))

# XXX script should tell the user what type we're looking for
type_guard_script = Script([Text("""Raise an error if object the wrong type:"""),
			    Method('check:', ['object'], 'primitive check'),
			    Method('passes:', ['object'], 'primitive passes')
			    ])
global_env.define('numberguard', TypeGuard(0))
global_env.define('stringguard', TypeGuard(''))
global_env.define('listguard', TypeGuard(()))
global_env.define('booleanguard', TypeGuard(True))


class Stamp(Actor):
    """A unique tag checked by a corresponding stampguard."""

    def __init__(self):
	# XXX global_env is mutable
	Actor.__init__(self, global_env, stamp_script, False)

    def uneval(self, context, label):
	return context.uncall('builtin.Stamp')

    def __repr__(self):
	return '<<Stamp>>'

    def may_edit(self):
	return False

    def link_caption(self):
	return 'stamp'

    def prim_stamp(self, env):
	object = env.must_get('object')
	return StampedActor(object, self)

stamp_script = Script([Text("""A stamp marks object types to be passed by a corresponding stampguard."""),
		       Method('stamp:', ['object'], 'primitive stamp')])


class StampGuard(Actor):

    def __init__(self, stamp):
	# XXX global_env is mutable
	Actor.__init__(self, global_env, stampguard_script, stamp)

    def uneval(self, context, label):
	return context.uncall('builtin.StampGuard', stamp=self.primitive_data)

    def __repr__(self):
	return '<<StampGuard>>'

    def may_edit(self):
	return False

    def link_caption(self):
	return 'stampguard'

    def prim_check(self, env):
	object = env.must_get('object')
	if object.bears_stamp(self.primitive_data):
	    return void_actor
	raise 'Not properly stamped', object

stampguard_script = \
    Script([Text("""A stampguard checks whether objects are of a type bearing a particular stamp."""),
	    Method('check:', ['object'], 'primitive check')])

class StampMaker(Actor):
    # XXX the only reason we need this whole class is in order to
    # restrict the prim_makestamp... Maybe we should allow 'global'
    # primitives too.

    def __init__(self):
	# XXX global_env is mutable
	Actor.__init__(self, global_env, stamp_maker_script, True)

    def uneval(self, context, label):
	return context.uncall('builtin.StampMaker')
    
    def __repr__(self):
	return '<<StampMaker>>'

    def may_edit(self):
	return False

    def prim_makestamp(self, env):
	stamp = Stamp()
	return List((stamp, StampGuard(stamp),))

stamp_maker_script = Script([Text("""Make a new [stamp, stampguard] pair:"""),
			     Method('run', [], 'primitive makestamp')])
global_env.define('makestamp', StampMaker())


maildir_script = \
    Script([Method('at:put:', ['name', 'sender'], 'primitive atput'),
	    Method('at:', ['name'], 'primitive at')])

class MailDirectory(Actor):

    def __init__(self, env=None):
	if env is None:
	    env = global_env.sprout()
	Actor.__init__(self, env, maildir_script, True)
	# XXX the following might run before env is initialized, when
	# restoring from a snapshot.  We should just throw out this
	# env hack and make something better.
	for key in env.locals:
	    self.script.add_element(Example(key))

    def uneval(self, context, label):
	return context.uncall('builtin.MailDirectory', 
			      env=self.env)
    
    def __repr__(self):
	return '<<MailDirectory>>'

    def may_edit(self):
	return False

    def prim_atput(self, env):
	name = env.must_get('name')
	if not is_string(name):
	    raise 'Not a string', name
	key = name.primitive_data.strip()
	p = Parser(key, {})
	is_identifier = p.token(p.identifier, True)
	if not is_identifier:
	    raise 'Not a valid mailbox name', name
	p.token(p.identifier)
	p.done()
	sender = env.must_get('sender')
	already = self.env.get(key)
	if already is not None:
	    return false_actor
	self.env.define(key, sender)
	self.script.add_element(Example(key))
	return true_actor

    def prim_at(self, env):
	name = env.must_get('name')
	if not is_string(name):
	    raise 'Not a string', name
	key = name.primitive_data.strip()
	already = self.env.get(key)
	if already is None:
	    return false_actor
	return already

maildir_actor = MailDirectory()


def make_account():
    from actors import Expression # XXX circular module dependency
    root_env = global_env.sprout()

    sender_script = \
	Script([Method('send:', ['message'], 
		       'inbox <- ([message] + inbox get)')])
    mailbox_script = \
	Script([Method('first', [], 'inbox get at: 1'),
		Method('removefirst', [], 'inbox <- (inbox get from: 2)'),
		Method('sender', [], 'sender')])
    makemailbox_run = \
	Method('run', [], 
	       Expression('let inbox = makebox holding: []. make sender. make mailbox',
			  {'sender': sender_script,
			   'mailbox': mailbox_script}))
    root_env.define('makemailbox', Actor(root_env, Script([makemailbox_run])))

    root_env.define('maildirectory', maildir_actor)

    root_actor = \
	Actor(root_env,
	      Script([Text('Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:'),
		      Example('2 + 3'), 
		      Example('(3*3) + (4*4)'), 
		      Text('The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":'),
		      Example('make Foo'),
		      Text('You can also give a local name to any other object using "let name = expression". For example:'),
		      Example('let box = makebox holding: true'),
		      Example('box get'),
		      Example('box <- false. box get'),
		      Example("['hello']"),
 		      Text("""There's a public directory of message boxes for other users, in maildirectory:"""),
 		      Example('maildirectory'),
		      Text('You can create your own mailbox:'),
		      Example('let mailbox = makemailbox run'),
 		      Text("""To add it to the directory, enter "maildirectory at: 'alice' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text."""),
		      Text("""Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!""")
		      ]))
    return get_editor(root_actor)
