"""
Information about our URI tree structure takes three forms:
1. URI strings like /id/123 associated with GET or POST and with parameters
2. Form elements like 
  <form method="POST" action="%(uri)s/addelement">
    <input type="textarea" name="content">
  ...</form>
3. The dispatching and parameter parsing in the HTTP handler.

We want to define these things in one place.
Unfortunately, #2 mixes in user-interface aspects.

It might also make sense to keep the ID registry here.
"""

import cgi
import urllib

from parser   import parse_literal, parse_signature
from registry import get_actor, get_editor, get_id, get_uri, id_is_defined, \
                     access_id, add_account
import webserver


welcome = '''
<h1>Hmph! User-hackable websites</h1>

<b>Hmph</b> encourages <b>public, on-the-fly programming of a website
by its users</b>, a bit like how <a
href="http://en.wikipedia.org/wiki/Wiki">wikis</a> get created by
their visitors.  Hmph's pages are active objects that people view,
control, or edit 'live', as in <a
href="http://www.squeak.org">Squeak</a>; people and objects can
collaborate securely because all actions follow capability discipline,
as in <a href="http://erights.org">E</a>.

<p>Read the <a href="/about">hype-filled sales pitch for suits</a>.
Or just try it out: <form method="POST" action="/makeaccount">
 <input type="submit" value="Go!">
</form>
'''

about = '''
<h1>About Hmph</h1>

Hmph is a web-based programming system for open, collaborative
development of collaborative applications.  The most successful web
businesses, like Amazon, eBay, and Google, embody Tim O'Reilly's
<b>architecture of participation</b>: the value of these sites gets
created largely by ordinary people as they use the web.  Hmph tries to
open up a new way they can participate, perhaps ultimately creating
new business opportunities that couldn't be envisioned before.

<p>Hmph <b>differs from most content management systems</b> by
focusing on programming more than publishing, and by blurring the line
between site developers and users.  (This line becomes more of a
dynamic distribution of roles and authority.)  Traditional systems
can't trust users with programming because of its arcanity and the
difficulty of separating and delegating authorities.  People need a
smooth slope between clicking links, editing text, tweaking behavior,
and building new apps, like the smooth slope from simple to fancy
spreadsheets.

<p>Hmph <b>differs from most programming languages</b> by working from
structured, hyperlinked documents instead of plain text; the structure
and links are integral to the language, not just sugar.  Like
spreadsheets, Hmph is designed for motivated but ordinary people, by
working with concrete, live examples, minimizing syntax, and enacting
a high-level metaphor of active documents.  It supports a literate
style mingling text and examples with code.

<p>Hmph's objects conform to <b>capability security</b>.  Traditional
security systems like those of Unix and Windows grew out of basic
designs for small local groups or individuals off the net; those
architectures don't scale to open systems with mutually-untrusting
agents.  Capabilities are a simple but surprising alternative, better
suited to modern problems and opportunities.

<p>[Maybe add a bit about the power of end-user programming in real
life with systems like spreadsheets -- how it matters even though most
people don't do any programming, because of local power users making
local adaptations, etc.]

<p>(This is a super-pre-alpha version that doesn't deliver on the
above claims yet; I hope it does begin to show the shape of the thing.
Most importantly, I don't know how well in practice capability
concepts map onto familiar operations in a web browser -- we need to
try it and see.  Web features like the 'referer' field might end up
making it too hard to get real security in popular web browsers.)

<p>(Also, the name is totally random -- please feel free to suggest a
better one.)

<p>
<form method="POST" action="/makeaccount">
 <input type="submit" value="Try it out!">
</form>
'''


