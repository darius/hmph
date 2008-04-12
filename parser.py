import sre

from registry import get_actor, get_editor, get_id


def parse(e, inner_map={}):
    return Parser(e, inner_map).parse()

def parse_literal(string):
    p = Parser(string, {})
    expr = p.literal()
    p.done()
    return expr

def parse_signature(pattern):
    p = Parser('x ' + pattern, {})
    expr = p.expr()
    p.done()
    return expr.as_signature()

class Parser:

    '''
    stmts       = (expr ('.' expr)*)?
    expr        = primary unarymess* binarymess* keywordmess?
    unarymess   = unary_selector
    binarymess  = binary_selector primary unarymess*
    keywordmess = (keyword primary unarymess* binarymess*)+
    primary     = identifier
                | '(' expr ')'           XXX stmts instead?
                | literal
                | make identifier
                | let identifier = expr
                | '[' (expr (',' expr)*)? ']'
    literal     = numeric_lit | string_lit | http_lit
    '''

    numeric_lit = r'-?[0-9]+([.][0-9]+)?'
    string_lit = r"'[^']*'"	# XXX handle escape chars
    http_lit = r'http:(//[^/]*)?/id/([0-9a-f]+)'   # XXX must match my host
	# XXX http_lit should be followed only by whitespace or punctuation
    identifier = r'[A-Za-z_][A-Za-z_0-9]*(?![:A-Za-z_0-9])'
    keyword = r'[A-Za-z_][A-Za-z_0-9]*:'
    binary_selector = r'[-+/\\*~<>=@%|&?!]+'
    keyword_primitive = r'primitive(?![:A-Za-z_0-9])'
    keyword_make = r'make(?![:A-Za-z_0-9])'
    keyword_let = r'let(?![:A-Za-z_0-9])'
    eqsign = r'=(?![-:+/\\*~<>=@%|&?!,])'

    def __init__(self, str, inner_map):
	self.str = str
	self.i = 0
	self.inner_map = inner_map
	self.decorators = []

    def decorate(self, range, formatter):
	self.decorators.append((range, formatter))

    def parse(self):
	if self.primitive(True):
	    result = self.primitive()
	else:
	    result = self.stmts()
	self.done()
	return result, self.decorators

    def primitive(self, probe=False):
	if probe: 
	    return self.token(self.keyword_primitive, True)
	src_pos = self.i
	self.token(self.keyword_primitive)
	p = self.token(self.identifier)
	return Primitive((src_pos, self.i), p)

    def stmts(self, probe=False):
	if probe:
	    return True
	src_pos = self.i
	if not self.expr(True):
	    return EmptyStmt(((src_pos, self.i), self.i))
	e = self.expr()
	while self.token(r'[.]', True):
	    self.token(r'[.]')
	    r = self.expr()
	    e = SeqStmt((src_pos, self.i), e, r)
	return e

    def expr_list(self, probe=False):
	if probe:
	    return True
	es = []
	if not self.expr(True):
	    return es
	es.append(self.expr())
	while self.token(r',', True):
	    self.token(r',')
	    es.append(self.expr())
	return es

    def expr(self, probe=False):
	if probe:
	    return self.primary(probe)
	src_pos = self.i
	e = self.primary()
	while self.unary_message(True):
	    m = self.unary_message()
	    e = CallExpr((src_pos, self.i), e, m)
	while self.binary_message(True):
	    m = self.binary_message()
	    e = CallExpr((src_pos, self.i), e, m)
	if self.keyword_message(True):
	    m = self.keyword_message()
	    e = CallExpr((src_pos, self.i), e, m)
	return e

    def unary_message(self, probe=False):
	if probe:
	    return self.token(self.identifier, probe)
	return (self.token(self.identifier), [])

    def binary_message(self, probe=False):
	if probe:
	    return self.token(self.binary_selector, probe)
	selector = self.token(self.binary_selector)
	src_pos = self.i
	e = self.primary()
	while self.unary_message(True):
	    m = self.unary_message()
	    e = CallExpr((src_pos, self.i), e, m)
	return (selector, [e])

    def keyword_message(self, probe=False):
	if probe:
	    return self.token(self.keyword, probe)
	keywords = []
	arg_exprs = []
	while self.token(self.keyword, True):
	    keywords.append(self.token(self.keyword))
	    src_pos = self.i
	    e = self.primary()
	    while self.unary_message(True):
		m = self.unary_message()
		e = CallExpr((src_pos, self.i), e, m)
	    while self.binary_message(True):
		m = self.binary_message()
		e = CallExpr((src_pos, self.i), e, m)
	    arg_exprs.append(e)
	return (''.join(keywords), arg_exprs)

    def literal(self, probe=False):
	if probe:
	    return self.token(self.numeric_lit, probe) or \
		self.token(self.string_lit, probe) or \
		self.token(self.http_lit, probe)
	src_pos = self.i
	if self.token(self.numeric_lit, True):
	    lit = self.token(self.numeric_lit)
	    return NumericLitExpr((src_pos, self.i), cook_number(lit))
	elif self.token(self.string_lit, True):
	    lit = self.token(self.string_lit)
	    return StringLitExpr((src_pos, self.i), cook_string(lit))
	elif self.token(self.http_lit, True):
	    lit = self.token(self.http_lit)
	    m = sre.match(self.http_lit, lit)
	    range = (src_pos, self.i)
	    self.decorate(range, format_http_link)
	    return HttpLitExpr(range, m.group(2))
	else:
	    raise ParseError(self, 'Bad literal: ' + self.str[src_pos:])

    def primary(self, probe=False):
	if probe:
	    return self.token(self.keyword_let, probe) or \
		self.nested_object(probe) or \
		self.token(self.identifier, probe) or \
		self.literal(probe) or \
		self.token(r'[(]', probe) or \
		self.token(r'[[]', probe)
	src_pos = self.i
	if self.token(self.keyword_let, True):
	    # XXX maybe this should be off in the stmts production or something
	    self.token(self.keyword_let)
	    name = self.token(self.identifier)
	    self.token(self.eqsign)
	    e = self.expr()
	    return LetExpr((src_pos, self.i), name, e)
	elif self.nested_object(True):
	    return self.nested_object()
	elif self.token(self.identifier, True):
	    name, range = self.token_and_range(self.identifier)
	    self.decorate(range, format_variable)
	    return VarExpr((src_pos, self.i), name)
	elif self.literal(True):
	    return self.literal()
	elif self.token(r'[(]', True):
	    self.token(r'[(]')
	    e = self.expr()
	    self.token(r'[)]')
	    return e
	elif self.token(r'\[', True):
	    self.token(r'\[')
	    es = self.expr_list()
	    self.token(r'\]')
	    return ListExpr((src_pos, self.i), es)
	else:
	    raise ParseError(self, 'Bad primary')

    def nested_object(self, probe=False):
	if probe: 
	    return self.token(self.keyword_make, True)
	src_pos = self.i
	self.token(self.keyword_make)
	name_pos = self.i
	name = self.token(self.identifier)
	self.decorate((name_pos, self.i), format_nested_object)
	if name not in self.inner_map:
	    from actors import Script
	    self.inner_map[name] = Script([])
	return NestExpr((src_pos, self.i), name, self.inner_map[name])

    def token(self, pattern, probe=False):
	# XXX this code should be shorter
	s = sre.match(r'\s+', self.str[self.i:])
	if s: 
	    self.i += s.end()
	m = sre.match(pattern, self.str[self.i:])
	if not m: 
	    return False
	if probe:
	    return True
	start, end = self.i + m.start(), self.i + m.end()
	self.i += m.end()
	return self.str[start:end]

    def token_and_range(self, pattern):
	m = sre.match(pattern, self.str[self.i:])
	start, end = self.i + m.start(), self.i + m.end()
	self.i += m.end()
	return self.str[start:end], (start, end)

    def done(self):
	self.token('')   # skip whitespace
	if self.i != len(self.str):
	    raise ParseError(self, 'Incomplete expression: ' + self.str)


