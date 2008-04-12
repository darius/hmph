class Hidden:
    def __init__(self, value):
	pass			# XXX

def form(method, action, body_html='', **params):
    return """
<form method="%(method)s" action="%(action)s">
%(inputs)s%(body)s
</form>
""" % { 'method': method,
	'action': action,
	'inputs': ... }


def method_call_form(target, selector, argument_field):
    return form('POST', get_uri(target) + '/call',
		selector=Hidden(selector),
		body_html=argument_field)

def element_delete_form(target, serial_id):
    return form('POST', get_uri(target) + '/delete',
		serial_id=Hidden(serial_id),
		_='Delete') # XXX

def element_edit_form(target, serial_id):
    return form('GET', "%s/edit#%s" % (get_uri(target), serial_id),
		serial_id=Hidden(serial_id),
		_='Edit') # XXX

def element_editor_form(target, serial_id, body):
    return form('POST', get_uri(target) + '/update',
		serial_id=Hidden(serial_id),
		_='Save',
		body=Textarea(body, style='width:100%', rows='10'))

def adder_form(target):
    uri = get_uri(target)
    # XXX the first 2 textareas should be <input type="textarea">
    return '<hr>' +\
	form('POST',uri + '/addmethod', content=Textarea(), _='Add method') +\
	form('POST',uri + '/addexample', content=Textarea(), _='Add example') +\
	form('POST',uri + '/addtext', 
	     content=Textarea(width='90%', rows='10'), 
	     _='Add text')

