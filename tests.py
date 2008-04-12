import sys

from actors  import Actor, Method, Script, void_actor
from builtin import Number, String, eqv
from envs    import Env, global_env
from parser  import Parser, parse, parser_tests


def test_expr(env, str, expected_result):
    code, decorators = parse(str)
    result = code.eval(env)
    if not(eqv(result, expected_result)):
	raise 'Bad result', result

def should_raise(env, str, exception_type):
    code, decorators = parse(str)
    try:
	code.eval(env)
    except:
	foo = sys.exc_info()
	if exception_type != foo[0]:
	    raise foo
    else:
	raise 'Expected an exception', exception_type

def tests():
    parser_tests()
    a = Actor(global_env,
	      Script([Method('method1', [], 'Hurary'), 
		      Method('method2:', ['x'], 'x')]))
    n = Number(3)
    env = Env(None, {'a': a, 'n': n})
    test_expr(env, 'a', a)
    should_raise(env, 'b', 'Unbound')
    should_raise(env, 'a method1', 'Unbound')
    should_raise(env, 'a foo', 'No matching method')
    test_expr(env, 'a method2: a', a)
    test_expr(env, 'n * n', Number(9))
    test_expr(env, 'a. n', n)
    test_expr(env, '', void_actor)
    test_expr(env, '42', Number(42))
    test_expr(env, '(a method2: 3) * 2', Number(6))

    s1 = Script([Method('run:', ['x'], 'make Foo')])
    s2 = Script([Method('multiply_by:', ['y'], 'x * y')])
    s1.get_method('run:').set_inner('Foo', s2)
    a1 = Actor(global_env, s1)
    env1 = Env(None, {'a1': a1})
    test_expr(env1, '(a1 run: 4) multiply_by: 5', Number(20))

    assert Method('f', [], 'ab. ab').mark_up_body(global_env) == 'ab. ab'
    assert Method('foo:', ['x'], 'x').get_signature() == 'foo: x'

    s = String('Hello, world!')
    env2 = Env(None, {'s': s})
    test_expr(env2, 's', String('Hello, ' + 'world!'))
    test_expr(env2, 's length', Number(13))
    test_expr(env2, 's from: 1 to: 5', String('Hello'))
    test_expr(env2, "'Hello, world!'", s)
    test_expr(env2, 'let x = 2 * 3. x * x', Number(36))