class ParseError:
    def __init__(self, parser, message):
	self.parser = parser
	self.message = message
    def __repr__(self):
	return '<ParseError: %s>' % self.message


def format_variable(string, env, inner_map):
    value = env.get(string)
    if value is not None:
	return '<a href="/id/%s">%s</a>' % (get_id(get_editor(value)), string)
    return string

def format_nested_object(string, env, inner_map):
    name = string.strip()
    if name in inner_map:
	return ' <a href="/id/%s">%s</a>' % (get_id(inner_map[name]), name)
    return string

def format_http_link(string, env, inner_map):
    link = string.strip()
    return '<a href="%s">%s</a>' % (link, link)


class Code:
    def __init__(self, src_range):
	self.src_range = src_range
    def run(self, actor, env):
	return self.eval(env)
    def as_signature(self):
	raise 'Bad pattern'

class Primitive(Code):
    def __init__(self, src_range, name):
	Code.__init__(self, src_range)
	self.name = name
    def __repr__(self):
	return 'primitive %s' % self.name
    def run(self, actor, env):
	if actor.primitive_data is None:
	    raise 'No primitive data', actor
	return getattr(actor, 'prim_' + self.name)(env)

class EmptyStmt(Code):
    def __repr__(self):
	return 'EmptyStmt'
    def eval(self, env):
	from actors import void_actor # XXX circular dependency
	return void_actor