class HmphDispatcher(webserver.MetaDispatcher):

    def get_(self, http):
	http.send_html(welcome)

    def get_about(self, http):
	http.send_html(about)

    def post_makeaccount(self, http):
	import builtin
	account = builtin.make_account()
	add_account(get_id(account))
	http.redirect('%s' % get_uri(account))

    def get_id_V(self, http, hid):
	if not id_is_defined(hid):
	    http.send_error(404, 'Object Not Found: %s' % http.path)
	else:
	    access_id(hid)
	    http.send_html(get_actor(hid).show())

    def get_id_V_edit(self, http, hid, serial_id):
	actor = get_actor(hid)
	# XXX complain if serial_id is not an existing element
	http.send_html(actor.show_editable(int(serial_id)))

    def post_id_V_update(self, http, hid, serial_id, body):
	actor = get_actor(hid)
	element = actor.get_element(int(serial_id))
	element.set_body(body)
	http.redirect(element_uri(actor, element))

    def post_id_V_delete(self, http, hid, serial_id):
	actor = get_actor(hid)
	previous_element = actor.delete_element(int(serial_id))
	if previous_element is None:
	    uri = get_uri(actor)
	else:
	    uri = element_uri(actor, previous_element)
	http.redirect(uri)

    def post_id_V_addexample(self, http, hid, content):
	actor = get_actor(hid)
	example = actor.add_example(content)
	http.redirect(element_uri(actor, example))

    def post_id_V_addmethod(self, http, hid, content):
	actor = get_actor(hid)
	selector, parameters = parse_signature(content)
	actor.add_method(selector, parameters)
	element = actor.get_method(selector)
	http.redirect('%s/edit?%s#%s' % \
		      (get_uri(actor), 
		       urllib.urlencode({'serial_id': element.serial_id}),
		       element.serial_id))

    def post_id_V_addtext(self, http, hid, content):
	actor = get_actor(hid)
	text = actor.add_text(content)
	http.redirect(element_uri(actor, text))

    def post_id_V_call(self, http, hid, selector, **query):
	actor = get_actor(hid)
	# XXX what if query needs to contain 'selector' as a key?
	arguments = parse_args(actor.get_method(selector), query)
	result = actor.call(selector, arguments)
	http.redirect('%s' % get_uri(result))

dispatcher = HmphDispatcher()

class HmphHTTPRequestHandler(webserver.DispatchingHTTPRequestHandler):

    def _get_dispatcher(self):
	return dispatcher


def element_uri(actor, element):
    return '%s#%s' % (get_uri(actor), element.serial_id)

def parse_args(method, query):
    return [parse_arg(p, query) for p in method.parameters]

def parse_arg(p, query):
    if p not in query:
	raise 'Missing parameter', p
    lit_expr = parse_literal(query[p])
    return lit_expr.run(None, None)


def method_call_form(target, selector, argument_field):
    body = '<input type="submit" value="Call"> ' + argument_field
    return '''
   <form method="POST" action="%(uri)s/call">
    <input type="hidden" name="selector" value="%(selector)s">
    %(body)s
   </form>
''' % { 'uri': get_uri(target), 
	'selector': cgi.escape(selector, True),
	'body': body }

def element_delete_form(target, serial_id):
    return '''
   <form method="POST" action="%(uri)s/delete">
    <input type="hidden" name="serial_id" value="%(serial_id)s">
    <input type="submit" value="Delete">
   </form>
''' % { 'uri': get_uri(target), 
	'serial_id': serial_id }

def element_edit_form(target, serial_id):
    return '''
   <form method="GET" action="%(uri)s/edit#%(serial_id)s">
    <input type="hidden" name="serial_id" value="%(serial_id)s">
    <input type="submit" value="Edit">
   </form>
''' % { 'uri': get_uri(target), 
	'serial_id': serial_id }

def element_editor_form(target, serial_id, body):
    return '''
<form method="POST" action="%(uri)s/update">
<input type="hidden" name="serial_id" value="%(serial_id)s">
<input type="submit" value="Save">
<textarea name="body" style="width:100%%" rows="10">%(body)s</textarea>
</form>
''' % { 'uri': get_uri(target), 
	'serial_id': serial_id,
	'body': cgi.escape(body) }

def adder_form(target):
    return '''
<hr>
<form method="POST" action="%(uri)s/addmethod">
<input type="textarea" name="content">
<input type="submit" value="Add method">
</form>
<form method="POST" action="%(uri)s/addexample">
<input type="textarea" name="content">
<input type="submit" value="Add example">
</form>
<form method="POST" action="%(uri)s/addtext">
<textarea name="content" style="width:90%%" rows="10"></textarea><br>
<input type="submit" value="Add text">
</form>
''' % { 'uri': get_uri(target) }
