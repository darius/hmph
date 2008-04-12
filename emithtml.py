import cgi

def emit(obj, attribute=False):
    if type(obj) == list:
	return ''.join([emit(element) for element in obj])
    if type(obj) == str:
	return cgi.escape(obj, attribute)
    if type(obj) == type(emit):
	return obj()		# XXX what if attribute=True?
    raise 'Bad type', obj

def emit_attributes(dict):
    attrs = []
    for key in dict:
	attrs.append(' %s="%s"' % (cgi.escape(key), 
				   emit(dict[key], attribute=True)))
    return ''.join(attrs)

def make_tag_emitter(tag):
    def make(_='', **kwargs):
	def emitter():
	    return '<%s%s>%s</%s>' % (tag,
				      emit_attributes(kwargs), emit(_),
				      tag)
	return emitter
    return make

def make_lonetag_emitter(tag):
    def make(**kwargs):
	def emitter():
	    return '<%s%s>' % (tag, emit_attributes(kwargs))
	return emitter
    return make

Form = make_tag_emitter('form')
TextArea = make_tag_emitter('textarea')
Input = make_lonetag_emitter('input')


def method_call_form(target, selector, argument_html):
    return Form(method='POST', 
		action=get_uri(target) + '/call',
		_=[Input(type='hidden', name='selector', value=selector)] + \
		  argument_html)()

def element_delete_form(target, serial_id):
    return Form(method='POST', 
		action=get_uri(target) + '/delete',
		_=[Input(type='hidden', name='serial_id', value=serial_id),
		   Input(type='submit', value='Delete')])()

def element_edit_form(target, serial_id):
    return Form(method='GET', 
		action=get_uri(target) + '/edit#' + serial_id,
		_=[Input(type='hidden', name='serial_id', value=serial_id),
		   Input(type='submit', value='Edit')])()

def element_editor_form(target, serial_id, body):
    return Form(method='POST', 
		action=get_uri(target) + '/update',
		_=[Input(type='hidden', name='serial_id', value=serial_id),
		   Input(type='submit', value='Save'),
		   TextArea(style='width:100%', rows='10', _=body)])()

def adder_form(target):		# XXX rename
    uri = get_uri(target)
    form1 = Form(method='POST', action=uri + '/addmethod', 
		 _=[Input(type='textarea', name='content'),
		    Input(type='submit', value='Add method')])
    form2 = Form(method='POST', action=uri + '/addexample', 
		 _=[Input(type='textarea', name='content'),
		    Input(type='submit', value='Add example')])
    form3 = Form(method='POST', action=uri + '/addtext', 
		 _=[TextArea(name='content', width='90%', rows='10'), 
		    Input(type='submit', value='Add text')])
    return '<hr>' + form1() + form2() + form3()

def get_uri(x): 
    return x
