class ElementInterface:
    """
    An element belongs to a Script.
    """

    public_fields = ('serial_id', 'selector',)

    def uneval(self, context, label):
	"""An element is persistent."""

    def get_body(self):
	"""Return a string with my body for editing."""

    def set_body(self, body):
	"""Set my body text."""

    def get_heading(self):
	"""Return HTML to appear before my body."""

    def show_bare(self, script, opt_actor):
	"""
	Return HTML for this element when shown as part of an encapsulated
	object (as opposed to a view of the object's guts).  
	script: the script self belongs to.
	opt_actor: either None or an actor whose script is 'script'.
	The point of passing this in is to be able to form URIs.
	XXX could be an ActorEditor too, right?  I don't think so, 
	because ActorEditors don't show self as bare, I think.
	"""
    
    def show(self, script, opt_actor, editable):
	"""
	Return HTML for this element in a view of an object's guts.
	script: the script self belongs to.
	opt_actor: either None or an actor whose script is 'script'.
	editable: true iff we are to supply an Edit button
	"""

class ExpressionInterface:

    def uneval(self, context, label):
	"""Must be persistent."""

    def set_text(self, text):
	"""Set my text."""

    def set_inner(self, name, script):
	"""Make my inner_map map 'name' to 'script'."""

    def ensure_inner(self, name):
	"""Ensure that my inner_map maps 'name' to a script -- an empty one if
	not yet mapped."""

    def mark_up(self, env):
	"""Return HTML for myself with variables linked according to env.
	XXX It would be less 'global' to pass in the registry, here and
	elsewhere..."""

    def eval(self, env, actor):
	"""Return my value in env.  
	actor is needed because primitives access it.
	XXX reorg so it isn't needed anymore?"""

class TextInterface(ElementInterface): 
    pass

class ExampleInterface(ElementInterface):
    pass

class MethodInterface(ElementInterface):

    def set_body(self, body):
	"""Set my body's text."""

    def set_inner(self, name, script):
	"""Set my body's inner_map association for 'name' to 'script'."""

    def ensure_inner(self, name):
	"""Ensure that my body's inner_map maps 'name' to a script --
	an empty one if not yet mapped."""

    def mark_up_body(self, env):
	"""Return HTML for myself with variables linked according to env."""

    def get_signature(self):
	"""
	Return my signature line as a string (e.g. "foo: param1 bar: param2")
	"""

    def call(self, actor, selector, arguments):
	"""
	Run self with the given arguments.
	Pre: selector is my selector, and len(arguments) is correct.
	actor: included for two reasons: 
               1. so we can extend its current mutable env
               2. because Expression.eval needs it
	selector: included for the sake of OtherwiseMethod
	"""

class OtherwiseMethodInterface:

    def call(self, actor, selector, arguments):
	"""
	Same as from MethodInterface.
	XXX Note that this class defines none of the rest of MethodInterface.
	"""

class ActorInterface:

    def uneval(self, context, label):
	"""Persistent."""

    def bears_stamp(self, stamp):
	"""Return true iff self bears stamp.
	stamp may be a Stamp or a primitive type object."""

    def link_caption(self):
	"""Return a short string to be used in HREF anchors linking to me."""

    def may_edit(self):
	"""Return true iff my elements may be edited.
	XXX We're supposed to use capabilities to manage that stuff."""

    def get_env(self):
	"""Return my environment."""

    def get_script(self):
	"""Return my script."""

    def get_element(self, serial_id):
	"""Return my script's element with the given serial_id."""

    def get_method(self, selector):
	"""Return my script's method with the given selector, or None
	if there is no such method.
	XXX rename to opt_get_method?  raise an error?"""

    def show_data(self):
	"""Return HTML displaying any primitive_data I have."""

    def show(self):
	"""Return HTML displaying myself (encapsulated by default)."""

    def call(self, selector, arguments):
	"""Invoke myself with the given message and return the result.
	XXX control flow should be explicit, for debugging."""

class ScriptInterface:
    """
    XXX work out just what's in common between this interface and
    those of actors and actoreditors.  Not to mention elements.
    """

    public_fields = ('stamps',)

    def uneval(self, context, label):
	"""Persistent."""
    
    def may_edit(self):
	"""Return true iff my elements may be edited.
	XXX We're supposed to use capabilities to manage that stuff."""

    def get_element(self, serial_id):
	"""Return my element with the given serial_id."""

    def delete_element(self, serial_id):
	"""Remove the element with the given serial_id."""

    def get_method(self, selector):
	"""Return my method with the given selector, or None if there is no
	such method.
	XXX rename to opt_get_method?  raise an error?"""

    def set_method_body(self, selector, body):
	"""Set the text of my method for 'selector' to 'body'.
	XXX raise an error if no method?  or just add it?"""

    def add_element(self, element):
	"""Append a new element to my elements.  element must be newly
	consed, not belonging to another script.
	XXX change interface so element is given its serial_id on
	creation?"""

    def add_example(self, expression):
	"""Append a new example to my elements, and return it."""

    def add_method(self, selector, parameters):
	"""If I don't have a method with the given selector, add a new one
	(with an empty body.
	XXX should warn if already exists"""

    def add_text(self, body):
	"""Append a new text element to my elements, and return it."""

    def show_bare(self, actor=None):
	"""
	Return HTML displaying a view of me (or of actor) encapsulated.
	Pre: If actor isn't None then I must be its script.
	XXX Maybe we should have different methods for showing me as a
	script vs. showing an actor whose script is me.
	"""

    def show(self, actor=None, editable=True):
	"""
	Return HTML displaying a view of my guts (or of actor's).
	Supply Edit buttons and so on iff editable is true.
	Pre: If actor isn't None then I must be its script.
	"""

    def show_editable(self, serial_id, actor=None):
	"""
	Return HTML displaying a view of my guts (or of actor's),
	with edit buttons, and a text-editing area for the given element.
	Pre: If actor isn't None then I must be its script.
	XXX use a scheme that works for other element types too
	"""
	
    def dispatch(self, selector):
	"""
	Return a method handling messages with the given selector sent
	to actors whose script is me.
	Don't use get_method() for this because the selector might not
	be defined -- we return an OtherwiseMethod then.
	XXX yuck
	"""

    def call(self, selector, arguments):
	"""
	XXX only included because we're sort of polymorphic with actors
	"""

class ActorEditorInterface:

    def uneval(self, context, label):
	"""Persistent."""
    
    def get_env(self): """like ActorInterface"""

    def get_script(self): """like ActorInterface"""

    def get_element(self, serial_id): """like ActorInterface"""

    def delete_element(self, serial_id): """like ActorInterface"""

    def get_method(self, selector): """like ScriptInterface"""

    def set_method_body(self, selector, body): """like ScriptInterface"""

    def add_element(self, element): """like ScriptInterface"""

    def add_example(self, expression): """like ScriptInterface"""

    def add_method(self, selector, parameters): """like ScriptInterface"""

    def add_text(self, body): """like ScriptInterface"""

    def show(self):
	"""
	Return HTML displaying a view of my guts, 
	Supply Edit buttons and so on iff my wrapped actor is editable.
	"""

    def show_editable(self, serial_id):
	"""
	Return HTML displaying a view of my guts with edit buttons,
	and a text-editing area for the given element.
	(Unless my wrapped actor is not editable -- then raise an error.)
	"""

    def call(self, selector, arguments):
	"""like ActorInterface"""