class SeqStmt(Code):
    def __init__(self, src_range, e1, e2):
	Code.__init__(self, src_range)
	self.e1 = e1
	self.e2 = e2
    def __repr__(self):
	return '%s. %s' % (self.e1, self.e2)
    def eval(self, env):
	self.e1.eval(env)
	return self.e2.eval(env)

class NestExpr(Code):
    def __init__(self, src_range, name, script):
	Code.__init__(self, src_range)
	self.name = name
	self.script = script
    def __repr__(self):
	return '<object %s>' % self.name
    def eval(self, env):
	from actors import Actor, void_actor # XXX circular dependency
	nested_env = env.sprout()
	env.define(self.name, void_actor) # XXX need some other marker
	result = Actor(nested_env, self.script)
	env.define(self.name, result)
	return result

class LetExpr(Code):
    def __init__(self, src_range, name, expr):
	Code.__init__(self, src_range)
	self.name = name
	self.expr = expr
    def __repr__(self):
	return '(let %s = %s)' % (self.name, self.expr)
    def eval(self, env):
	value = self.expr.eval(env)
	env.define(self.name, value)
	return value

class CallExpr(Code):
    def __init__(self, src_range, subject, (selector, arg_exprs)):
	Code.__init__(self, src_range)
	self.subject = subject
	self.selector = selector
	self.arg_exprs = arg_exprs
    def __repr__(self):
	args = ', '.join([`e` for e in self.arg_exprs])
	if args == '':
	    return '(%s %s)' % (self.subject, self.selector)
	elif len(self.arg_exprs) == 1:
	    return '(%s %s %s)' % (self.subject, self.selector, args)
	else:
	    return '(%s %s {%s})' % (self.subject, self.selector, args)
    def eval(self, env):
	subject = self.subject.eval(env)
	arguments = [ae.eval(env) for ae in self.arg_exprs]
	return subject.call(self.selector, arguments)
    def as_signature(self):
	params = []
	for ae in self.arg_exprs:
	    assert ae.__class__ == VarExpr
	    params.append(ae.name)
	return (self.selector, params)

class ListExpr(Code):
    def __init__(self, src_range, exprs):
	Code.__init__(self, src_range)
	self.exprs = exprs
    def __repr__(self):
	return '[%s]' % ', '.join(map(repr, self.exprs))
    def eval(self, env):
	import builtin
	return builtin.List([e.eval(env) for e in self.exprs])

class VarExpr(Code):
    def __init__(self, src_range, name):
	Code.__init__(self, src_range)
	self.name = name
    def __repr__(self):
	return self.name
    def eval(self, env):
	return env.must_get(self.name)

class NumericLitExpr(Code):
    def __init__(self, src_range, literal):
	Code.__init__(self, src_range)
	self.literal = literal
    def __repr__(self):
	return `self.literal`
    def eval(self, env):
	from builtin import Number # XXX circular module dependency
	return Number(self.literal)

def cook_number(str):
    return float(str)		# XXX handle integers

class StringLitExpr(Code):
    def __init__(self, src_range, literal):
	Code.__init__(self, src_range)
	self.literal = literal
    def __repr__(self):
	return "'%s'" % self.literal # XXX escape quotes
    def eval(self, env):
	from builtin import String # XXX circular module dependency
	return String(self.literal)

def cook_string(str):
    # Trim off the leading and trailing quotes:
    return str[1:-1]		# XXX handle escape chars

class HttpLitExpr(Code):
    def __init__(self, src_range, hid):
	Code.__init__(self, src_range)
	self.hid = hid
    def __repr__(self):
	return 'http:/id/%s' % self.hid
    def eval(self, env):
	return get_actor(self.hid)


def test_syntax(str, reunparsed):
    code, decorators = parse(str)
    result = `code`
    if result != reunparsed:
	raise 'Bad parse/unparse', result

def parser_tests():
    test_syntax('primitive  multiply', 'primitive multiply')
    test_syntax('a bc: d', '(a bc: d)')
    test_syntax('[]', '[]')
    test_syntax('[1, a, 2 + 3]', '[1.0, a, (2.0 + 3.0)]')
    test_syntax('http:/id/12345', 'http:/id/12345')
    assert parse_signature('squared') == ('squared', [])
    assert parse_signature('foo: x') == ('foo:', ['x'])
    assert parse_signature('* a_number') == ('*', ['a_number'])
    assert parse_signature('at: place put: value') == \
	('at:put:', ['place', 'value'])
