from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import sre
import sys
import urlparse


class DispatchingHTTPRequestHandler(BaseHTTPRequestHandler):

    def _get_dispatcher(self):
        abstract                # Ugh, the contortions.

    def do_GET(self):
        self._handle(self._get_dispatcher().getters, parse_qs)

    def do_POST(self):
        self._handle(self._get_dispatcher().posters, self._parse_post_params)

    def _parse_post_params(self, url_query_str):
        content_length = int(self.headers.getheader('Content-Length'))
        if content_length == 0:
            data = ''
        else:
            data = self.rfile.read(content_length)
        return parse_qs(data)

    def _handle(self, handlers, parse_query):
        _, _, path_str, _, query_str, _ = urlparse.urlparse(self.path)
        if path_str[0:1] == '/': # XXX does this ever not happen?
            path_str = path_str[1:]
        handler, params = _lookup(handlers, path_str)
        if handler is None:
            self.send_error(404, 'Object Not Found: %s' % self.path)
            return
        try:
            handler(self, *params, **parse_query(query_str))
        except:
            exception_type, exception_value = sys.exc_info()[:2]
            complaint = cgi.escape('%s: %s' % (exception_type, exception_value))
            self.send_html('Error: ' + complaint)
            raise

    def redirect(self, uri):
        self.send_response(302, uri)
        self.send_header('Location', uri)
        self.send_header('Content-type', 'text/html')
        self.end_headers() 
        self.wfile.write('Redirect to <a href="%s">%s</a>' % (uri, uri))

    def send_html(self, body):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(body)

def parse_qs(string):
    query = cgi.parse_qs(string)
    result = {}
    for key in query:
        if len(query[key]) != 1:
            raise 'Multiple values for key', key
        result[key] = query[key][0]
    return result

def _lookup(pairs, path_str):
    for (name, pattern), handler in pairs:
        m = pattern.match(path_str)
        if m:
            return handler, m.groups()
    return None, None

def parse_name(name):
    parts = name.split('_')
    patterns = [cond(part == 'V', r'([0-9a-f]+)', part) for part in parts]
    name = '/'.join(patterns) + '$'
    return name, sre.compile(name)

def cond(test, yes, no):
    if test: return yes
    return no


class MetaDispatcher:

    def __init__(self):
        self.getters = self._collect('get_')
        self.posters = self._collect('post_')

    def _collect(self, prefix):
        pairs = [(parse_name(name[len(prefix):]), getattr(self, name))
                 for name in dir(self) if name.startswith(prefix)]
        return tuple(pairs)
