import actors
import builtin
import envs
import registry

L171 = envs.Env(parent=None)
L170 = envs.Env(parent=L171)
L210 = envs.Env(parent=L170)
L212 = envs.Env(parent=L210)
L845 = envs.Env(parent=L212)
L848 = actors.Script(elements=[],
                     next_serial_id=0)
L843 = actors.Actor(env=envs.Env(parent=L845),
                    script=L848)
L842 = actors.ActorEditor(editable=True,
                          actor=L843)
L531 = envs.Env(parent=None)
L530 = envs.Env(parent=L531)
L571 = actors.Script(elements=[actors.Method(body=actors.Expression(text='let ballotbox = makebox holding: 0',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='run')],
                     next_serial_id=1)
L569 = actors.Actor(env=envs.Env(parent=L530),
                    script=L571)
L972 = actors.ActorEditor(editable=True,
                          actor=L569)
L224 = envs.Env(parent=L210)
L246 = envs.Env(parent=L224)
L245 = envs.Env(parent=L246)
L235 = actors.Script(elements=[actors.Text(body="I'm out of guesses about your animal.  Please tell me its name and a new question I can ask, so that your animal has a yes answer.  Thanks!",
                                           serial_id=0),
                               actors.Method(body=actors.Expression(text="box <- (makequestion asking: question ifyes: (makeguess name: animal parent: box) ifno: (box get)).\r\n'OK!'\r\n",
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=['animal',
                                                         'question'],
                                             selector='name:question:')],
                     next_serial_id=2)
L228 = actors.Script(elements=[actors.Method(body=actors.Expression(text="'Is it a ' + animal + '?'\r\n",
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='run'),
                               actors.Method(body=actors.Expression(text="'Thank you!'\r\n",
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='yes'),
                               actors.Method(body=actors.Expression(text='make question',
                                                                    inner_map={'question': L235}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='no')],
                     next_serial_id=3)
L244 = actors.Actor(env=L245,
                    script=L228)
L1410 = actors.ActorEditor(editable=True,
                           actor=L244)
L654 = builtin.Boolean(value=False,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='falsevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L670 = builtin.Box(initial_value=L654)
L1632 = actors.ActorEditor(editable=False,
                           actor=L670)
L124 = builtin.Boolean(value=False,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='falseaction run',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['trueaction',
                                                                                'falseaction'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L1479 = actors.ActorEditor(editable=False,
                           actor=L124)
L796 = builtin.List(elements=(builtin.String(str='hello'),))
L795 = actors.ActorEditor(editable=False,
                          actor=L796)
L172 = builtin.Boolean(value=False,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='falsevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L194 = builtin.Box(initial_value=L172)
L961 = actors.ActorEditor(editable=False,
                          actor=L194)
L765 = builtin.Box(initial_value=builtin.List(elements=()))
L1494 = actors.ActorEditor(editable=False,
                           actor=L765)
L542 = builtin.BoxMaker()
L1234 = actors.ActorEditor(editable=False,
                           actor=L542)
L2 = builtin.String(str='dog')
L1 = actors.ActorEditor(editable=False,
                        actor=L2)
L965 = builtin.Number(n=40.0)
L964 = actors.ActorEditor(editable=False,
                          actor=L965)
L464 = builtin.String(str='<p>')
L1258 = actors.ActorEditor(editable=False,
                           actor=L464)
L717 = envs.Env(parent=None)
L716 = envs.Env(parent=L717)
L715 = envs.Env(parent=L716)
L747 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='first'),
                               actors.Method(body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='removefirst'),
                               actors.Method(body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='sender')],
                     next_serial_id=3)
L713 = actors.Actor(env=envs.Env(parent=L715),
                    script=L747)
L712 = actors.ActorEditor(editable=True,
                          actor=L713)
L1396 = builtin.List(elements=(builtin.String(str='hello'),))
L1609 = actors.ActorEditor(editable=False,
                           actor=L1396)
L386 = builtin.Boolean(value=False,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='falseaction run',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['trueaction',
                                                                                'falseaction'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L394 = builtin.Box(initial_value=L386)
L1185 = actors.ActorEditor(editable=False,
                           actor=L394)
L169 = envs.Env(parent=L170)
L279 = envs.Env(parent=L169)
L328 = envs.Env(parent=L279)
L327 = envs.Env(parent=L328)
L1646 = envs.Env(parent=L327)
L286 = actors.Script(elements=[actors.Method(body=actors.Expression(text='question',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='question'),
                               actors.Method(body=actors.Expression(text='call on: yesbox',
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='yes'),
                               actors.Method(body=actors.Expression(text='call on: nobox',
                                                                    inner_map={}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='no')],
                     next_serial_id=3)
L1644 = actors.Actor(env=envs.Env(parent=L1646),
                     script=L286)
L1643 = actors.ActorEditor(editable=True,
                           actor=L1644)
L1066 = builtin.Number(n=25.0)
L1065 = actors.ActorEditor(editable=False,
                           actor=L1066)
L768 = builtin.Number(n=25.0)
L767 = actors.ActorEditor(editable=False,
                          actor=L768)
L283 = actors.Script(elements=[actors.Method(body=actors.Expression(text='make asker',
                                                                    inner_map={'asker': L286}),
                                             serial_id=0,
                                             parameters=['node'],
                                             selector='on:')],
                     next_serial_id=1)
L326 = actors.Actor(env=L327,
                    script=L283)
L325 = builtin.Box(initial_value=L326)
L1627 = actors.ActorEditor(editable=False,
                           actor=L325)
L378 = envs.Env(parent=None)
L377 = envs.Env(parent=L378)
L396 = envs.Env(parent=L377)
L442 = actors.Script(elements=[actors.Method(body=actors.Expression(text="' ' + attribute show + string",
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['attribute',
                                                         'string'],
                                             selector='left:right:'),
                               actors.Text(body='XXX rename this since it generically applies to html elements',
                                           serial_id=1)],
                     next_serial_id=2)
L440 = actors.Actor(env=envs.Env(parent=L396),
                    script=L442)
L1628 = actors.ActorEditor(editable=True,
                           actor=L440)
L490 = builtin.Stamp()
L491 = builtin.StampGuard(stamp=L490)
L489 = builtin.List(elements=(L490,
                              L491))
L508 = actors.ActorEditor(editable=False,
                          actor=L489)
L505 = builtin.Number(n=25.0)
L504 = actors.ActorEditor(editable=False,
                          actor=L505)
L1567 = builtin.Number(n=6.0)
L1637 = actors.ActorEditor(editable=False,
                           actor=L1567)
L881 = builtin.Boolean(value=False,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='falsevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L880 = actors.ActorEditor(editable=False,
                          actor=L881)
L77 = builtin.Number(n=25.0)
L1365 = actors.ActorEditor(editable=False,
                           actor=L77)
L385 = builtin.StampMaker()
L1244 = actors.ActorEditor(editable=False,
                           actor=L385)
L804 = envs.Env(parent=None)
L803 = envs.Env(parent=L804)
L831 = actors.Script(elements=[],
                     next_serial_id=0)
L829 = actors.Actor(env=envs.Env(parent=L803),
                    script=L831)
L1134 = actors.ActorEditor(editable=True,
                           actor=L829)
L1192 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1195 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L584 = actors.Script(elements=[],
                     next_serial_id=0)
L1198 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L584}),
                       serial_id=4)
L1201 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1203 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1205 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1207 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1212 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1215 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L578 = actors.Script(elements=[actors.Text(body='Hi - time to vote on where to go out for lunch.  Pick a method for the restaurant you like and click it.',
                                           serial_id=0),
                               actors.Method(body=actors.Expression(text='',
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='voteforstarbucks')],
                     next_serial_id=2)
L1219 = actors.Example(expression=actors.Expression(text='mailbox sender send: make message',
                                                    inner_map={'message': L578}),
                       serial_id=16)
L1221 = actors.Example(expression=actors.Expression(text='makek makeballot',
                                                    inner_map={}),
                       serial_id=17)
L1223 = actors.Example(expression=actors.Expression(text='make makeballot',
                                                    inner_map={'makeballot': L571}),
                       serial_id=18)
L1189 = actors.Actor(env=L530,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1192,
                                                    L1195,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1198,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1201,
                                                    L1203,
                                                    L1205,
                                                    L1207,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1212,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1215,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1219,
                                                    L1221,
                                                    L1223],
                                          next_serial_id=19))
L1188 = actors.ActorEditor(editable=True,
                           actor=L1189)
L6 = envs.Env(parent=None)
L5 = envs.Env(parent=L6)
L67 = actors.Script(elements=[actors.Method(body=actors.Expression(text="'Hello, Alex! How are you?'",
                                                                   inner_map={}),
                                            serial_id=0,
                                            parameters=[],
                                            selector='greet')],
                    next_serial_id=1)
L65 = actors.Actor(env=envs.Env(parent=L5),
                   script=L67)
L1060 = actors.ActorEditor(editable=True,
                           actor=L65)
L1414 = envs.Env(parent=None)
L1413 = envs.Env(parent=L1414)
L1412 = actors.Actor(env=L1413,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    actors.Example(expression=actors.Expression(text='2 + 3',
                                                                                                inner_map={}),
                                                                   serial_id=1),
                                                    actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                                                                inner_map={}),
                                                                   serial_id=2),
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    actors.Example(expression=actors.Expression(text='make Foo',
                                                                                                inner_map={}),
                                                                   serial_id=4),
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                                                                inner_map={}),
                                                                   serial_id=6),
                                                    actors.Example(expression=actors.Expression(text='box get',
                                                                                                inner_map={}),
                                                                   serial_id=7),
                                                    actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                                                                inner_map={}),
                                                                   serial_id=8),
                                                    actors.Example(expression=actors.Expression(text="['hello']",
                                                                                                inner_map={}),
                                                                   serial_id=9),
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    actors.Example(expression=actors.Expression(text='maildirectory',
                                                                                                inner_map={}),
                                                                   serial_id=11),
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                                                                inner_map={}),
                                                                   serial_id=13),
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15)],
                                          next_serial_id=16))
L1411 = actors.ActorEditor(editable=True,
                           actor=L1412)
L306 = envs.Env(parent=L169)
L348 = envs.Env(parent=L306)
L347 = envs.Env(parent=L348)
L365 = envs.Env(parent=L347)
L364 = envs.Env(parent=L365)
L1253 = envs.Env(parent=L364)
L321 = actors.Script(elements=[actors.Text(body="I'm out of ideas about your animal -- please tell me its name and a question to ask in the future, such that yes is the right answer for it.",
                                           serial_id=0),
                               actors.Method(body=actors.Expression(text="node <- (makebranch on: question ifyes: (makebox holding: (makeguess for: animal)) ifno: (makebox holding: guessernode)).\r\n'Thanks, I will remember.'",
                                                                    inner_map={}),
                                             serial_id=2,
                                             parameters=['animal',
                                                         'question'],
                                             selector='name:question:')],
                     next_serial_id=3)
L1251 = actors.Actor(env=envs.Env(parent=L1253),
                     script=L321)
L1250 = actors.ActorEditor(editable=True,
                           actor=L1251)
L1129 = builtin.Number(n=29.0)
L1128 = actors.ActorEditor(editable=False,
                           actor=L1129)
L314 = actors.Script(elements=[actors.Method(body=actors.Expression(text="'Is it a ' + animal + '?'",
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='question'),
                               actors.Method(body=actors.Expression(text="'Wavy!'",
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='yes'),
                               actors.Method(body=actors.Expression(text='make terminus',
                                                                    inner_map={'terminus': L321}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='no')],
                     next_serial_id=3)
L311 = actors.Script(elements=[actors.Method(body=actors.Expression(text='make guesser',
                                                                    inner_map={'guesser': L314}),
                                             serial_id=0,
                                             parameters=['node'],
                                             selector='on:')],
                     next_serial_id=1)
L346 = actors.Actor(env=L347,
                    script=L311)
L345 = builtin.Box(initial_value=L346)
L960 = actors.ActorEditor(editable=False,
                          actor=L345)
L802 = envs.Env(parent=L803)
L822 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='first'),
                               actors.Method(body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='removefirst'),
                               actors.Method(body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='sender')],
                     next_serial_id=3)
L800 = actors.Actor(env=envs.Env(parent=L802),
                    script=L822)
L799 = actors.ActorEditor(editable=True,
                          actor=L800)
L1125 = actors.ActorEditor(editable=False,
                           actor=L386)
L841 = actors.Script(elements=[],
                     next_serial_id=0)
L839 = actors.Actor(env=envs.Env(parent=L396),
                    script=L841)
L838 = actors.ActorEditor(editable=True,
                          actor=L839)
L1039 = actors.ActorEditor(editable=False,
                           actor=L654)
L771 = builtin.Boolean(value=False,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='falsevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L770 = builtin.Box(initial_value=L771)
L769 = actors.ActorEditor(editable=False,
                          actor=L770)
L268 = builtin.MailDirectory(env=envs.Env(parent=L171))
L1027 = actors.ActorEditor(editable=False,
                           actor=L268)
L853 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                   inner_map={}),
                      serial_id=1)
L856 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                   inner_map={}),
                      serial_id=2)
L859 = actors.Example(expression=actors.Expression(text='make Foo',
                                                   inner_map={'Foo': L831}),
                      serial_id=4)
L862 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                   inner_map={}),
                      serial_id=6)
L864 = actors.Example(expression=actors.Expression(text='box get',
                                                   inner_map={}),
                      serial_id=7)
L866 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                   inner_map={}),
                      serial_id=8)
L868 = actors.Example(expression=actors.Expression(text="['hello']",
                                                   inner_map={}),
                      serial_id=9)
L871 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                   inner_map={}),
                      serial_id=11)
L874 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                   inner_map={}),
                      serial_id=13)
L878 = actors.Example(expression=actors.Expression(text='let pair = makestamp run',
                                                   inner_map={}),
                      serial_id=16)
L850 = actors.Actor(env=L803,
                    script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                               serial_id=0),
                                                   L853,
                                                   L856,
                                                   actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                               serial_id=3),
                                                   L859,
                                                   actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                               serial_id=5),
                                                   L862,
                                                   L864,
                                                   L866,
                                                   L868,
                                                   actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                               serial_id=10),
                                                   L871,
                                                   actors.Text(body='You can create your own mailbox:',
                                                               serial_id=12),
                                                   L874,
                                                   actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                               serial_id=14),
                                                   actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                               serial_id=15),
                                                   L878],
                                         next_serial_id=17))
L849 = actors.ActorEditor(editable=True,
                          actor=L850)
L934 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                   inner_map={}),
                      serial_id=1)
L937 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                   inner_map={}),
                      serial_id=2)
L757 = actors.Example(expression=actors.Expression(text='1 * 2 * 3 * 4 * 5',
                                                   inner_map={}),
                      serial_id=0)
L756 = actors.Script(elements=[L757],
                     next_serial_id=1)
L941 = actors.Example(expression=actors.Expression(text='make Foo',
                                                   inner_map={'Foo': L756}),
                      serial_id=4)
L944 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                   inner_map={}),
                      serial_id=6)
L946 = actors.Example(expression=actors.Expression(text='box get',
                                                   inner_map={}),
                      serial_id=7)
L948 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                   inner_map={}),
                      serial_id=8)
L950 = actors.Example(expression=actors.Expression(text="['hello']",
                                                   inner_map={}),
                      serial_id=9)
L953 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                   inner_map={}),
                      serial_id=11)
L956 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                   inner_map={}),
                      serial_id=13)
L931 = actors.Actor(env=L716,
                    script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                               serial_id=0),
                                                   L934,
                                                   L937,
                                                   actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                               serial_id=3),
                                                   L941,
                                                   actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                               serial_id=5),
                                                   L944,
                                                   L946,
                                                   L948,
                                                   L950,
                                                   actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                               serial_id=10),
                                                   L953,
                                                   actors.Text(body='You can create your own mailbox:',
                                                               serial_id=12),
                                                   L956,
                                                   actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                               serial_id=14),
                                                   actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                               serial_id=15)],
                                         next_serial_id=16))
L930 = actors.ActorEditor(editable=True,
                          actor=L931)
L1077 = envs.Env(parent=None)
L1076 = envs.Env(parent=L1077)
L1099 = envs.Env(parent=L1076)
L1107 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
                                                                     inner_map={}),
                                              serial_id=0,
                                              parameters=[],
                                              selector='first'),
                                actors.Method(body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                     inner_map={}),
                                              serial_id=1,
                                              parameters=[],
                                              selector='removefirst'),
                                actors.Method(body=actors.Expression(text='sender',
                                                                     inner_map={}),
                                              serial_id=2,
                                              parameters=[],
                                              selector='sender')],
                      next_serial_id=3)
L1097 = actors.Actor(env=envs.Env(parent=L1099),
                     script=L1107)
L1634 = actors.ActorEditor(editable=True,
                           actor=L1097)
L1617 = actors.ActorEditor(editable=False,
                           actor=L771)
L1688 = builtin.String(str='hello world!')
L1687 = actors.ActorEditor(editable=False,
                           actor=L1688)
L90 = builtin.List(elements=(builtin.String(str='hello'),))
L1063 = actors.ActorEditor(editable=False,
                           actor=L90)
L342 = envs.Env(parent=L306)
L341 = envs.Env(parent=L342)
L783 = envs.Env(parent=L341)
L782 = envs.Env(parent=L783)
L781 = actors.Actor(env=L782,
                    script=L314)
L780 = actors.ActorEditor(editable=True,
                          actor=L781)
L711 = envs.Env(parent=L245)
L709 = actors.Actor(env=envs.Env(parent=L711),
                    script=L235)
L708 = actors.ActorEditor(editable=True,
                          actor=L709)
L653 = envs.Env(parent=None)
L652 = envs.Env(parent=L653)
L651 = envs.Env(parent=L652)
L678 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='first'),
                               actors.Method(body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='removefirst'),
                               actors.Method(body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='sender')],
                     next_serial_id=3)
L700 = actors.Actor(env=envs.Env(parent=L651),
                    script=L678)
L1484 = actors.ActorEditor(editable=True,
                           actor=L700)
L242 = envs.Env(parent=L212)
L216 = actors.Script(elements=[actors.Method(body=actors.Expression(text='query',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='question'),
                               actors.Method(body=actors.Expression(text='onyes\r\n',
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='yes'),
                               actors.Method(body=actors.Expression(text='onno\r\n',
                                                                    inner_map={}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='no')],
                     next_serial_id=3)
L240 = actors.Actor(env=envs.Env(parent=L242),
                    script=L216)
L239 = builtin.Box(initial_value=L240)
L647 = actors.ActorEditor(editable=False,
                          actor=L239)
L675 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L671 = actors.Actor(env=L652,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L675,
                                                                                                   'mailbox': L678}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L1495 = actors.ActorEditor(editable=True,
                           actor=L671)
L695 = builtin.MailDirectory(env=envs.Env(parent=L653))
L1033 = actors.ActorEditor(editable=False,
                           actor=L695)
L1640 = builtin.String(str='Is it a cat?')
L1639 = actors.ActorEditor(editable=False,
                           actor=L1640)
L1648 = builtin.Number(n=5.0)
L1647 = actors.ActorEditor(editable=False,
                           actor=L1648)
L1131 = actors.Actor(env=L653,
                     script=actors.Script(elements=[],
                                          next_serial_id=0))
L1130 = actors.ActorEditor(editable=True,
                           actor=L1131)
L398 = builtin.Stamp()
L397 = builtin.StampGuard(stamp=L398)
L1243 = actors.ActorEditor(editable=False,
                           actor=L397)
L909 = builtin.List(elements=(builtin.String(str='hello'),))
L1036 = actors.ActorEditor(editable=False,
                           actor=L909)
L109 = actors.Actor(env=L6,
                    script=actors.Script(elements=[],
                                         next_serial_id=0))
L1031 = actors.ActorEditor(editable=True,
                           actor=L109)
L1624 = builtin.String(str='Thank you!')
L1623 = actors.ActorEditor(editable=False,
                           actor=L1624)
L118 = builtin.Number(n=5.0)
L117 = actors.ActorEditor(editable=False,
                          actor=L118)
L687 = envs.Env(parent=L652)
L685 = actors.Actor(env=envs.Env(parent=L687),
                    script=L678)
L1622 = actors.ActorEditor(editable=True,
                           actor=L685)
L392 = builtin.BoxMaker()
L509 = actors.ActorEditor(editable=False,
                          actor=L392)
L789 = builtin.Boolean(value=False,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='falseaction run',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['trueaction',
                                                                                'falseaction'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L814 = builtin.Box(initial_value=L789)
L1072 = actors.ActorEditor(editable=False,
                           actor=L814)
L574 = builtin.MailDirectory(env=envs.Env(parent=L531))
L1649 = actors.ActorEditor(editable=False,
                           actor=L574)
L707 = builtin.String(str='hello')
L1576 = builtin.List(elements=(L707,))
L1575 = actors.ActorEditor(editable=False,
                           actor=L1576)
L182 = builtin.BoxMaker()
L1638 = actors.ActorEditor(editable=False,
                           actor=L182)
L1151 = builtin.Number(n=25.0)
L1231 = actors.ActorEditor(editable=False,
                           actor=L1151)
L130 = builtin.BoxMaker()
L525 = actors.ActorEditor(editable=False,
                          actor=L130)
L37 = actors.Script(elements=[actors.Text(body='Hi, there.  ',
                                          serial_id=0)],
                    next_serial_id=1)
L35 = actors.Actor(env=envs.Env(parent=L5),
                   script=L37)
L1236 = actors.ActorEditor(editable=True,
                           actor=L35)
L243 = builtin.String(str='Does it meow?')
L1489 = actors.ActorEditor(editable=False,
                           actor=L243)
L1374 = builtin.String(str='Hello, Alex!')
L1373 = actors.ActorEditor(editable=False,
                           actor=L1374)
L744 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L763 = actors.Actor(env=envs.Env(parent=L715),
                    script=L744)
L1635 = actors.ActorEditor(editable=True,
                           actor=L763)
L1023 = actors.Actor(env=L531,
                     script=actors.Script(elements=[],
                                          next_serial_id=0))
L1022 = actors.ActorEditor(editable=True,
                           actor=L1023)
L1121 = builtin.Number(n=25.0)
L1120 = actors.ActorEditor(editable=False,
                           actor=L1121)
L1297 = envs.Env(parent=None)
L1296 = envs.Env(parent=L1297)
L1295 = actors.Actor(env=L1296,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    actors.Example(expression=actors.Expression(text='2 + 3',
                                                                                                inner_map={}),
                                                                   serial_id=1),
                                                    actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                                                                inner_map={}),
                                                                   serial_id=2),
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    actors.Example(expression=actors.Expression(text='make Foo',
                                                                                                inner_map={}),
                                                                   serial_id=4),
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                                                                inner_map={}),
                                                                   serial_id=6),
                                                    actors.Example(expression=actors.Expression(text='box get',
                                                                                                inner_map={}),
                                                                   serial_id=7),
                                                    actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                                                                inner_map={}),
                                                                   serial_id=8),
                                                    actors.Example(expression=actors.Expression(text="['hello']",
                                                                                                inner_map={}),
                                                                   serial_id=9),
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    actors.Example(expression=actors.Expression(text='maildirectory',
                                                                                                inner_map={}),
                                                                   serial_id=11),
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                                                                inner_map={}),
                                                                   serial_id=13),
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15)],
                                          next_serial_id=16))
L1294 = actors.ActorEditor(editable=True,
                           actor=L1295)
L1614 = builtin.String(str='<p>')
L1613 = actors.ActorEditor(editable=False,
                           actor=L1614)
L1488 = builtin.Number(n=5.0)
L1487 = actors.ActorEditor(editable=False,
                           actor=L1488)
L158 = builtin.Box(initial_value=builtin.List(elements=()))
L1368 = actors.ActorEditor(editable=False,
                           actor=L158)
L971 = builtin.Box(initial_value=L881)
L970 = actors.ActorEditor(editable=False,
                          actor=L971)
L532 = builtin.Boolean(value=False,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='falsevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L554 = builtin.Box(initial_value=L532)
L1247 = actors.ActorEditor(editable=False,
                           actor=L554)
L249 = actors.Example(expression=actors.Expression(text='let gamebox = makebox holding: 0',
                                                   inner_map={}),
                      serial_id=1)
L225 = actors.Script(elements=[actors.Method(body=actors.Expression(text='make guess\r\n',
                                                                    inner_map={'guess': L228}),
                                             serial_id=0,
                                             parameters=['animal',
                                                         'box'],
                                             selector='name:parent:')],
                     next_serial_id=1)
L252 = actors.Example(expression=actors.Expression(text='make makeguess',
                                                   inner_map={'makeguess': L225}),
                      serial_id=2)
L254 = actors.Example(expression=actors.Expression(text="makeguess name: 'dog' parent: gamebox",
                                                   inner_map={}),
                      serial_id=3)
L259 = actors.Example(expression=actors.Expression(text='gamebox get',
                                                   inner_map={}),
                      serial_id=4)
L248 = actors.Script(elements=[L249,
                               L252,
                               L254,
                               L259],
                     next_serial_id=5)
L209 = actors.Actor(env=L210,
                    script=L248)
L251 = actors.ActorEditor(editable=True,
                          actor=L209)
L310 = actors.Script(elements=[],
                     next_serial_id=0)
L307 = actors.Script(elements=[actors.Method(body=actors.Expression(text='make guessernode',
                                                                    inner_map={'guesser': L310,
                                                                               'guessernode': L311}),
                                             serial_id=0,
                                             parameters=['animal'],
                                             selector='for:')],
                     next_serial_id=1)
L305 = actors.Actor(env=L306,
                    script=L307)
L1618 = actors.ActorEditor(editable=True,
                           actor=L305)
L123 = envs.Env(parent=None)
L160 = builtin.MailDirectory(env=envs.Env(parent=L123))
L798 = actors.ActorEditor(editable=False,
                          actor=L160)
L1124 = builtin.Number(n=42.0)
L1123 = actors.ActorEditor(editable=False,
                           actor=L1124)
L404 = actors.Script(elements=[actors.Method(body=actors.Expression(text="'<' + tag + (attributes foldr: showattr initially: '>')",
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='show')],
                     next_serial_id=1)
L412 = actors.Script(elements=[actors.Method(body=actors.Expression(text="'<' + tag + (attributes foldr: showattr initially: '>') + \r\n  (elements foldr: showattr initially: '') + \r\n  '</' + tag + '>'",
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='show')],
                     next_serial_id=1)
L419 = actors.Script(elements=[],
                     next_serial_id=0)
L420 = actors.Script(elements=[],
                     next_serial_id=0)
L421 = actors.Script(elements=[],
                     next_serial_id=0)
L422 = actors.Script(elements=[],
                     next_serial_id=0)
L401 = actors.Script(elements=[actors.Method(body=actors.Expression(text='stringguard check: tag.\r\nlistguard check: attributes.\r\nhtmlstamp stamp: make element',
                                                                    inner_map={'element': L404}),
                                             serial_id=0,
                                             parameters=['tag',
                                                         'attributes'],
                                             selector='lonetag:attributes:'),
                               actors.Text(body='XXX must check each attribute as well',
                                           serial_id=1),
                               actors.Method(body=actors.Expression(text='markup lonetag: tag attributes: []',
                                                                    inner_map={}),
                                             serial_id=2,
                                             parameters=['tag'],
                                             selector='lonetag:'),
                               actors.Method(body=actors.Expression(text='stringguard check: tag.\r\nlistguard check: attributes.\r\nlistguard check: elements.\r\nhtmlstamp stamp: make element',
                                                                    inner_map={'element': L412}),
                                             serial_id=3,
                                             parameters=['tag',
                                                         'attributes',
                                                         'elements'],
                                             selector='tag:attributes:elements:'),
                               actors.Method(body=actors.Expression(text='markup tag: tag attributes: [] elements: elements',
                                                                    inner_map={}),
                                             serial_id=4,
                                             parameters=['tag',
                                                         'elements'],
                                             selector='tag:elements:'),
                               actors.Method(body=actors.Expression(text='if true: (htmlguard passes: object)\r\n   then: make onhtml\r\n   else: (if true: (listguard passes: object)\r\n               then: make onlist\r\n               else: (if true: (stringguard passes: object)\r\n                           then: make onstring\r\n                           else: make onerror))',
                                                                    inner_map={'onerror': L419,
                                                                               'onlist': L420,
                                                                               'onhtml': L421,
                                                                               'onstring': L422}),
                                             serial_id=5,
                                             parameters=['object'],
                                             selector='coerce:')],
                     next_serial_id=6)
L399 = actors.Actor(env=envs.Env(parent=L396),
                    script=L401)
L967 = actors.ActorEditor(editable=True,
                          actor=L399)
L1209 = builtin.List(elements=(builtin.String(str='hello'),))
L1514 = actors.ActorEditor(editable=False,
                           actor=L1209)
L302 = actors.Script(elements=[actors.Method(body=actors.Expression(text='(box get) on: box',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['box'],
                                             selector='on:')],
                     next_serial_id=1)
L300 = actors.Actor(env=envs.Env(parent=L169),
                    script=L302)
L966 = actors.ActorEditor(editable=True,
                          actor=L300)
L939 = builtin.Number(n=25.0)
L1249 = actors.ActorEditor(editable=False,
                           actor=L939)
L786 = builtin.List(elements=())
L785 = actors.ActorEditor(editable=False,
                          actor=L786)
L513 = builtin.Boolean(value=False,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='falsevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L1481 = actors.ActorEditor(editable=False,
                           actor=L513)
L1523 = builtin.Number(n=25.0)
L1697 = actors.ActorEditor(editable=False,
                           actor=L1523)
L594 = envs.Env(parent=None)
L628 = builtin.MailDirectory(env=envs.Env(parent=L594))
L1186 = actors.ActorEditor(editable=False,
                           actor=L628)
L524 = builtin.Number(n=25.0)
L523 = actors.ActorEditor(editable=False,
                          actor=L524)
L1029 = builtin.Number(n=5.0)
L1028 = actors.ActorEditor(editable=False,
                           actor=L1029)
L728 = builtin.Boolean(value=True,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='truevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L1235 = actors.ActorEditor(editable=False,
                           actor=L728)
L599 = builtin.BoxMaker()
L1291 = actors.ActorEditor(editable=False,
                           actor=L599)
L1633 = actors.ActorEditor(editable=True,
                           actor=L346)
L48 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                   inner_map={}),
                                            serial_id=0,
                                            parameters=['message'],
                                            selector='send:')],
                    next_serial_id=1)
L41 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
                                                                   inner_map={}),
                                            serial_id=0,
                                            parameters=[],
                                            selector='first'),
                              actors.Method(body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                   inner_map={}),
                                            serial_id=1,
                                            parameters=[],
                                            selector='removefirst'),
                              actors.Method(body=actors.Expression(text='sender',
                                                                   inner_map={}),
                                            serial_id=2,
                                            parameters=[],
                                            selector='sender')],
                    next_serial_id=3)
L51 = actors.Actor(env=L5,
                   script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                       inner_map={'sender': L48,
                                                                                                  'mailbox': L41}),
                                                                serial_id=0,
                                                                parameters=[],
                                                                selector='run')],
                                        next_serial_id=1))
L976 = actors.ActorEditor(editable=True,
                          actor=L51)
L1654 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1656 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1096 = actors.Script(elements=[],
                      next_serial_id=0)
L1659 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L1096}),
                       serial_id=4)
L1662 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1664 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1666 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1668 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1671 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1674 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1678 = actors.Example(expression=actors.Expression(text='http://localhost:8080/id/5186614581370432354',
                                                    inner_map={}),
                       serial_id=16)
L1680 = actors.Example(expression=actors.Expression(text='8 * 5',
                                                    inner_map={}),
                       serial_id=17)
L1651 = actors.Actor(env=L1076,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1654,
                                                    L1656,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1659,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1662,
                                                    L1664,
                                                    L1666,
                                                    L1668,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1671,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1674,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1678,
                                                    L1680],
                                          next_serial_id=18))
L1650 = actors.ActorEditor(editable=True,
                           actor=L1651)
L247 = builtin.String(str='cat')
L522 = actors.ActorEditor(editable=False,
                          actor=L247)
L349 = builtin.String(str='dog')
L1025 = actors.ActorEditor(editable=False,
                           actor=L349)
L1114 = builtin.MailDirectory(env=envs.Env(parent=L1077))
L1492 = actors.ActorEditor(editable=False,
                           actor=L1114)
L593 = envs.Env(parent=L594)
L891 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                   inner_map={}),
                      serial_id=1)
L894 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                   inner_map={}),
                      serial_id=2)
L627 = actors.Script(elements=[],
                     next_serial_id=0)
L898 = actors.Example(expression=actors.Expression(text='make Foo',
                                                   inner_map={'Foo': L627}),
                      serial_id=4)
L901 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                   inner_map={}),
                      serial_id=6)
L903 = actors.Example(expression=actors.Expression(text='box get',
                                                   inner_map={}),
                      serial_id=7)
L905 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                   inner_map={}),
                      serial_id=8)
L907 = actors.Example(expression=actors.Expression(text="['hello']",
                                                   inner_map={}),
                      serial_id=9)
L912 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                   inner_map={}),
                      serial_id=11)
L915 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                   inner_map={}),
                      serial_id=13)
L919 = actors.Example(expression=actors.Expression(text='http://localhost:8080/id/5292533547202728044',
                                                   inner_map={}),
                      serial_id=16)
L888 = actors.Actor(env=L593,
                    script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                               serial_id=0),
                                                   L891,
                                                   L894,
                                                   actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                               serial_id=3),
                                                   L898,
                                                   actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                               serial_id=5),
                                                   L901,
                                                   L903,
                                                   L905,
                                                   L907,
                                                   actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                               serial_id=10),
                                                   L912,
                                                   actors.Text(body='You can create your own mailbox:',
                                                               serial_id=12),
                                                   L915,
                                                   actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                               serial_id=14),
                                                   actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                               serial_id=15),
                                                   L919],
                                         next_serial_id=17))
L887 = actors.ActorEditor(editable=True,
                          actor=L888)
L600 = builtin.Boolean(value=True,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='truevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L1493 = actors.ActorEditor(editable=False,
                           actor=L600)
L982 = envs.Env(parent=None)
L981 = envs.Env(parent=L982)
L1003 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                     inner_map={}),
                                              serial_id=0,
                                              parameters=['message'],
                                              selector='send:')],
                      next_serial_id=1)
L1006 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
                                                                     inner_map={}),
                                              serial_id=0,
                                              parameters=[],
                                              selector='first'),
                                actors.Method(body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                     inner_map={}),
                                              serial_id=1,
                                              parameters=[],
                                              selector='removefirst'),
                                actors.Method(body=actors.Expression(text='sender',
                                                                     inner_map={}),
                                              serial_id=2,
                                              parameters=[],
                                              selector='sender')],
                      next_serial_id=3)
L999 = actors.Actor(env=L981,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L1003,
                                                                                                   'mailbox': L1006}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L1619 = actors.ActorEditor(editable=True,
                           actor=L999)
L1042 = envs.Env(parent=None)
L1041 = actors.Actor(env=L1042,
                     script=actors.Script(elements=[],
                                          next_serial_id=0))
L1040 = actors.ActorEditor(editable=True,
                           actor=L1041)
L649 = actors.Actor(env=envs.Env(parent=L651),
                    script=L675)
L648 = actors.ActorEditor(editable=True,
                          actor=L649)
L1363 = builtin.String(str='<p/>')
L1362 = actors.ActorEditor(editable=False,
                           actor=L1363)
L370 = envs.Env(parent=L327)
L368 = actors.Actor(env=envs.Env(parent=L370),
                    script=L286)
L1177 = actors.ActorEditor(editable=True,
                           actor=L368)
L122 = envs.Env(parent=L123)
L155 = envs.Env(parent=L122)
L146 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='first'),
                               actors.Method(body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='removefirst'),
                               actors.Method(body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='sender')],
                     next_serial_id=3)
L153 = actors.Actor(env=envs.Env(parent=L155),
                    script=L146)
L1480 = actors.ActorEditor(editable=True,
                           actor=L153)
L969 = builtin.String(str='Is it a dog?')
L968 = actors.ActorEditor(editable=False,
                          actor=L969)
L263 = envs.Env(parent=L170)
L202 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='first'),
                               actors.Method(body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='removefirst'),
                               actors.Method(body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='sender')],
                     next_serial_id=3)
L261 = actors.Actor(env=envs.Env(parent=L263),
                    script=L202)
L1187 = actors.ActorEditor(editable=True,
                           actor=L261)
L63 = builtin.MailDirectory(env=envs.Env(parent=L6))
L1232 = actors.ActorEditor(editable=False,
                           actor=L63)
L425 = actors.Script(elements=[actors.Method(body=actors.Expression(text="markup lonetag: 'p'",
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='p'),
                               actors.Method(body=actors.Expression(text="markup tag: 'blockquote' elements: elements",
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=['elements'],
                                             selector='blockquote:')],
                     next_serial_id=2)
L423 = actors.Actor(env=envs.Env(parent=L396),
                    script=L425)
L1034 = actors.ActorEditor(editable=True,
                           actor=L423)
L1239 = builtin.String(str='Thanks, I will remember.')
L1238 = actors.ActorEditor(editable=False,
                           actor=L1239)
L17 = builtin.BoxMaker()
L1071 = actors.ActorEditor(editable=False,
                           actor=L17)
L507 = builtin.Number(n=5.0)
L506 = actors.ActorEditor(editable=False,
                          actor=L507)
L332 = envs.Env(parent=L279)
L331 = envs.Env(parent=L332)
L1685 = envs.Env(parent=L331)
L1683 = actors.Actor(env=envs.Env(parent=L1685),
                     script=L286)
L1682 = actors.ActorEditor(editable=True,
                           actor=L1683)
L927 = envs.Env(parent=L782)
L925 = actors.Actor(env=envs.Env(parent=L927),
                    script=L321)
L924 = actors.ActorEditor(editable=True,
                          actor=L925)
L131 = builtin.Boolean(value=True,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='trueaction run',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['trueaction',
                                                                                'falseaction'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L975 = actors.ActorEditor(editable=False,
                          actor=L131)
L520 = builtin.Number(n=7.0)
L519 = actors.ActorEditor(editable=False,
                          actor=L520)
L582 = actors.Actor(env=envs.Env(parent=L530),
                    script=L584)
L1030 = actors.ActorEditor(editable=True,
                           actor=L582)
L1263 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1265 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L272 = actors.Script(elements=[],
                     next_serial_id=0)
L1268 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L272}),
                       serial_id=4)
L1271 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1273 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1275 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1277 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1280 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1283 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1287 = actors.Example(expression=actors.Expression(text='make animalgame',
                                                    inner_map={'animalgame': L248}),
                       serial_id=16)
L351 = actors.Example(expression=actors.Expression(text='make call',
                                                   inner_map={'call': L302}),
                      serial_id=0)
L293 = actors.Script(elements=[actors.Method(body=actors.Expression(text='question',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='question'),
                               actors.Method(body=actors.Expression(text='call on: yesbox',
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='yes'),
                               actors.Method(body=actors.Expression(text='call on: nobox',
                                                                    inner_map={}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='no')],
                     next_serial_id=3)
L280 = actors.Script(elements=[actors.Method(body=actors.Expression(text='make askernode\r\n',
                                                                    inner_map={'askernode': L283,
                                                                               'asker': L293}),
                                             serial_id=0,
                                             parameters=['question',
                                                         'yesbox',
                                                         'nobox'],
                                             selector='on:ifyes:ifno:')],
                     next_serial_id=1)
L353 = actors.Example(expression=actors.Expression(text='make makebranch',
                                                   inner_map={'makebranch': L280}),
                      serial_id=1)
L355 = actors.Example(expression=actors.Expression(text='make makeguess',
                                                   inner_map={'makeguess': L307}),
                      serial_id=2)
L357 = actors.Example(expression=actors.Expression(text="let root = box holding: (makeguess for: 'dog')",
                                                   inner_map={}),
                      serial_id=3)
L359 = actors.Example(expression=actors.Expression(text="let root = makebox holding: (makeguess for: 'dog')",
                                                   inner_map={}),
                      serial_id=4)
L361 = actors.Example(expression=actors.Expression(text='call on: root',
                                                   inner_map={}),
                      serial_id=6)
L366 = actors.Example(expression=actors.Expression(text='call on: root',
                                                   inner_map={}),
                      serial_id=7)
L275 = actors.Script(elements=[actors.Method(body=actors.Expression(text='call on: root',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='run')],
                     next_serial_id=1)
L371 = actors.Example(expression=actors.Expression(text='make playgame',
                                                   inner_map={'playgame': L275}),
                      serial_id=8)
L350 = actors.Script(elements=[L351,
                               L353,
                               L355,
                               L357,
                               L359,
                               L361,
                               L366,
                               L371],
                     next_serial_id=9)
L1289 = actors.Example(expression=actors.Expression(text='make newanimalgame',
                                                    inner_map={'newanimalgame': L350}),
                       serial_id=17)
L1260 = actors.Actor(env=L170,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1263,
                                                    L1265,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1268,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1271,
                                                    L1273,
                                                    L1275,
                                                    L1277,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1280,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1283,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1287,
                                                    L1289],
                                          next_serial_id=18))
L1259 = actors.ActorEditor(editable=True,
                           actor=L1260)
L1230 = builtin.Number(n=0.0)
L1229 = actors.ActorEditor(editable=False,
                           actor=L1230)
L1015 = actors.Script(elements=[],
                      next_serial_id=0)
L1013 = actors.Actor(env=envs.Env(parent=L981),
                     script=L1015)
L1142 = actors.ActorEditor(editable=True,
                           actor=L1013)
L18 = builtin.Boolean(value=True,
                      script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                          inner_map={}),
                                                                   serial_id=0,
                                                                   parameters=[],
                                                                   selector='not'),
                                                     actors.Method(body=actors.Expression(text='truevalue',
                                                                                          inner_map={}),
                                                                   serial_id=1,
                                                                   parameters=['truevalue',
                                                                               'falsevalue'],
                                                                   selector='iftrue:iffalse:')],
                                           next_serial_id=2))
L704 = actors.ActorEditor(editable=False,
                          actor=L18)
L223 = actors.Actor(env=L224,
                    script=L225)
L510 = actors.ActorEditor(editable=True,
                          actor=L223)
L642 = builtin.String(str='Wavy!')
L641 = actors.ActorEditor(editable=False,
                          actor=L642)
L1017 = envs.Env(parent=L982)
L1016 = builtin.MailDirectory(env=L1017)
L1699 = actors.ActorEditor(editable=False,
                           actor=L1016)
L1082 = builtin.BoxMaker()
L1254 = actors.ActorEditor(editable=False,
                           actor=L1082)
L625 = actors.Actor(env=envs.Env(parent=L593),
                    script=L627)
L1237 = actors.ActorEditor(editable=True,
                           actor=L625)
L1137 = actors.ActorEditor(editable=True,
                           actor=L240)
L166 = actors.Script(elements=[],
                     next_serial_id=0)
L120 = actors.Actor(env=envs.Env(parent=L122),
                    script=L166)
L119 = actors.ActorEditor(editable=True,
                          actor=L120)
L1094 = actors.Actor(env=envs.Env(parent=L1076),
                     script=L1096)
L1364 = actors.ActorEditor(editable=True,
                           actor=L1094)
L718 = builtin.Boolean(value=False,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='falsevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L739 = builtin.Box(initial_value=L718)
L1367 = actors.ActorEditor(editable=False,
                           actor=L739)
L1020 = builtin.Box(initial_value=builtin.List(elements=()))
L1409 = actors.ActorEditor(editable=False,
                           actor=L1020)
L1083 = builtin.Boolean(value=True,
                        script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                            inner_map={}),
                                                                     serial_id=0,
                                                                     parameters=[],
                                                                     selector='not'),
                                                       actors.Method(body=actors.Expression(text='truevalue',
                                                                                            inner_map={}),
                                                                     serial_id=1,
                                                                     parameters=['truevalue',
                                                                                 'falsevalue'],
                                                                     selector='iftrue:iffalse:')],
                                             next_serial_id=2))
L1122 = actors.ActorEditor(editable=False,
                           actor=L1083)
L143 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L139 = actors.Actor(env=L122,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L143,
                                                                                                   'mailbox': L146}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L521 = actors.ActorEditor(editable=True,
                          actor=L139)
L703 = builtin.BoxMaker()
L702 = actors.ActorEditor(editable=False,
                          actor=L703)
L1582 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1584 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L496 = actors.Script(elements=[],
                     next_serial_id=0)
L1587 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L496}),
                       serial_id=4)
L1590 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1592 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1594 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1596 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1599 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1602 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L447 = actors.Example(expression=actors.Expression(text='let stamppair = makestamp run',
                                                   inner_map={}),
                      serial_id=0)
L450 = actors.Example(expression=actors.Expression(text='let htmlstamp = stamppair at: 1',
                                                   inner_map={}),
                      serial_id=1)
L452 = actors.Example(expression=actors.Expression(text='let htmlguard = stamppair at: 2',
                                                   inner_map={}),
                      serial_id=2)
L454 = actors.Example(expression=actors.Expression(text='make markup',
                                                   inner_map={'markup': L401}),
                      serial_id=4)
L456 = actors.Example(expression=actors.Expression(text='make html',
                                                   inner_map={'html': L425}),
                      serial_id=5)
L436 = actors.Script(elements=[actors.Method(body=actors.Expression(text='name htmlescaped + \'="\' +value htmlescaped + \'"\'',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='show'),
                               actors.Text(body='XXX need to html-escape the strings',
                                           serial_id=1)],
                     next_serial_id=2)
L433 = actors.Script(elements=[actors.Method(body=actors.Expression(text='stringguard check: name.\r\nstringguard check: value.\r\nmake attribute',
                                                                    inner_map={'attribute': L436}),
                                             serial_id=0,
                                             parameters=['name',
                                                         'value'],
                                             selector='name:value:')],
                     next_serial_id=1)
L458 = actors.Example(expression=actors.Expression(text='make makeattr',
                                                   inner_map={'makeattr': L433}),
                      serial_id=8)
L460 = actors.Example(expression=actors.Expression(text='make showattr',
                                                   inner_map={'showattr': L442}),
                      serial_id=9)
L462 = actors.Example(expression=actors.Expression(text='html p show',
                                                   inner_map={}),
                      serial_id=12)
L465 = actors.Example(expression=actors.Expression(text='(html blockquote: []) show',
                                                   inner_map={}),
                      serial_id=14)
L468 = actors.Example(expression=actors.Expression(text='(html blockquote: [html p]) show',
                                                   inner_map={}),
                      serial_id=15)
L471 = actors.Example(expression=actors.Expression(text="(html blockquote: ['hello']) show",
                                                   inner_map={}),
                      serial_id=16)
L446 = actors.Script(elements=[L447,
                               L450,
                               L452,
                               L454,
                               L456,
                               L458,
                               L460,
                               L462,
                               L465,
                               L468,
                               L471],
                     next_serial_id=17)
L1606 = actors.Example(expression=actors.Expression(text='make htmlmodule',
                                                    inner_map={'htmlmodule': L446}),
                       serial_id=25)
L1579 = actors.Actor(env=L377,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1582,
                                                    L1584,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1587,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1590,
                                                    L1592,
                                                    L1594,
                                                    L1596,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1599,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1602,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1606],
                                          next_serial_id=26))
L1578 = actors.ActorEditor(editable=True,
                           actor=L1579)
L33 = builtin.Box(initial_value=builtin.List(elements=(L35,)))
L1178 = actors.ActorEditor(editable=False,
                           actor=L33)
L787 = actors.ActorEditor(editable=False,
                          actor=L398)
L893 = builtin.Number(n=5.0)
L1241 = actors.ActorEditor(editable=False,
                           actor=L893)
L1692 = builtin.String(str='Is it a dog?')
L1691 = actors.ActorEditor(editable=False,
                           actor=L1692)
L502 = builtin.Box(initial_value=builtin.List(elements=()))
L501 = actors.ActorEditor(editable=False,
                          actor=L502)
L512 = builtin.Box(initial_value=L513)
L511 = actors.ActorEditor(editable=False,
                          actor=L512)
L183 = builtin.Boolean(value=True,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='truevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L1642 = actors.ActorEditor(editable=False,
                           actor=L183)
L543 = builtin.Boolean(value=True,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='truevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L1366 = actors.ActorEditor(editable=False,
                           actor=L543)
L1549 = envs.Env(parent=None)
L1548 = actors.Actor(env=L1549,
                     script=actors.Script(elements=[],
                                          next_serial_id=0))
L1612 = actors.ActorEditor(editable=True,
                           actor=L1548)
L114 = builtin.Number(n=25.0)
L113 = actors.ActorEditor(editable=False,
                          actor=L114)
L987 = builtin.BoxMaker()
L1611 = actors.ActorEditor(editable=False,
                           actor=L987)
L1147 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1149 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1153 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L1015}),
                       serial_id=4)
L1156 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1158 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1160 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1162 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1167 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1170 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1175 = actors.Example(expression=actors.Expression(text="maildirectory at: 'alice' put: mailbox sender",
                                                    inner_map={}),
                       serial_id=17)
L1144 = actors.Actor(env=L981,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1147,
                                                    L1149,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1153,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1156,
                                                    L1158,
                                                    L1160,
                                                    L1162,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1167,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1170,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    actors.Text(body="maildirectory at: 'alice' put: mailbox sender",
                                                                serial_id=16),
                                                    L1175],
                                          next_serial_id=18))
L1143 = actors.ActorEditor(editable=True,
                           actor=L1144)
L592 = envs.Env(parent=L593)
L618 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='first'),
                               actors.Method(body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='removefirst'),
                               actors.Method(body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='sender')],
                     next_serial_id=3)
L590 = actors.Actor(env=envs.Env(parent=L592),
                    script=L618)
L589 = actors.ActorEditor(editable=True,
                          actor=L590)
L104 = builtin.Number(n=10)
L1119 = actors.ActorEditor(editable=False,
                           actor=L104)
L1102 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                     inner_map={}),
                                              serial_id=0,
                                              parameters=['message'],
                                              selector='send:')],
                      next_serial_id=1)
L1075 = actors.Actor(env=L1076,
                     script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                         inner_map={'sender': L1102,
                                                                                                    'mailbox': L1107}),
                                                                  serial_id=0,
                                                                  parameters=[],
                                                                  selector='run')],
                                          next_serial_id=1))
L1074 = actors.ActorEditor(editable=True,
                           actor=L1075)
L778 = builtin.List(elements=(builtin.String(str='hello'),))
L777 = actors.ActorEditor(editable=False,
                          actor=L778)
L477 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L480 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='first'),
                               actors.Method(body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='removefirst'),
                               actors.Method(body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='sender')],
                     next_serial_id=3)
L473 = actors.Actor(env=L377,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L477,
                                                                                                   'mailbox': L480}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L1631 = actors.ActorEditor(editable=True,
                           actor=L473)
L754 = actors.Actor(env=envs.Env(parent=L716),
                    script=L756)
L760 = actors.ActorEditor(editable=True,
                          actor=L754)
L988 = builtin.Boolean(value=True,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='truevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L1255 = actors.ActorEditor(editable=False,
                           actor=L988)
L7 = builtin.Boolean(value=False,
                     script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                         inner_map={}),
                                                                  serial_id=0,
                                                                  parameters=[],
                                                                  selector='not'),
                                                    actors.Method(body=actors.Expression(text='falsevalue',
                                                                                         inner_map={}),
                                                                  serial_id=1,
                                                                  parameters=['truevalue',
                                                                              'falsevalue'],
                                                                  selector='iftrue:iffalse:')],
                                          next_serial_id=2))
L1491 = actors.ActorEditor(editable=False,
                           actor=L7)
L805 = builtin.Boolean(value=True,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='trueaction run',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['trueaction',
                                                                                'falseaction'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L1686 = actors.ActorEditor(editable=False,
                           actor=L805)
L664 = builtin.BoxMaker()
L1248 = actors.ActorEditor(editable=False,
                           actor=L664)
L72 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                  inner_map={}),
                     serial_id=1)
L75 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                  inner_map={}),
                     serial_id=2)
L79 = actors.Example(expression=actors.Expression(text='make Foo',
                                                  inner_map={'Foo': L67}),
                     serial_id=4)
L82 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                  inner_map={}),
                     serial_id=6)
L84 = actors.Example(expression=actors.Expression(text='box get',
                                                  inner_map={}),
                     serial_id=7)
L86 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                  inner_map={}),
                     serial_id=8)
L88 = actors.Example(expression=actors.Expression(text="['hello']",
                                                  inner_map={}),
                     serial_id=9)
L93 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                  inner_map={}),
                     serial_id=11)
L96 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                  inner_map={}),
                     serial_id=13)
L100 = actors.Example(expression=actors.Expression(text="'hello alex' size",
                                                   inner_map={}),
                      serial_id=16)
L102 = actors.Example(expression=actors.Expression(text="'hello alex' length",
                                                   inner_map={}),
                      serial_id=17)
L105 = actors.Example(expression=actors.Expression(text='let sender = mailbox sender',
                                                   inner_map={}),
                      serial_id=18)
L107 = actors.Example(expression=actors.Expression(text='sender send: make message',
                                                   inner_map={'message': L37}),
                      serial_id=19)
L60 = actors.Script(elements=[actors.Method(body=actors.Expression(text='votesformcdonalds <- (votesformcdonalds get + 1)',
                                                                   inner_map={}),
                                            serial_id=0,
                                            parameters=[],
                                            selector='votemcdonalds')],
                    next_serial_id=1)
L57 = actors.Script(elements=[actors.Method(body=actors.Expression(text='let votesformcdonalds = makebox holding: 0.\r\nmake ballot',
                                                                   inner_map={'ballot': L60}),
                                            serial_id=0,
                                            parameters=[],
                                            selector='run')],
                    next_serial_id=1)
L111 = actors.Example(expression=actors.Expression(text='make makeballot',
                                                   inner_map={'makeballot': L57}),
                      serial_id=20)
L4 = actors.Actor(env=L5,
                  script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                             serial_id=0),
                                                 L72,
                                                 L75,
                                                 actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                             serial_id=3),
                                                 L79,
                                                 actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                             serial_id=5),
                                                 L82,
                                                 L84,
                                                 L86,
                                                 L88,
                                                 actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                             serial_id=10),
                                                 L93,
                                                 actors.Text(body='You can create your own mailbox:',
                                                             serial_id=12),
                                                 L96,
                                                 actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                             serial_id=14),
                                                 actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                             serial_id=15),
                                                 L100,
                                                 L102,
                                                 L105,
                                                 L107,
                                                 L111],
                                       next_serial_id=21))
L3 = actors.ActorEditor(editable=True,
                        actor=L4)
L1257 = builtin.Number(n=6.0)
L1256 = actors.ActorEditor(editable=False,
                           actor=L1257)
L811 = builtin.StampMaker()
L1127 = actors.ActorEditor(editable=False,
                           actor=L811)
L330 = actors.Actor(env=L331,
                    script=L283)
L329 = builtin.Box(initial_value=L330)
L1227 = actors.ActorEditor(editable=False,
                           actor=L329)
L1184 = builtin.String(str='Is it a dog?')
L1183 = actors.ActorEditor(editable=False,
                           actor=L1184)
L699 = actors.Script(elements=[],
                     next_serial_id=0)
L697 = actors.Actor(env=envs.Env(parent=L652),
                    script=L699)
L1035 = actors.ActorEditor(editable=True,
                           actor=L697)
L1380 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1382 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1385 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L699}),
                       serial_id=4)
L1388 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1390 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1392 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1394 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1399 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1402 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L692 = actors.Script(elements=[],
                     next_serial_id=0)
L1406 = actors.Example(expression=actors.Expression(text='mailbox sender send: make message',
                                                    inner_map={'message': L692}),
                       serial_id=16)
L1377 = actors.Actor(env=L652,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1380,
                                                    L1382,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1385,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1388,
                                                    L1390,
                                                    L1392,
                                                    L1394,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1399,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1402,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1406],
                                          next_serial_id=17))
L1376 = actors.ActorEditor(editable=True,
                           actor=L1377)
L492 = actors.StampedActor(stamp=L490,
                           actor=builtin.String(str='hello'))
L973 = actors.ActorEditor(editable=False,
                          actor=L492)
L29 = builtin.Box(initial_value=L7)
L1577 = actors.ActorEditor(editable=False,
                           actor=L29)
L980 = envs.Env(parent=L981)
L1018 = actors.Actor(env=envs.Env(parent=L980),
                     script=L1003)
L1233 = actors.ActorEditor(editable=True,
                           actor=L1018)
L759 = builtin.Number(n=120.0)
L974 = actors.ActorEditor(editable=False,
                          actor=L759)
L213 = actors.Script(elements=[actors.Method(body=actors.Expression(text='make yesnoquestion\r\n',
                                                                    inner_map={'yesnoquestion': L216}),
                                             serial_id=2,
                                             parameters=['query',
                                                         'onyes',
                                                         'onno'],
                                             selector='asking:ifyes:ifno:')],
                     next_serial_id=3)
L211 = actors.Actor(env=L212,
                    script=L213)
L1032 = actors.ActorEditor(editable=True,
                           actor=L211)
L273 = actors.Actor(env=envs.Env(parent=L169),
                    script=L275)
L1228 = actors.ActorEditor(editable=True,
                           actor=L273)
L635 = builtin.Boolean(value=True,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='truevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L634 = actors.ActorEditor(editable=False,
                          actor=L635)
L258 = envs.Env(parent=L224)
L257 = envs.Env(parent=L258)
L646 = envs.Env(parent=L257)
L644 = actors.Actor(env=envs.Env(parent=L646),
                    script=L235)
L643 = actors.ActorEditor(editable=True,
                          actor=L644)
L1636 = actors.ActorEditor(editable=False,
                           actor=L491)
L1626 = builtin.String(str='Is it a dog?')
L1625 = actors.ActorEditor(editable=False,
                           actor=L1626)
L1621 = builtin.String(str='Is it a dog?')
L1620 = actors.ActorEditor(editable=False,
                           actor=L1621)
L168 = actors.Actor(env=L169,
                    script=L350)
L167 = actors.ActorEditor(editable=True,
                          actor=L168)
L1180 = builtin.String(str='Is it a cat?')
L1179 = actors.ActorEditor(editable=False,
                           actor=L1180)
L1293 = builtin.Box(initial_value=L1124)
L1292 = actors.ActorEditor(editable=False,
                           actor=L1293)
L1139 = builtin.List(elements=(builtin.String(str='hello'),))
L1138 = actors.ActorEditor(editable=False,
                           actor=L1139)
L55 = actors.Actor(env=envs.Env(parent=L5),
                   script=L57)
L929 = actors.ActorEditor(editable=True,
                          actor=L55)
L1372 = envs.Env(parent=L257)
L1370 = actors.Actor(env=envs.Env(parent=L1372),
                     script=L235)
L1369 = actors.ActorEditor(editable=True,
                           actor=L1370)
L740 = actors.Actor(env=L716,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L744,
                                                                                                   'mailbox': L747}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L962 = actors.ActorEditor(editable=True,
                          actor=L740)
L832 = builtin.MailDirectory(env=envs.Env(parent=L804))
L1616 = actors.ActorEditor(editable=False,
                           actor=L832)
L156 = actors.Actor(env=envs.Env(parent=L155),
                    script=L143)
L1240 = actors.ActorEditor(editable=True,
                           actor=L156)
L340 = actors.Actor(env=L341,
                    script=L311)
L1135 = actors.ActorEditor(editable=True,
                           actor=L340)
L1483 = builtin.Number(n=0)
L1482 = actors.ActorEditor(editable=False,
                           actor=L1483)
L1408 = actors.ActorEditor(editable=False,
                           actor=L490)
L487 = builtin.MailDirectory(env=envs.Env(parent=L378))
L1141 = actors.ActorEditor(editable=False,
                           actor=L487)
L812 = builtin.BoxMaker()
L1574 = actors.ActorEditor(editable=False,
                           actor=L812)
L74 = builtin.Number(n=5.0)
L1059 = actors.ActorEditor(editable=False,
                           actor=L74)
L376 = envs.Env(parent=L377)
L374 = actors.Actor(env=envs.Env(parent=L376),
                    script=L480)
L373 = actors.ActorEditor(editable=True,
                          actor=L374)
L1246 = builtin.Number(n=5.0)
L1245 = actors.ActorEditor(editable=False,
                           actor=L1246)
L199 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L195 = actors.Actor(env=L170,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L199,
                                                                                                   'mailbox': L202}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L1242 = actors.ActorEditor(editable=True,
                           actor=L195)
L1498 = envs.Env(parent=None)
L1497 = actors.Actor(env=L1498,
                     script=actors.Script(elements=[],
                                          next_serial_id=0))
L1496 = actors.ActorEditor(editable=True,
                           actor=L1497)
L788 = actors.ActorEditor(editable=False,
                          actor=L789)
L395 = actors.Actor(env=L396,
                    script=L446)
L449 = actors.ActorEditor(editable=True,
                          actor=L395)
L379 = builtin.Boolean(value=True,
                       script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0,
                                                                    parameters=[],
                                                                    selector='not'),
                                                      actors.Method(body=actors.Expression(text='trueaction run',
                                                                                           inner_map={}),
                                                                    serial_id=1,
                                                                    parameters=['trueaction',
                                                                                'falseaction'],
                                                                    selector='iftrue:iffalse:')],
                                            next_serial_id=2))
L1573 = actors.ActorEditor(editable=False,
                           actor=L379)
L529 = envs.Env(parent=L530)
L562 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='first'),
                               actors.Method(body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='removefirst'),
                               actors.Method(body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='sender')],
                     next_serial_id=3)
L527 = actors.Actor(env=envs.Env(parent=L529),
                    script=L562)
L526 = actors.ActorEditor(editable=True,
                          actor=L527)
L559 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L555 = actors.Actor(env=L530,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L559,
                                                                                                   'mailbox': L562}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L1064 = actors.ActorEditor(editable=True,
                           actor=L555)
L494 = actors.Actor(env=envs.Env(parent=L377),
                    script=L496)
L1133 = actors.ActorEditor(editable=True,
                           actor=L494)
L270 = actors.Actor(env=envs.Env(parent=L170),
                    script=L272)
L1375 = actors.ActorEditor(editable=True,
                           actor=L270)
L1068 = builtin.List(elements=(builtin.String(str='hello'),))
L1067 = actors.ActorEditor(editable=False,
                           actor=L1068)
L761 = builtin.MailDirectory(env=envs.Env(parent=L717))
L1690 = actors.ActorEditor(editable=False,
                           actor=L761)
L1572 = actors.ActorEditor(editable=False,
                           actor=L172)
L363 = actors.Actor(env=L364,
                    script=L314)
L1136 = actors.ActorEditor(editable=True,
                           actor=L363)
L343 = builtin.String(str='cat')
L1226 = actors.ActorEditor(editable=False,
                           actor=L343)
L470 = builtin.String(str='<blockquote> <p></blockquote>')
L1490 = actors.ActorEditor(editable=False,
                           actor=L470)
L430 = builtin.List(elements=(L398,
                              L397))
L1629 = actors.ActorEditor(editable=False,
                           actor=L430)
L164 = actors.Script(elements=[actors.Text(body='Hi me, how are me?\r\n',
                                           serial_id=0)],
                     next_serial_id=1)
L162 = actors.Actor(env=envs.Env(parent=L122),
                    script=L164)
L784 = actors.ActorEditor(editable=True,
                          actor=L162)
L978 = actors.Actor(env=envs.Env(parent=L980),
                    script=L1006)
L977 = actors.ActorEditor(editable=True,
                          actor=L978)
L936 = builtin.Number(n=5.0)
L1181 = actors.ActorEditor(editable=False,
                           actor=L936)
L431 = actors.Actor(env=envs.Env(parent=L396),
                    script=L433)
L1608 = actors.ActorEditor(editable=True,
                           actor=L431)
L615 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L611 = actors.Actor(env=L593,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L615,
                                                                                                   'mailbox': L618}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L705 = actors.ActorEditor(editable=True,
                          actor=L611)
L32 = envs.Env(parent=L5)
L39 = actors.Actor(env=envs.Env(parent=L32),
                   script=L41)
L1062 = actors.ActorEditor(editable=True,
                           actor=L39)
L896 = builtin.Number(n=25.0)
L963 = actors.ActorEditor(editable=False,
                          actor=L896)
L393 = builtin.TypeGuard(sample_instance=())
L1061 = actors.ActorEditor(editable=False,
                           actor=L393)
L1486 = builtin.String(str='hello world!hello world!')
L1485 = actors.ActorEditor(editable=False,
                           actor=L1486)
L256 = actors.Actor(env=L257,
                    script=L228)
L1630 = actors.ActorEditor(editable=True,
                           actor=L256)
L1519 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1521 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1525 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L166}),
                       serial_id=4)
L1528 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1530 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1532 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1534 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1537 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1540 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1544 = actors.Example(expression=actors.Expression(text='let tome = mailbox sender',
                                                    inner_map={}),
                       serial_id=16)
L1546 = actors.Example(expression=actors.Expression(text='tome send: make message',
                                                    inner_map={'message': L164}),
                       serial_id=17)
L1565 = actors.Example(expression=actors.Expression(text='2 * 3',
                                                    inner_map={}),
                       serial_id=18)
L1568 = actors.Example(expression=actors.Expression(text='2 / 0',
                                                    inner_map={}),
                       serial_id=19)
L1570 = actors.Example(expression=actors.Expression(text='let pair = makestamp run',
                                                    inner_map={}),
                       serial_id=20)
L1516 = actors.Actor(env=L122,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1519,
                                                    L1521,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1525,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1528,
                                                    L1530,
                                                    L1532,
                                                    L1534,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1537,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1540,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1544,
                                                    L1546,
                                                    L1565,
                                                    L1568,
                                                    L1570],
                                          next_serial_id=21))
L1515 = actors.ActorEditor(editable=True,
                           actor=L1516)
L116 = builtin.String(str='Thanks, I will remember.')
L115 = actors.ActorEditor(editable=False,
                          actor=L116)
L278 = actors.Actor(env=L279,
                    script=L280)
L1126 = actors.ActorEditor(editable=True,
                           actor=L278)
L922 = builtin.List(elements=(builtin.String(str='hello'),))
L921 = actors.ActorEditor(editable=False,
                          actor=L922)
L30 = actors.Actor(env=envs.Env(parent=L32),
                   script=L48)
L1641 = actors.ActorEditor(editable=True,
                           actor=L30)
L819 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L815 = actors.Actor(env=L803,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L819,
                                                                                                   'mailbox': L822}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L1070 = actors.ActorEditor(editable=True,
                           actor=L815)
L338 = builtin.String(str='Is it easily frightened?')
L1073 = actors.ActorEditor(editable=False,
                           actor=L338)
L1225 = actors.ActorEditor(editable=False,
                           actor=L532)
L1164 = builtin.List(elements=(builtin.String(str='hello'),))
L1698 = actors.ActorEditor(editable=False,
                           actor=L1164)
L344 = builtin.String(str='Does it meow?')
L1026 = actors.ActorEditor(editable=False,
                           actor=L344)
L1696 = envs.Env(parent=L347)
L1694 = actors.Actor(env=envs.Env(parent=L1696),
                     script=L314)
L1693 = actors.ActorEditor(editable=True,
                           actor=L1694)
L855 = builtin.Number(n=5.0)
L1610 = actors.ActorEditor(editable=False,
                           actor=L855)
L1038 = builtin.String(str='OK!')
L1037 = actors.ActorEditor(editable=False,
                           actor=L1038)
L138 = builtin.Box(initial_value=L124)
L928 = actors.ActorEditor(editable=False,
                          actor=L138)
L1194 = builtin.Number(n=5.0)
L1689 = actors.ActorEditor(editable=False,
                           actor=L1194)
L706 = actors.ActorEditor(editable=False,
                          actor=L707)
L467 = builtin.String(str='<blockquote></blockquote>')
L1182 = actors.ActorEditor(editable=False,
                           actor=L467)
L1615 = actors.ActorEditor(editable=False,
                           actor=L718)
L0 = registry.HmphSystem(editor_of_actor={L843: L842,
                                          L386: L1125,
                                          L492: L973,
                                          L124: L1479,
                                          L346: L1633,
                                          L2: L1,
                                          L931: L930,
                                          L635: L634,
                                          L464: L1258,
                                          L713: L712,
                                          L30: L1641,
                                          L1692: L1691,
                                          L700: L1484,
                                          L1624: L1623,
                                          L1644: L1643,
                                          L881: L880,
                                          L1614: L1613,
                                          L1139: L1138,
                                          L829: L1134,
                                          L1189: L1188,
                                          L1129: L1128,
                                          L345: L960,
                                          L374: L373,
                                          L812: L1574,
                                          L839: L838,
                                          L1579: L1578,
                                          L770: L769,
                                          L268: L1027,
                                          L90: L1063,
                                          L505: L504,
                                          L1097: L1634,
                                          L344: L1026,
                                          L532: L1225,
                                          L781: L780,
                                          L709: L708,
                                          L74: L1059,
                                          L649: L648,
                                          L695: L1033,
                                          L805: L1686,
                                          L397: L1243,
                                          L909: L1036,
                                          L109: L1031,
                                          L487: L1141,
                                          L489: L508,
                                          L118: L117,
                                          L35: L1236,
                                          L1151: L1231,
                                          L423: L1034,
                                          L130: L525,
                                          L4: L3,
                                          L491: L1636,
                                          L763: L1635,
                                          L1023: L1022,
                                          L759: L974,
                                          L1688: L1687,
                                          L1370: L1369,
                                          L611: L705,
                                          L343: L1226,
                                          L77: L1365,
                                          L1640: L1639,
                                          L325: L1627,
                                          L850: L849,
                                          L512: L511,
                                          L978: L977,
                                          L194: L961,
                                          L778: L777,
                                          L1124: L1123,
                                          L399: L967,
                                          L1209: L1514,
                                          L642: L641,
                                          L811: L1127,
                                          L243: L1489,
                                          L513: L1481,
                                          L1523: L1697,
                                          L628: L1186,
                                          L524: L523,
                                          L1029: L1028,
                                          L922: L921,
                                          L644: L643,
                                          L599: L1291,
                                          L670: L1632,
                                          L1651: L1650,
                                          L1648: L1647,
                                          L771: L1617,
                                          L1412: L1411,
                                          L600: L1493,
                                          L999: L1619,
                                          L1131: L1130,
                                          L440: L1628,
                                          L1363: L1362,
                                          L368: L1177,
                                          L55: L929,
                                          L153: L1480,
                                          L1018: L1233,
                                          L969: L968,
                                          L590: L589,
                                          L1230: L1229,
                                          L158: L1368,
                                          L542: L1234,
                                          L936: L1181,
                                          L1121: L1120,
                                          L1239: L1238,
                                          L17: L1071,
                                          L261: L1187,
                                          L363: L1136,
                                          L470: L1490,
                                          L554: L1247,
                                          L1567: L1637,
                                          L65: L1060,
                                          L1260: L1259,
                                          L182: L1638,
                                          L1013: L1142,
                                          L18: L704,
                                          L223: L510,
                                          L888: L887,
                                          L1016: L1699,
                                          L1082: L1254,
                                          L1396: L1609,
                                          L240: L1137,
                                          L1066: L1065,
                                          L273: L1228,
                                          L120: L119,
                                          L398: L787,
                                          L654: L1039,
                                          L305: L1618,
                                          L1144: L1143,
                                          L278: L1126,
                                          L33: L1178,
                                          L1488: L1487,
                                          L893: L1241,
                                          L1083: L1122,
                                          L796: L795,
                                          L520: L519,
                                          L543: L1366,
                                          L1548: L1612,
                                          L114: L113,
                                          L51: L976,
                                          L494: L1133,
                                          L671: L1495,
                                          L1041: L1040,
                                          L1180: L1179,
                                          L104: L1119,
                                          L1075: L1074,
                                          L395: L449,
                                          L209: L251,
                                          L473: L1631,
                                          L939: L1249,
                                          L988: L1255,
                                          L7: L1491,
                                          L393: L1061,
                                          L815: L1070,
                                          L965: L964,
                                          L1257: L1256,
                                          L392: L509,
                                          L555: L1064,
                                          L1020: L1409,
                                          L740: L962,
                                          L63: L1232,
                                          L697: L1035,
                                          L896: L963,
                                          L1377: L1376,
                                          L814: L1072,
                                          L1483: L1482,
                                          L625: L1237,
                                          L1094: L1364,
                                          L971: L970,
                                          L394: L1185,
                                          L1576: L1575,
                                          L703: L702,
                                          L349: L1025,
                                          L1626: L1625,
                                          L1621: L1620,
                                          L244: L1410,
                                          L1114: L1492,
                                          L168: L167,
                                          L1293: L1292,
                                          L385: L1244,
                                          L131: L975,
                                          L786: L785,
                                          L183: L1642,
                                          L329: L1227,
                                          L832: L1616,
                                          L116: L115,
                                          L340: L1135,
                                          L754: L760,
                                          L855: L1610,
                                          L582: L1030,
                                          L138: L928,
                                          L739: L1367,
                                          L502: L501,
                                          L300: L966,
                                          L728: L1235,
                                          L1246: L1245,
                                          L195: L1242,
                                          L1497: L1496,
                                          L765: L1494,
                                          L569: L972,
                                          L379: L1573,
                                          L768: L767,
                                          L1683: L1682,
                                          L664: L1248,
                                          L789: L788,
                                          L270: L1375,
                                          L1038: L1037,
                                          L1068: L1067,
                                          L761: L1690,
                                          L172: L1572,
                                          L1184: L1183,
                                          L29: L1577,
                                          L430: L1629,
                                          L574: L1649,
                                          L925: L924,
                                          L211: L1032,
                                          L431: L1608,
                                          L239: L647,
                                          L39: L1062,
                                          L139: L521,
                                          L1251: L1250,
                                          L507: L506,
                                          L527: L526,
                                          L1516: L1515,
                                          L156: L1240,
                                          L490: L1408,
                                          L1486: L1485,
                                          L1295: L1294,
                                          L338: L1073,
                                          L987: L1611,
                                          L1164: L1698,
                                          L162: L784,
                                          L1374: L1373,
                                          L1694: L1693,
                                          L247: L522,
                                          L685: L1622,
                                          L800: L799,
                                          L160: L798,
                                          L1194: L1689,
                                          L707: L706,
                                          L256: L1630,
                                          L467: L1182,
                                          L718: L1615},
                         accounts=['4227047065147840205',
                                   '8511836882149982016',
                                   '15354271914547105265',
                                   '5292533547202728044',
                                   '16495268673511082035',
                                   'CCDF40493E712274L',
                                   '987ba6d80c536ef72fd3',
                                   '4edd14e178ad0c694a5f',
                                   '959c6923ca073aa23ec2',
                                   '84af1be6f390fc4f0d92',
                                   '7aa131ceb0eae191a3ed',
                                   '740e543a73fba8ae453f',
                                   '6737ab2d99858d2cb98e'],
                         at_id={'3852696174487011421': registry.Entry(timestamp=1104697525.0871,
                                                                      actor=L787),
                                '479cbf4440b2fda712e3': registry.Entry(timestamp=1108956215.9968741,
                                                                       actor=L704),
                                '389f782794ad82bf42c2': registry.Entry(timestamp=1109435020.479353,
                                                                       actor=L1179),
                                '50c6025c3f7c1b17b359': registry.Entry(timestamp=1190664334.063704,
                                                                       actor=L880),
                                '92077dd35d38c54b1d7a': registry.Entry(timestamp=1109433506.8028109,
                                                                       actor=L302),
                                'e0a19b1b2095e54a1a98': registry.Entry(timestamp=1109428828.339134,
                                                                       actor=L240),
                                '563ca179481499c18ab6': registry.Entry(timestamp=1109435048.1022961,
                                                                       actor=L116),
                                '177af5534bd8e4a0efef': registry.Entry(timestamp=1109434948.9887691,
                                                                       actor=L1638),
                                '33e43cb0a69702868a1b': registry.Entry(timestamp=1109435117.5115161,
                                                                       actor=L1693),
                                'a9dd87deafb6771dc685': registry.Entry(timestamp=1109433538.641732,
                                                                       actor=L194),
                                '661509098043722411': registry.Entry(timestamp=1104650549.6519859,
                                                                     actor=L1574),
                                '9e4059674b42ebb77e80': registry.Entry(timestamp=1190664333.9055829,
                                                                       actor=L1144),
                                '2452790028842326399': registry.Entry(timestamp=1104650712.6615851,
                                                                      actor=L509),
                                '244593790248987534': registry.Entry(timestamp=1104696067.7436399,
                                                                     actor=L1608),
                                '7733755804024661725': registry.Entry(timestamp=1104730507.793503,
                                                                      actor=L1096),
                                'd3f069172de864d5ed94': registry.Entry(timestamp=1105921788.5114219,
                                                                       actor=L1234),
                                '585cf6e821add948341f': registry.Entry(timestamp=1108956454.2687061,
                                                                       actor=L1257),
                                '9923278975221135661': registry.Entry(timestamp=1104650760.2987189,
                                                                      actor=L1636),
                                '3313777953666434324': registry.Entry(timestamp=1104650549.6397591,
                                                                      actor=L113),
                                '701718880621245410': registry.Entry(timestamp=1104689955.3227019,
                                                                     actor=L401),
                                '2169573376375311512': registry.Entry(timestamp=1104732128.235605,
                                                                      actor=L519),
                                '425401d16cbbcb013414': registry.Entry(timestamp=1109424299.651423,
                                                                       actor=L1),
                                '7488614337481629366': registry.Entry(timestamp=1104732124.7329731,
                                                                      actor=L1647),
                                'b02f708094d7017ff9ca': registry.Entry(timestamp=1109428831.4527409,
                                                                       actor=L243),
                                '4716280173295595176': registry.Entry(timestamp=1104632228.340987,
                                                                      actor=L1697),
                                '6ea8e4e7c59015808866': registry.Entry(timestamp=1108956215.9937069,
                                                                       actor=L1577),
                                '809ca9a6a52e472c2232': registry.Entry(timestamp=1108956539.881407,
                                                                       actor=L1373),
                                '2fe08bfff563b4be7b88': registry.Entry(timestamp=1109428875.280458,
                                                                       actor=L1620),
                                '14f6bb412e4e8dba28e7': registry.Entry(timestamp=1105921513.4537351,
                                                                       actor=L523),
                                '752780470375236548': registry.Entry(timestamp=1104650712.6552,
                                                                     actor=L1133),
                                'bd70c7c47be23dba293f': registry.Entry(timestamp=1109433735.9576671,
                                                                       actor=L305),
                                '86494131c70f31e05c76': registry.Entry(timestamp=1105921566.047498,
                                                                       actor=L1030),
                                '95e56b4ad9bd4778155e': registry.Entry(timestamp=1109435020.4820459,
                                                                       actor=L1180),
                                'aeca121725efb320e1bd': registry.Entry(timestamp=1109435097.3057289,
                                                                       actor=L1643),
                                '10397032148789093459': registry.Entry(timestamp=1104732128.235873,
                                                                       actor=L520),
                                '6ad807ecfa9819fc5274': registry.Entry(timestamp=1108956554.296838,
                                                                       actor=L1060),
                                '27a3eaafc2929449c2': registry.Entry(timestamp=1108412240.3505909,
                                                                     actor=L1130),
                                'f6599863150eeb0c6b2c': registry.Entry(timestamp=1109434795.847883,
                                                                       actor=L363),
                                '7773452571940476712': registry.Entry(timestamp=1104697525.0874059,
                                                                      actor=L398),
                                '8260809509679861109': registry.Entry(timestamp=1104633042.4136021,
                                                                      actor=L1240),
                                '13289750248154104862': registry.Entry(timestamp=1104730109.325695,
                                                                       actor=L1481),
                                '9876815513572400324': registry.Entry(timestamp=1104650549.6620231,
                                                                      actor=L795),
                                '4023b3c507c036f50e56': registry.Entry(timestamp=1104797071.70976,
                                                                       actor=L1181),
                                '4c09de69dcaeb7cc983c': registry.Entry(timestamp=1109428388.68279,
                                                                       actor=L647),
                                'afe0f8475c226480003e': registry.Entry(timestamp=1104797063.4905939,
                                                                       actor=L1690),
                                '14572783785176608328': registry.Entry(timestamp=1104632228.3476341,
                                                                       actor=L975),
                                '2af0a890ec67be538d2e': registry.Entry(timestamp=1190664333.9233689,
                                                                       actor=L1231),
                                '3bc09d4543e10c13c0fd': registry.Entry(timestamp=1109435162.498421,
                                                                       actor=L344),
                                '744cd5a5607fb52901e3': registry.Entry(timestamp=1190665257.4724829,
                                                                       actor=L1233),
                                'dfdddcc9276b298ffa66': registry.Entry(timestamp=1108412173.816499,
                                                                       actor=L1484),
                                '3221c3e44d26b6bbd5ad': registry.Entry(timestamp=1105921540.943424,
                                                                       actor=L1194),
                                'e64afe24df26d799a9ac': registry.Entry(timestamp=1104807972.488673,
                                                                       actor=L754),
                                '17543361990980566375': registry.Entry(timestamp=1104650712.6712439,
                                                                       actor=L777),
                                'aa59537f559184f9eca2': registry.Entry(timestamp=1104797063.503005,
                                                                       actor=L962),
                                '15235668337536127643': registry.Entry(timestamp=1104650549.6492591,
                                                                       actor=L1072),
                                '506e223cff60b5489e1b': registry.Entry(timestamp=1109435078.919728,
                                                                       actor=L275),
                                'bd4007d9b81ff6015fa': registry.Entry(timestamp=1109677352.059732,
                                                                      actor=L1228),
                                '66e67041b7181b22690': registry.Entry(timestamp=1104797063.3189459,
                                                                      actor=L756),
                                '9f783033e4c251e7aecd': registry.Entry(timestamp=1109435120.1054151,
                                                                       actor=L969),
                                '1823737881735097641': registry.Entry(timestamp=1104633108.6909039,
                                                                      actor=L1496),
                                'd12f22d62909bfa38926': registry.Entry(timestamp=1190664334.0435531,
                                                                       actor=L1142),
                                '6231133fb36d5570d27a': registry.Entry(timestamp=1109434995.1101241,
                                                                       actor=L1238),
                                '2291036927185731541': registry.Entry(timestamp=1104650712.656209,
                                                                      actor=L496),
                                '16832713526910606204': registry.Entry(timestamp=1104732473.8273611,
                                                                       actor=L1687),
                                '5f250d31a4b5ac2e53cb': registry.Entry(timestamp=1109435010.016041,
                                                                       actor=L960),
                                '10238622742572975996': registry.Entry(timestamp=1104696935.0587831,
                                                                       actor=L404),
                                'feab0d101efa1eb7800c': registry.Entry(timestamp=1105921822.377749,
                                                                       actor=L1023),
                                '6368b3eb10785a7e39c3': registry.Entry(timestamp=1104797063.330265,
                                                                       actor=L1235),
                                '8635995105440979424': registry.Entry(timestamp=1104650712.6806979,
                                                                      actor=L373),
                                '9515dc91fc08cfc0dda0': registry.Entry(timestamp=1109428838.2248061,
                                                                       actor=L1640),
                                '1955787528046718785': registry.Entry(timestamp=1104689968.784857,
                                                                      actor=L399),
                                '4b6ad410a34d5b6c16ee': registry.Entry(timestamp=1105921803.8393171,
                                                                       actor=L972),
                                '5b0ee41b18f3e75167a2': registry.Entry(timestamp=1104797063.3379431,
                                                                       actor=L1615),
                                'd09a2d478bd604dc3907': registry.Entry(timestamp=1109435120.102756,
                                                                       actor=L968),
                                '4eec14b8e7620b9cbbf6': registry.Entry(timestamp=1104797063.3455911,
                                                                       actor=L921),
                                '5ce1f20ddbfb0d7dbdc8': registry.Entry(timestamp=1109422775.132426,
                                                                       actor=L1242),
                                '9360497806179331195': registry.Entry(timestamp=1104650930.792357,
                                                                      actor=L492),
                                'd56af1fc4e478d2676e4': registry.Entry(timestamp=1109424447.451117,
                                                                       actor=L1691),
                                '17127538032127337902': registry.Entry(timestamp=1104730109.318953,
                                                                       actor=L1291),
                                'f087d80a9309247b65a': registry.Entry(timestamp=1108956695.1802731,
                                                                      actor=L39),
                                '844713905205980550': registry.Entry(timestamp=1104730109.319428,
                                                                     actor=L1493),
                                '17611950891294426261': registry.Entry(timestamp=1104690171.623419,
                                                                       actor=L1061),
                                'f58848882bb5b9bb3ac8': registry.Entry(timestamp=1109433508.5816081,
                                                                       actor=L300),
                                '8cf176cfe796cd156975': registry.Entry(timestamp=1190665181.345289,
                                                                       actor=L977),
                                '1d080e958d08e20c362b': registry.Entry(timestamp=1109434485.9212029,
                                                                       actor=L311),
                                'f8ff73eb7cf1b9941a73': registry.Entry(timestamp=1109428388.6854019,
                                                                       actor=L239),
                                '9057425907194955737': registry.Entry(timestamp=1105488351.8877051,
                                                                      actor=L449),
                                '3518475730128674669': registry.Entry(timestamp=1104730507.83989,
                                                                      actor=L1634),
                                '4227047065147840205': registry.Entry(timestamp=1104650529.884198,
                                                                      actor=L1515),
                                '12634790733065757812': registry.Entry(timestamp=1104632228.343287,
                                                                       actor=L166),
                                '12685563122316055259': registry.Entry(timestamp=1104706912.387881,
                                                                       actor=L419),
                                'c4fbf97dd8919c749ca9': registry.Entry(timestamp=1190664333.911598,
                                                                       actor=L506),
                                '10330519763115726681': registry.Entry(timestamp=1104689888.177563,
                                                                       actor=L841),
                                'a51f96a48acf383d67b6': registry.Entry(timestamp=1108956747.618078,
                                                                       actor=L109),
                                '8511836882149982016': registry.Entry(timestamp=1104650706.713083,
                                                                      actor=L849),
                                '232be96254a60b1185f4': registry.Entry(timestamp=1109428842.672349,
                                                                       actor=L1623),
                                'eaad67a6f405387e7f63': registry.Entry(timestamp=1109428392.426419,
                                                                       actor=L211),
                                '1f450f46787e5df1a832': registry.Entry(timestamp=1109433892.9024999,
                                                                       actor=L283),
                                'f57378bfa8f1bda4717f': registry.Entry(timestamp=1109428871.343946,
                                                                       actor=L1630),
                                'e6e700e2d7e729e3e72': registry.Entry(timestamp=1104807950.8954489,
                                                                      actor=L712),
                                '2f63027d1e8f1c1a37fd': registry.Entry(timestamp=1109428835.8189859,
                                                                       actor=L522),
                                '16136617492328534660': registry.Entry(timestamp=1104650949.250061,
                                                                       actor=L1040),
                                '6c6ed31f12ce3e23a22a': registry.Entry(timestamp=1109434683.425472,
                                                                       actor=L961),
                                '14138594607498135940': registry.Entry(timestamp=1104650760.299006,
                                                                       actor=L491),
                                '9638377965285201700': registry.Entry(timestamp=1104632228.3473179,
                                                                      actor=L525),
                                '1aa5ec03a965669b0022': registry.Entry(timestamp=1109423781.7648139,
                                                                       actor=L843),
                                '236d38760c6a183af6f8': registry.Entry(timestamp=1108956215.9963861,
                                                                       actor=L1071),
                                '1546622807325074855': registry.Entry(timestamp=1104696117.3322141,
                                                                      actor=L436),
                                '7936621921662856627': registry.Entry(timestamp=1104650549.672792,
                                                                      actor=L799),
                                'e87eee5c7103444d365b': registry.Entry(timestamp=1108412101.378515,
                                                                       actor=L634),
                                '941178e1441881defb2b': registry.Entry(timestamp=1108412101.4808841,
                                                                       actor=L1033),
                                '97cdf671f963709d9eb3': registry.Entry(timestamp=1108412173.8229091,
                                                                       actor=L501),
                                '6817141969146993628': registry.Entry(timestamp=1104708982.6086359,
                                                                      actor=L967),
                                '12545444783397887118': registry.Entry(timestamp=1104693955.28495,
                                                                       actor=L440),
                                '7a19485e947469b48f5d': registry.Entry(timestamp=1105921826.4260719,
                                                                       actor=L1124),
                                '13319024784900900893': registry.Entry(timestamp=1104730507.798197,
                                                                       actor=L1254),
                                '12946586331713097828': registry.Entry(timestamp=1104650753.210412,
                                                                       actor=L490),
                                '1061218531910574846': registry.Entry(timestamp=1104706912.3873279,
                                                                      actor=L420),
                                '59366674524a8992ec57': registry.Entry(timestamp=1105921808.808475,
                                                                       actor=L1230),
                                '34874108ea81817dd45f': registry.Entry(timestamp=1109428828.336385,
                                                                       actor=L1137),
                                '620b2cb3deba6d946d89': registry.Entry(timestamp=1109433834.8225541,
                                                                       actor=L293),
                                '11512313525346285370': registry.Entry(timestamp=1104730109.340476,
                                                                       actor=L589),
                                '2496797421715521539': registry.Entry(timestamp=1104732153.4440341,
                                                                      actor=L707),
                                '4f4d746968439adc77f8': registry.Entry(timestamp=1108956726.5260489,
                                                                       actor=L1641),
                                'fc67e57428a80e5c577': registry.Entry(timestamp=1109434690.4835491,
                                                                      actor=L1627),
                                '959c6923ca073aa23ec2': registry.Entry(timestamp=1105921745.7405829,
                                                                       actor=L1188),
                                '9e1868775012070da71': registry.Entry(timestamp=1109434991.6687219,
                                                                      actor=L1250),
                                'd0f449aa58533e36ea69': registry.Entry(timestamp=1109433966.3965299,
                                                                       actor=L310),
                                '27642d37c9e93d88a9d3': registry.Entry(timestamp=1108412173.8300371,
                                                                       actor=L648),
                                '66d46b6a4c45495d85f': registry.Entry(timestamp=1108412101.364145,
                                                                      actor=L1035),
                                'c4491d62f5b2c77c1788': registry.Entry(timestamp=1109435027.723671,
                                                                       actor=L925),
                                '9cab7b2aaf0861d72052': registry.Entry(timestamp=1105921513.584868,
                                                                       actor=L1649),
                                'b378f20f4218f5661db8': registry.Entry(timestamp=1109428186.7802711,
                                                                       actor=L228),
                                '38674a8406c10d8acc66': registry.Entry(timestamp=1105921513.4133351,
                                                                       actor=L1189),
                                '11497005180784433127': registry.Entry(timestamp=1104730109.3140781,
                                                                       actor=L1237),
                                '11885770933734303644': registry.Entry(timestamp=1104689888.176734,
                                                                       actor=L838),
                                '2909c2803333fa9763dd': registry.Entry(timestamp=1190665226.653671,
                                                                       actor=L1699),
                                'abd8c6c996e0bdee54ab': registry.Entry(timestamp=1105921788.513629,
                                                                       actor=L542),
                                '40318dd352f07bad2f32': registry.Entry(timestamp=1109435048.0906439,
                                                                       actor=L115),
                                'a3707eafba7f8c29438f': registry.Entry(timestamp=1190665181.3520789,
                                                                       actor=L1409),
                                '7725879995356042119': registry.Entry(timestamp=1104633105.5330541,
                                                                      actor=L784),
                                'c28f00da84aabe9711f8': registry.Entry(timestamp=1109428846.2577951,
                                                                       actor=L709),
                                '8275236787514389161': registry.Entry(timestamp=1104732146.0397589,
                                                                      actor=L1576),
                                '1049070116954587991': registry.Entry(timestamp=1104697494.401659,
                                                                      actor=L1490),
                                '211eb2ea127cce5956ea': registry.Entry(timestamp=1109433447.629179,
                                                                       actor=L350),
                                '6ae432c49f19b06e3dce': registry.Entry(timestamp=1109424192.8307281,
                                                                       actor=L1183),
                                '6842470814180133769': registry.Entry(timestamp=1104632241.948518,
                                                                      actor=L158),
                                '3adc62bc55fb88be1f69': registry.Entry(timestamp=1108412101.3760641,
                                                                       actor=L1248),
                                '5dc7e64e69d3a5a73189': registry.Entry(timestamp=1105921748.370198,
                                                                       actor=L569),
                                '1817218079521314969': registry.Entry(timestamp=1104632228.3319261,
                                                                      actor=L1245),
                                '16897814623275256082': registry.Entry(timestamp=1104632239.2551229,
                                                                       actor=L153),
                                '7984984827063085602': registry.Entry(timestamp=1104730507.8248301,
                                                                      actor=L1617),
                                '10726820175615189179': registry.Entry(timestamp=1104650549.657733,
                                                                       actor=L788),
                                '848b9113b67cd5bfccbc': registry.Entry(timestamp=1105921513.6032341,
                                                                       actor=L1064),
                                'd368cd1b3e772c0dee3a': registry.Entry(timestamp=1109433734.2794211,
                                                                       actor=L307),
                                'eea508d94e56f68e728b': registry.Entry(timestamp=1108956215.9550979,
                                                                       actor=L4),
                                'f675ab66721705423554': registry.Entry(timestamp=1109434712.600971,
                                                                       actor=L1633),
                                '15000248107523643647': registry.Entry(timestamp=1104732488.3008361,
                                                                       actor=L1688),
                                '13176058059947371572': registry.Entry(timestamp=1104697346.2155011,
                                                                       actor=L1182),
                                '6737ab2d99858d2cb98e': registry.Entry(timestamp=1190665221.2731609,
                                                                       actor=L1143),
                                'b25d5843447a0422c30a': registry.Entry(timestamp=1108412101.3371241,
                                                                       actor=L117),
                                '2a4f7a3dcd2f87a7532b': registry.Entry(timestamp=1105921690.9049809,
                                                                       actor=L578),
                                'e20bc13b888334ad3537': registry.Entry(timestamp=1108956448.854455,
                                                                       actor=L74),
                                '15354271914547105265': registry.Entry(timestamp=1104689747.0002921,
                                                                       actor=L1578),
                                '9829540809193203453': registry.Entry(timestamp=1104633108.691174,
                                                                      actor=L1497),
                                '11244828830854864470': registry.Entry(timestamp=1104633047.078866,
                                                                       actor=L1480),
                                '9e55068b582c80b9f474': registry.Entry(timestamp=1108412101.4894359,
                                                                       actor=L1622),
                                'de5f81ed1b494d3519df': registry.Entry(timestamp=1109433597.6299551,
                                                                       actor=L278),
                                '6aa8789df5ecc4190c79': registry.Entry(timestamp=1108956850.9261429,
                                                                       actor=L55),
                                'f8670e226436fa73128f': registry.Entry(timestamp=1109428826.413799,
                                                                       actor=L251),
                                'def59007c148e24940ad': registry.Entry(timestamp=1190664334.0511611,
                                                                       actor=L970),
                                '35269d3b8f3f78114257': registry.Entry(timestamp=1108956796.8554609,
                                                                       actor=L35),
                                'fa59d03a167a4c1b94ff': registry.Entry(timestamp=1109434755.246258,
                                                                       actor=L314),
                                'fcceeb077cb614ca85f8': registry.Entry(timestamp=1105921806.0911419,
                                                                       actor=L1293),
                                '93a74d12b66f1bf6d440': registry.Entry(timestamp=1109677336.731226,
                                                                       actor=L167),
                                '5d52906b91dc36916500': registry.Entry(timestamp=1104807950.912137,
                                                                       actor=L1635),
                                '54573033a0f923d876e0': registry.Entry(timestamp=1109422775.108053,
                                                                       actor=L1642),
                                '120d37656e5a1a12158e': registry.Entry(timestamp=1109428443.6542909,
                                                                       actor=L235),
                                '4667264518391135515': registry.Entry(timestamp=1104650724.1308751,
                                                                      actor=L508),
                                'e94c4dff11c20c4a0886': registry.Entry(timestamp=1104797071.7125549,
                                                                       actor=L936),
                                '3324730690425372007': registry.Entry(timestamp=1104650549.6319871,
                                                                      actor=L1610),
                                '5591050765793200711': registry.Entry(timestamp=1104732505.688601,
                                                                      actor=L1486),
                                '12051635174327115429': registry.Entry(timestamp=1104650712.6820021,
                                                                       actor=L1631),
                                '9fe8821ff61c3fe3b77d': registry.Entry(timestamp=1109422775.0955131,
                                                                       actor=L1375),
                                '56191cb3e8143011d87c': registry.Entry(timestamp=1190665181.347971,
                                                                       actor=L978),
                                '5274326361166066280': registry.Entry(timestamp=1104693745.0998559,
                                                                      actor=L431),
                                '13270445787827545889': registry.Entry(timestamp=1104730109.3088651,
                                                                       actor=L963),
                                'c223f740d0189de07951': registry.Entry(timestamp=1109435170.1033919,
                                                                       actor=L1073),
                                '9ed64c1f46f388ef377e': registry.Entry(timestamp=1108412240.3527069,
                                                                       actor=L1131),
                                '1a3edd7a42ba08472afd': registry.Entry(timestamp=1108956448.852829,
                                                                       actor=L1059),
                                '55786e30b2bf1b3ea69f': registry.Entry(timestamp=1109428799.6917369,
                                                                       actor=L643),
                                '4442827039649434997': registry.Entry(timestamp=1104650930.7920511,
                                                                      actor=L973),
                                '322fb4bc7605aa8653e2': registry.Entry(timestamp=1109435009.982374,
                                                                       actor=L1177),
                                '474b80e51e808fed1a99': registry.Entry(timestamp=1109433451.294275,
                                                                       actor=L168),
                                '12128037699416130148': registry.Entry(timestamp=1104732146.0393341,
                                                                       actor=L1575),
                                '6f3a7f7d336523b08bd4': registry.Entry(timestamp=1109422775.123138,
                                                                       actor=L1027),
                                '10871997212631801029': registry.Entry(timestamp=1104730109.3334141,
                                                                       actor=L1186),
                                '13387220976027820258': registry.Entry(timestamp=1104650712.644146,
                                                                       actor=L1487),
                                '7a89bcf8d307b258b3b4': registry.Entry(timestamp=1109435009.9851551,
                                                                       actor=L368),
                                '672462e5d7d6c8606fe3': registry.Entry(timestamp=1109434948.9922681,
                                                                       actor=L182),
                                '708093d3f5efae9ceb81': registry.Entry(timestamp=1109435009.994391,
                                                                       actor=L1227),
                                '67eeb2429b63101a4ec7': registry.Entry(timestamp=1108412161.574615,
                                                                       actor=L1495),
                                '994f72d124ba4ab3e643': registry.Entry(timestamp=1109435124.707993,
                                                                       actor=L642),
                                '1679989706457713520': registry.Entry(timestamp=1104706912.3876929,
                                                                      actor=L422),
                                'e18028cacd7efe69dfbb': registry.Entry(timestamp=1190665154.678051,
                                                                       actor=L1016),
                                '6402116433048299654': registry.Entry(timestamp=1104650712.6671181,
                                                                      actor=L1125),
                                '70ca891a948da6b4fd73': registry.Entry(timestamp=1109422775.1296489,
                                                                       actor=L1187),
                                '15511116157062632786': registry.Entry(timestamp=1104650712.6740661,
                                                                       actor=L1141),
                                'fff687e48591806e7d56': registry.Entry(timestamp=1109435168.3178489,
                                                                       actor=L1682),
                                'b774260d0676ba628669': registry.Entry(timestamp=1104797063.3239031,
                                                                       actor=L1367),
                                'b714558827a1934689eb': registry.Entry(timestamp=1109435027.72104,
                                                                       actor=L924),
                                '9ffceadfb339bf0a37b7': registry.Entry(timestamp=1109434995.1128759,
                                                                       actor=L1239),
                                'dee2d9a8289d27ac176a': registry.Entry(timestamp=1109424028.7127371,
                                                                       actor=L223),
                                '804e5b1a3b2aadf7c001': registry.Entry(timestamp=1109423781.762228,
                                                                       actor=L842),
                                '13472432016877657261': registry.Entry(timestamp=1104650549.645519,
                                                                       actor=L1134),
                                '4cb50eebe02b70a0d71b': registry.Entry(timestamp=1190664334.091352,
                                                                       actor=L1619),
                                '9564f27dcab30da4c8d4': registry.Entry(timestamp=1190664334.0540831,
                                                                       actor=L1611),
                                '25c2e6f96744ae60c374': registry.Entry(timestamp=1105921513.572356,
                                                                       actor=L1225),
                                'CCDF40493E712274L': registry.Entry(timestamp=1104796672.1500449,
                                                                    actor=L1294),
                                '93ea785fea4a1506079a': registry.Entry(timestamp=1108412161.5768311,
                                                                       actor=L671),
                                '22eb057b0621169328c9': registry.Entry(timestamp=1108956215.9773271,
                                                                       actor=L1365),
                                '73d4b6bd3504795305a1': registry.Entry(timestamp=1109424445.3275061,
                                                                       actor=L256),
                                '8060076283853931247': registry.Entry(timestamp=1104650549.665045,
                                                                      actor=L1616),
                                '7472656884655288975': registry.Entry(timestamp=1104689853.1316221,
                                                                      actor=L1243),
                                'fd0e0dcd73af9e72f597': registry.Entry(timestamp=1108956216.009995,
                                                                       actor=L1232),
                                '17980192334006365197': registry.Entry(timestamp=1104632228.403507,
                                                                       actor=L521),
                                '7fd28421399c0260a1a0': registry.Entry(timestamp=1109428731.5971761,
                                                                       actor=L216),
                                '4178227206424925539': registry.Entry(timestamp=1104650549.674288,
                                                                      actor=L1070),
                                '15250013233234179905': registry.Entry(timestamp=1104632228.3750589,
                                                                       actor=L1479),
                                '6c85152f239871975017': registry.Entry(timestamp=1109428208.878855,
                                                                       actor=L848),
                                '3cb26424481623ed41bc': registry.Entry(timestamp=1108956926.1981299,
                                                                       actor=L60),
                                '1c4a4e54eec83f776e4a': registry.Entry(timestamp=1109424192.8323901,
                                                                       actor=L1184),
                                '12946925928954107809': registry.Entry(timestamp=1104730507.796433,
                                                                       actor=L769),
                                '92d4a78cea106df07c2c': registry.Entry(timestamp=1108956796.853735,
                                                                       actor=L1236),
                                '14095654525563810214': registry.Entry(timestamp=1104694007.8913209,
                                                                       actor=L1628),
                                'a14d85d55467ffe04ee0': registry.Entry(timestamp=1109435018.4971809,
                                                                       actor=L780),
                                'c25353745b522913f4c2': registry.Entry(timestamp=1109424299.653085,
                                                                       actor=L2),
                                '659985c7578a877b07e3': registry.Entry(timestamp=1109428804.8175659,
                                                                       actor=L1037),
                                '4f3f54f1d8db5a25f118': registry.Entry(timestamp=1108956216.005373,
                                                                       actor=L1063),
                                '13661059783025868973': registry.Entry(timestamp=1104633042.4138801,
                                                                       actor=L156),
                                '7aa131ceb0eae191a3ed': registry.Entry(timestamp=1108956833.1141219,
                                                                       actor=L3),
                                '6055406963319936966': registry.Entry(timestamp=1104650753.2101431,
                                                                      actor=L1408),
                                '354f3356b414dbdf6595': registry.Entry(timestamp=1109435083.837661,
                                                                       actor=L273),
                                '10927938414203847443': registry.Entry(timestamp=1104689958.5300021,
                                                                       actor=L425),
                                '420e55efa0fb8d8f2ffd': registry.Entry(timestamp=1109428835.814178,
                                                                       actor=L244),
                                'fd6a40ab5331a449ac99': registry.Entry(timestamp=1104797063.2925529,
                                                                       actor=L931),
                                '1359982258694374825': registry.Entry(timestamp=1104632228.379292,
                                                                      actor=L1067),
                                '10593314374053890933': registry.Entry(timestamp=1104730507.788162,
                                                                       actor=L1120),
                                'ad509debf6bb51e095c9': registry.Entry(timestamp=1108412101.357022,
                                                                       actor=L504),
                                'b33414f37886533390d2': registry.Entry(timestamp=1108412161.582691,
                                                                       actor=L675),
                                'f5a54a967633535bf134': registry.Entry(timestamp=1109422948.6272831,
                                                                       actor=L209),
                                '10103513020179766570': registry.Entry(timestamp=1104690335.904788,
                                                                       actor=L423),
                                'c757003da8382520250d': registry.Entry(timestamp=1105921822.3753741,
                                                                       actor=L1022),
                                '261ec3b86d5f1af30a43': registry.Entry(timestamp=1109435160.16693,
                                                                       actor=L1644),
                                '14107852319538388771': registry.Entry(timestamp=1104730507.833338,
                                                                       actor=L1492),
                                '73f50a3f60d178768e5d': registry.Entry(timestamp=1104807950.8976121,
                                                                       actor=L713),
                                'f9ab36734295b51f1fb9': registry.Entry(timestamp=1109435170.1005421,
                                                                       actor=L338),
                                '3ed58789fe9a7d9623fa': registry.Entry(timestamp=1104797063.3068709,
                                                                       actor=L1249),
                                '11549355846312153998': registry.Entry(timestamp=1104632228.3814001,
                                                                       actor=L798),
                                '3191a13927a42a0aca34': registry.Entry(timestamp=1109428764.7491829,
                                                                       actor=L1032),
                                '9ca23758d3e14b14e22f': registry.Entry(timestamp=1105921548.3496211,
                                                                       actor=L1128),
                                '4138178436990957034': registry.Entry(timestamp=1104732505.688319,
                                                                      actor=L1485),
                                '6920636786683624616': registry.Entry(timestamp=1104690523.1329401,
                                                                      actor=L1613),
                                '32b6411e86ed3305be63': registry.Entry(timestamp=1108956726.5277021,
                                                                       actor=L30),
                                '14726587180619911525': registry.Entry(timestamp=1104633035.78582,
                                                                       actor=L164),
                                'a125bcaed7f5954b9150': registry.Entry(timestamp=1109422775.1189499,
                                                                       actor=L1138),
                                '1564538181099476570': registry.Entry(timestamp=1104690401.654279,
                                                                      actor=L1362),
                                'ac567c51e8219e69ff16': registry.Entry(timestamp=1190664334.070976,
                                                                       actor=L1698),
                                'f4e883b36a48f3be4880': registry.Entry(timestamp=1109422945.6852801,
                                                                       actor=L248),
                                'dfd2c79df992922d1acf': registry.Entry(timestamp=1105921540.9413459,
                                                                       actor=L1689),
                                '12182569062741163979': registry.Entry(timestamp=1104730109.3149381,
                                                                       actor=L627),
                                'ca15ef2c3a7701c12458': registry.Entry(timestamp=1109423159.0988619,
                                                                       actor=L213),
                                '1b5a49fb0fec6944ecc4': registry.Entry(timestamp=1105921513.538332,
                                                                       actor=L1247),
                                'a7bd903423cd5317bd7b': registry.Entry(timestamp=1109428831.4499919,
                                                                       actor=L1489),
                                '17801320630458131755': registry.Entry(timestamp=1104689816.700052,
                                                                       actor=L1629),
                                '2d3ff26bf3a1ccdbda01': registry.Entry(timestamp=1109428838.222214,
                                                                       actor=L1639),
                                '13838842964897476745': registry.Entry(timestamp=1104650720.799705,
                                                                       actor=L1244),
                                'f96001099601a04981f6': registry.Entry(timestamp=1108956537.787472,
                                                                       actor=L65),
                                '9191949582763768590': registry.Entry(timestamp=1104732153.4437671,
                                                                      actor=L706),
                                'cea976a1318c7f6a6ec': registry.Entry(timestamp=1109434693.650279,
                                                                      actor=L346),
                                '7798158345955886274': registry.Entry(timestamp=1104650549.6464159,
                                                                      actor=L831),
                                '3cadcfebb3425343d2ae': registry.Entry(timestamp=1109434660.0012491,
                                                                       actor=L325),
                                '2956948422716100561': registry.Entry(timestamp=1104706912.386812,
                                                                      actor=L421),
                                '4131740470354140357': registry.Entry(timestamp=1104697377.9553559,
                                                                      actor=L442),
                                '740e543a73fba8ae453f': registry.Entry(timestamp=1109677327.1529441,
                                                                       actor=L1259),
                                'e568157c9501ba7cfc6a': registry.Entry(timestamp=1109428462.781116,
                                                                       actor=L644),
                                'c700b53d7a40117bd126': registry.Entry(timestamp=1109435168.315073,
                                                                       actor=L1683),
                                '2805739992860418134': registry.Entry(timestamp=1104650712.650219,
                                                                      actor=L1065),
                                'a80d84152cb05bbf1286': registry.Entry(timestamp=1109424025.394774,
                                                                       actor=L225),
                                '8549478301856461533': registry.Entry(timestamp=1104730507.77914,
                                                                      actor=L1651),
                                '400632f1c4d59068aadc': registry.Entry(timestamp=1104797063.3278401,
                                                                       actor=L702),
                                '3bcc6e02355a4489272b': registry.Entry(timestamp=1109434795.845222,
                                                                       actor=L1136),
                                '12904228506947022660': registry.Entry(timestamp=1104632228.327944,
                                                                       actor=L1516),
                                'af6bc0bdd2da549d34ab': registry.Entry(timestamp=1109435027.7326839,
                                                                       actor=L1135),
                                '978002a771fdb82dea39': registry.Entry(timestamp=1109435124.705168,
                                                                       actor=L641),
                                '8ab96d54de6dae117484': registry.Entry(timestamp=1109428846.255095,
                                                                       actor=L708),
                                '905b734d21990d905889': registry.Entry(timestamp=1109422775.0432079,
                                                                       actor=L767),
                                '8608183716299200486': registry.Entry(timestamp=1104632228.3480451,
                                                                      actor=L928),
                                '7436199748876259015': registry.Entry(timestamp=1104696844.4145091,
                                                                      actor=L1034),
                                '63d95a5f3af1685a4628': registry.Entry(timestamp=1104807978.8575661,
                                                                       actor=L974),
                                '69de3657b02e113b0f93': registry.Entry(timestamp=1108412173.8187251,
                                                                       actor=L700),
                                '14955675966070121265': registry.Entry(timestamp=1104650712.6410279,
                                                                       actor=L1579),
                                'f607f8a7a922d909c959': registry.Entry(timestamp=1105921825.2458611,
                                                                       actor=L1292),
                                '81ea31f2e40de4411915': registry.Entry(timestamp=1108956454.267065,
                                                                       actor=L1256),
                                'ea1042a44339a6b6299c': registry.Entry(timestamp=1108956216.0383761,
                                                                       actor=L976),
                                '4f7773f6e389793f5cff': registry.Entry(timestamp=1109428842.6749821,
                                                                       actor=L1624),
                                '77c7ce5c863dd5a05a76': registry.Entry(timestamp=1109422775.0328751,
                                                                       actor=L1260),
                                '1011012714027468268': registry.Entry(timestamp=1104650712.6589899,
                                                                      actor=L1185),
                                'c171aaf4622a67eec25f': registry.Entry(timestamp=1105921745.787854,
                                                                       actor=L571),
                                '13286087984584598130': registry.Entry(timestamp=1104650712.6619079,
                                                                       actor=L1573),
                                '96f0ef4cbdcdc2586bf0': registry.Entry(timestamp=1109428182.139416,
                                                                       actor=L510),
                                '40a8e69a8169b7a993b1': registry.Entry(timestamp=1108956889.0060489,
                                                                       actor=L929),
                                '10e10ac18640c6dd2364': registry.Entry(timestamp=1109434627.705112,
                                                                       actor=L1618),
                                '4939350837483695449': registry.Entry(timestamp=1104730109.317359,
                                                                      actor=L511),
                                'daa4bbacf74bab652f0a': registry.Entry(timestamp=1109434477.727283,
                                                                       actor=L1126),
                                '8096643624464055522': registry.Entry(timestamp=1104633049.924382,
                                                                      actor=L162),
                                'c6395c42b17dc6409a98': registry.Entry(timestamp=1108956695.1835511,
                                                                       actor=L1178),
                                'ce21e0cc674c8dff1aa1': registry.Entry(timestamp=1109428875.2832229,
                                                                       actor=L1621),
                                'f1b64b96203dc1031e47': registry.Entry(timestamp=1109433805.3580141,
                                                                       actor=L280),
                                'f2761198c8015e58297d': registry.Entry(timestamp=1109422775.0365369,
                                                                       actor=L1028),
                                '987ba6d80c536ef72fd3': registry.Entry(timestamp=1104796957.85256,
                                                                       actor=L1411),
                                '112755c6b7b0197ca6bb': registry.Entry(timestamp=1105921513.5788419,
                                                                       actor=L1514),
                                '335fd96b953d2239db53': registry.Entry(timestamp=1109433926.7197659,
                                                                       actor=L286),
                                '2c4f6289354906ecf08': registry.Entry(timestamp=1109424447.4493661,
                                                                      actor=L1692),
                                '12473ee71c96cd605738': registry.Entry(timestamp=1108412101.3312759,
                                                                       actor=L1377),
                                '477d1d63d2661835065d': registry.Entry(timestamp=1105921513.564682,
                                                                       actor=L1366),
                                '14095783355500097386': registry.Entry(timestamp=1104633023.2535551,
                                                                       actor=L1612),
                                '84af1be6f390fc4f0d92': registry.Entry(timestamp=1108412234.059459,
                                                                       actor=L1376),
                                '76105c3de42692569c7f': registry.Entry(timestamp=1190665257.4738071,
                                                                       actor=L1018),
                                'c97d9bb0c2aa5df61e6e': registry.Entry(timestamp=1108412101.454735,
                                                                       actor=L1609),
                                'dc10179ce6eb719eddec': registry.Entry(timestamp=1105921587.3464301,
                                                                       actor=L582),
                                '132bd817a0e8acb0485e': registry.Entry(timestamp=1108956833.1580081,
                                                                       actor=L57),
                                '40e51ffc174da6c81c4f': registry.Entry(timestamp=1108412101.37217,
                                                                       actor=L1632),
                                '5292533547202728044': registry.Entry(timestamp=1104730442.7894969,
                                                                      actor=L887),
                                'f84c449eddb7e174f514': registry.Entry(timestamp=1108956539.883023,
                                                                       actor=L1374),
                                '16495268673511082035': registry.Entry(timestamp=1104795314.0476921,
                                                                       actor=L1650),
                                '89b4ca205464b571e41e': registry.Entry(timestamp=1109428157.5395341,
                                                                       actor=L1369),
                                '8a9f1ac419253f7817c7': registry.Entry(timestamp=1105921826.4286239,
                                                                       actor=L1123),
                                '9462070805789713288': registry.Entry(timestamp=1104650549.652365,
                                                                      actor=L1686),
                                '15604201270503278878': registry.Entry(timestamp=1104632228.3436141,
                                                                       actor=L119),
                                '12079799893167868995': registry.Entry(timestamp=1104693742.1302421,
                                                                       actor=L433),
                                'daf060d1d66ad487dee3': registry.Entry(timestamp=1109435117.514183,
                                                                       actor=L1694),
                                'c88c9deae9a8bad90c4': registry.Entry(timestamp=1190664334.047466,
                                                                      actor=L1015),
                                '5217137786238671049': registry.Entry(timestamp=1104632241.9482341,
                                                                      actor=L1368),
                                '1f966172227f701d36a1': registry.Entry(timestamp=1109434798.857053,
                                                                       actor=L1626),
                                '7522505065968084182': registry.Entry(timestamp=1104730507.792691,
                                                                      actor=L1364),
                                '2ce2546b3a61d585544e': registry.Entry(timestamp=1108412161.584934,
                                                                       actor=L678),
                                '10579116576104148034': registry.Entry(timestamp=1104632797.6333671,
                                                                       actor=L786),
                                'bc6686a069873608f287': registry.Entry(timestamp=1109434503.0064521,
                                                                       actor=L321),
                                'cac21146f6ccd1384dcb': registry.Entry(timestamp=1108956794.6392231,
                                                                       actor=L1062),
                                '12427553908187455670': registry.Entry(timestamp=1104730109.330364,
                                                                       actor=L1036),
                                '4edd14e178ad0c694a5f': registry.Entry(timestamp=1104807944.3474181,
                                                                       actor=L930),
                                '1f894cedda7a5116c672': registry.Entry(timestamp=1109433555.5110941,
                                                                       actor=L172),
                                '202f42bea33bd7dcb5c7': registry.Entry(timestamp=1105921808.8114059,
                                                                       actor=L1229),
                                '11346868527983282560': registry.Entry(timestamp=1104632803.6578569,
                                                                       actor=L1482),
                                '12280374078573952893': registry.Entry(timestamp=1104689747.0388479,
                                                                       actor=L446),
                                '5186614581370432354': registry.Entry(timestamp=1104730776.1944089,
                                                                      actor=L1648),
                                '3719337025926476596': registry.Entry(timestamp=1104650549.6292789,
                                                                      actor=L850),
                                '7708682ba51a597e4483': registry.Entry(timestamp=1109427882.6983581,
                                                                       actor=L1370),
                                '3d7fe3f0661198add7d2': registry.Entry(timestamp=1108956216.0018411,
                                                                       actor=L1491),
                                'b6d022a6aab1a9c58c67': registry.Entry(timestamp=1105921513.5993609,
                                                                       actor=L526),
                                '7838193153830263651': registry.Entry(timestamp=1104730507.7985001,
                                                                      actor=L1122),
                                'ca30c87e605ba765be06': registry.Entry(timestamp=1109428804.8202569,
                                                                       actor=L1038),
                                '5ee3a50d3351e3b67fd4': registry.Entry(timestamp=1104807950.9019289,
                                                                       actor=L1494),
                                '10584963968992807980': registry.Entry(timestamp=1104730109.3000181,
                                                                       actor=L888),
                                '63af8fe6397a4ec62ec8': registry.Entry(timestamp=1104807978.85042,
                                                                       actor=L760),
                                'fc1d1a3284d605538654': registry.Entry(timestamp=1109422775.0987959,
                                                                       actor=L272),
                                '129f5ab2812ebd35a6f3': registry.Entry(timestamp=1108956527.0244949,
                                                                       actor=L67),
                                '2737335135250149149': registry.Entry(timestamp=1104650724.1311619,
                                                                      actor=L489),
                                'cf3306171571f5115689': registry.Entry(timestamp=1109435018.505995,
                                                                       actor=L1226),
                                '15550032082523474268': registry.Entry(timestamp=1104650556.4493201,
                                                                       actor=L1127),
                                'a9cb48105a7013552f52': registry.Entry(timestamp=1108412234.392565,
                                                                       actor=L692),
                                '1245e3bda58496bdf7e7': registry.Entry(timestamp=1105921513.4643559,
                                                                       actor=L584),
                                '1347a00d734365bfd85e': registry.Entry(timestamp=1108956747.616488,
                                                                       actor=L1031),
                                '3491372217552124879': registry.Entry(timestamp=1104694604.2031541,
                                                                      actor=L1258),
                                '13101820419664547343': registry.Entry(timestamp=1104632307.7753921,
                                                                       actor=L785),
                                '48c31983ab36c2b93869': registry.Entry(timestamp=1109422775.113838,
                                                                       actor=L1572),
                                '2226060574216469791': registry.Entry(timestamp=1104795314.147552,
                                                                      actor=L964),
                                '6461598025166001448': registry.Entry(timestamp=1104689796.4098401,
                                                                      actor=L395),
                                '11009507096081710421': registry.Entry(timestamp=1104650949.2503321,
                                                                       actor=L1041),
                                'd6b5b4340e8822d2762c': registry.Entry(timestamp=1109434804.450887,
                                                                       actor=L1251),
                                '11031015219216838346': registry.Entry(timestamp=1104730109.341886,
                                                                       actor=L705),
                                'bb790ac1a0ee7ed3ea5b': registry.Entry(timestamp=1109434798.854404,
                                                                       actor=L1625),
                                'c136252aeda06b05ab25': registry.Entry(timestamp=1108412101.4477329,
                                                                       actor=L1039),
                                '6752b9d510ea35cf88d9': registry.Entry(timestamp=1190664334.057488,
                                                                       actor=L1255),
                                '40e992d83eee6dfcc7a5': registry.Entry(timestamp=1108412101.3672991,
                                                                       actor=L699),
                                'c16a270d21302658f53d': registry.Entry(timestamp=1108956776.0309,
                                                                       actor=L37),
                                '35b913d9f1a9ff04226a': registry.Entry(timestamp=1109435098.7016151,
                                                                       actor=L1026),
                                '16622057499147950833': registry.Entry(timestamp=1104697074.9701481,
                                                                       actor=L412),
                                '3112541654131017587': registry.Entry(timestamp=1104633023.2538221,
                                                                      actor=L1548),
                                '310e5faab910f546eb10': registry.Entry(timestamp=1109434795.8531029,
                                                                       actor=L1025),
                                '33c2fbb146d136f5d402': registry.Entry(timestamp=1109428835.8112259,
                                                                       actor=L1410),
                                '14245085994013281857': registry.Entry(timestamp=1104640325.6669509,
                                                                       actor=L1637),
                                'd3fa83e2175f56e2183f': registry.Entry(timestamp=1109434779.0693159,
                                                                       actor=L966),
                                '10084807298204554591': registry.Entry(timestamp=1104730507.8413301,
                                                                       actor=L1074),
                                '2553436941368336606': registry.Entry(timestamp=1104632803.6574349,
                                                                      actor=L1483),
                                '8343b425fd8ebf32117': registry.Entry(timestamp=1105921548.351846,
                                                                      actor=L1129),
                                'd81a12a2169de556f93d': registry.Entry(timestamp=1108956488.748338,
                                                                       actor=L1119),
                                '18af9ec7344533271914': registry.Entry(timestamp=1109435018.501241,
                                                                       actor=L781),
                                '16060064330232869464': registry.Entry(timestamp=1104730109.3031399,
                                                                       actor=L1241)})
L576 = actors.Actor(env=envs.Env(parent=L530),
                    script=L578)
L690 = actors.Actor(env=envs.Env(parent=L652),
                    script=L692)
L336 = envs.Env(parent=L306)
L334 = actors.Actor(env=envs.Env(parent=L336),
                    script=L311)

L845.define(var='query',
            value=builtin.String(str='Does it bark?'))

L845.define(var='question',
             value=L843)

L845.define(var='animal',
             value=builtin.String(str='dog'))

L210.define(var='makequestion',
             value=L211)

L210.define(var='makeguess',
             value=L223)

L210.define(var='gamebox',
             value=L239)

L170.define(var='box',
             value=L194)

L170.define(var='newanimalgame',
             value=L168)

L170.define(var='makemailbox',
             value=L195)

L170.define(var='animalgame',
             value=L209)

L170.define(var='mailbox',
             value=L261)

L170.define(var='maildirectory',
             value=L268)

L170.define(var='Foo',
             value=L270)

L171.define(var='false',
             value=L172)

L171.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L171.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L171.define(var='makestamp',
             value=builtin.StampMaker())

L171.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L171.define(var='makebox',
             value=L182)

L171.define(var='true',
             value=L183)

L171.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L171.define(var='if',
             value=actors.Actor(env=L171,
                                script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0,
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             selector='true:then:else:')],
                                                     next_serial_id=1)))

L530.define(var='box',
             value=L554)

L530.define(var='makemailbox',
             value=L555)

L530.define(var='mailbox',
             value=L527)

L530.define(var='makeballot',
             value=L569)

L530.define(var='maildirectory',
             value=L574)

L530.define(var='message',
             value=L576)

L530.define(var='Foo',
             value=L582)

L531.define(var='false',
             value=L532)

L531.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L531.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L531.define(var='makestamp',
             value=builtin.StampMaker())

L531.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L531.define(var='makebox',
             value=L542)

L531.define(var='true',
             value=L543)

L531.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L531.define(var='if',
             value=actors.Actor(env=L531,
                                script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0,
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             selector='true:then:else:')],
                                                     next_serial_id=1)))

L246.define(var='box',
             value=L239)

L246.define(var='guess',
             value=L244)

L246.define(var='animal',
             value=L247)

L715.define(var='sender',
             value=L763)

L715.define(var='inbox',
             value=L765)

L715.define(var='mailbox',
             value=L713)

L716.define(var='box',
             value=L739)

L716.define(var='makemailbox',
             value=L740)

L716.define(var='Foo',
             value=L754)

L716.define(var='maildirectory',
             value=L761)

L716.define(var='mailbox',
             value=L713)

L717.define(var='false',
             value=L718)

L717.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L717.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L717.define(var='makestamp',
             value=builtin.StampMaker())

L717.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L717.define(var='makebox',
             value=L703)

L717.define(var='true',
             value=L728)

L717.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L717.define(var='if',
             value=actors.Actor(env=L717,
                                script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0,
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             selector='true:then:else:')],
                                                     next_serial_id=1)))

L1646.define(var='node',
              value=L325)

L1646.define(var='asker',
              value=L1644)

L328.define(var='yesbox',
             value=L329)

L328.define(var='askernode',
             value=L326)

L328.define(var='question',
             value=L344)

L328.define(var='nobox',
             value=L345)

L169.define(var='playgame',
             value=L273)

L169.define(var='makebranch',
             value=L278)

L169.define(var='call',
             value=L300)

L169.define(var='makeguess',
             value=L305)

L169.define(var='root',
             value=L325)

L396.define(var='htmlguard',
             value=L397)

L396.define(var='markup',
             value=L399)

L396.define(var='html',
             value=L423)

L396.define(var='stamppair',
             value=L430)

L396.define(var='htmlstamp',
             value=L398)

L396.define(var='makeattr',
             value=L431)

L396.define(var='showattr',
             value=L440)

L377.define(var='box',
             value=L394)

L377.define(var='htmlmodule',
             value=L395)

L377.define(var='makemailbox',
             value=L473)

L377.define(var='mailbox',
             value=L374)

L377.define(var='maildirectory',
             value=L487)

L377.define(var='pair',
             value=L489)

L377.define(var='x',
             value=L492)

L377.define(var='Foo',
             value=L494)

L378.define(var='true',
             value=L379)

L378.define(var='makestamp',
             value=L385)

L378.define(var='false',
             value=L386)

L378.define(var='makebox',
             value=L392)

L378.define(var='listguard',
             value=L393)

L803.define(var='box',
             value=L814)

L803.define(var='makemailbox',
             value=L815)

L803.define(var='Foo',
             value=L829)

L803.define(var='mailbox',
             value=L800)

L803.define(var='maildirectory',
             value=L832)

L804.define(var='true',
             value=L805)

L804.define(var='makestamp',
             value=L811)

L804.define(var='false',
             value=L789)

L804.define(var='makebox',
             value=L812)

L804.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L1192._add_result(result=L1194,
                   actor=L1188)

L1195._add_result(result=L524,
                   actor=L1188)

L1198._add_result(result=L582,
                   actor=L1188)

L1201._add_result(result=L554,
                   actor=L1188)

L1203._add_result(result=L543,
                   actor=L1188)

L1205._add_result(result=L532,
                   actor=L1188)

L1207._add_result(result=L1209,
                   actor=L1188)

L1212._add_result(result=L574,
                   actor=L1188)

L1215._add_result(result=L527,
                   actor=L1188)

L1219._add_result(result=L1023,
                   actor=L1188)

L1221._add_result(result='Error: Unbound: makek',
                   actor=L1188)

L1223._add_result(result=L569,
                   actor=L1188)

L5.define(var='box',
           value=L29)

L5.define(var='sender',
           value=L30)

L5.define(var='makemailbox',
           value=L51)

L5.define(var='mailbox',
           value=L39)

L5.define(var='makeballot',
           value=L55)

L5.define(var='maildirectory',
           value=L63)

L5.define(var='message',
           value=L35)

L5.define(var='Foo',
           value=L65)

L6.define(var='false',
           value=L7)

L6.define(var='numberguard',
           value=builtin.TypeGuard(sample_instance=0))

L6.define(var='listguard',
           value=builtin.TypeGuard(sample_instance=()))

L6.define(var='makestamp',
           value=builtin.StampMaker())

L6.define(var='booleanguard',
           value=builtin.TypeGuard(sample_instance=True))

L6.define(var='makebox',
           value=L17)

L6.define(var='true',
           value=L18)

L6.define(var='stringguard',
           value=builtin.TypeGuard(sample_instance=''))

L6.define(var='if',
           value=actors.Actor(env=L6,
                              script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                  inner_map={}),
                                                                           serial_id=0,
                                                                           parameters=['test',
                                                                                       'yes',
                                                                                       'no'],
                                                                           selector='true:then:else:')],
                                                   next_serial_id=1)))

L1413.define(var='makemailbox',
              value=actors.Actor(env=L1413,
                                 script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                                     inner_map={'sender': actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                                                                                                                                       inner_map={}),
                                                                                                                                                                serial_id=0,
                                                                                                                                                                parameters=['message'],
                                                                                                                                                                selector='send:')],
                                                                                                                                        next_serial_id=1),
                                                                                                                'mailbox': actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
                                                                                                                                                                                        inner_map={}),
                                                                                                                                                                 serial_id=0,
                                                                                                                                                                 parameters=[],
                                                                                                                                                                 selector='first'),
                                                                                                                                                   actors.Method(body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                                                                                                                                        inner_map={}),
                                                                                                                                                                 serial_id=1,
                                                                                                                                                                 parameters=[],
                                                                                                                                                                 selector='removefirst'),
                                                                                                                                                   actors.Method(body=actors.Expression(text='sender',
                                                                                                                                                                                        inner_map={}),
                                                                                                                                                                 serial_id=2,
                                                                                                                                                                 parameters=[],
                                                                                                                                                                 selector='sender')],
                                                                                                                                         next_serial_id=3)}),
                                                                              serial_id=0,
                                                                              parameters=[],
                                                                              selector='run')],
                                                      next_serial_id=1)))

L1413.define(var='maildirectory',
              value=builtin.MailDirectory(env=envs.Env(parent=L1414)))

L1414.define(var='false',
              value=builtin.Boolean(value=False,
                                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                                        inner_map={}),
                                                                                 serial_id=0,
                                                                                 parameters=[],
                                                                                 selector='not'),
                                                                   actors.Method(body=actors.Expression(text='falsevalue',
                                                                                                        inner_map={}),
                                                                                 serial_id=1,
                                                                                 parameters=['truevalue',
                                                                                             'falsevalue'],
                                                                                 selector='iftrue:iffalse:')],
                                                         next_serial_id=2)))

L1414.define(var='numberguard',
              value=builtin.TypeGuard(sample_instance=0))

L1414.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L1414.define(var='makestamp',
              value=builtin.StampMaker())

L1414.define(var='booleanguard',
              value=builtin.TypeGuard(sample_instance=True))

L1414.define(var='makebox',
              value=builtin.BoxMaker())

L1414.define(var='true',
              value=builtin.Boolean(value=True,
                                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                                        inner_map={}),
                                                                                 serial_id=0,
                                                                                 parameters=[],
                                                                                 selector='not'),
                                                                   actors.Method(body=actors.Expression(text='truevalue',
                                                                                                        inner_map={}),
                                                                                 serial_id=1,
                                                                                 parameters=['truevalue',
                                                                                             'falsevalue'],
                                                                                 selector='iftrue:iffalse:')],
                                                         next_serial_id=2)))

L1414.define(var='stringguard',
              value=builtin.TypeGuard(sample_instance=''))

L1414.define(var='if',
              value=actors.Actor(env=L1414,
                                 script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                     inner_map={}),
                                                                              serial_id=0,
                                                                              parameters=['test',
                                                                                          'yes',
                                                                                          'no'],
                                                                              selector='true:then:else:')],
                                                      next_serial_id=1)))

L1253.define(var='terminus',
              value=L1251)

L365.define(var='node',
             value=L325)

L365.define(var='guesser',
             value=L363)

L348.define(var='guessernode',
             value=L346)

L348.define(var='animal',
             value=L349)

L802.define(var='mailbox',
             value=L800)

L802.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=())))

L802.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L802),
                                script=L819))

L853._add_result(result=L855,
                  actor=L849)

L856._add_result(result=L114,
                  actor=L849)

L859._add_result(result=L829,
                  actor=L849)

L862._add_result(result=L814,
                  actor=L849)

L864._add_result(result=L805,
                  actor=L849)

L866._add_result(result=L789,
                  actor=L849)

L868._add_result(result=L796,
                  actor=L849)

L871._add_result(result=L832,
                  actor=L849)

L874._add_result(result=L800,
                  actor=L849)

L878._add_result(result='Error: exceptions.TypeError: unbound method __init__() must be called with Actor instance as first argument (got Stamp instance instead)',
                  actor=L849)

L934._add_result(result=L936,
                  actor=L930)

L937._add_result(result=L939,
                  actor=L930)

L941._add_result(result=L754,
                  actor=L930)

L757._add_result(result=L759,
                  actor=L760)

L944._add_result(result=L739,
                  actor=L930)

L946._add_result(result=L728,
                  actor=L930)

L948._add_result(result=L718,
                  actor=L930)

L950._add_result(result=L922,
                  actor=L930)

L953._add_result(result=L761,
                  actor=L930)

L956._add_result(result=L713,
                  actor=L930)

L1099.define(var='mailbox',
              value=L1097)

L1099.define(var='sender',
              value=actors.Actor(env=envs.Env(parent=L1099),
                                 script=L1102))

L1099.define(var='inbox',
              value=builtin.Box(initial_value=builtin.List(elements=())))

L1076.define(var='box',
              value=L770)

L1076.define(var='makemailbox',
              value=L1075)

L1076.define(var='Foo',
              value=L1094)

L1076.define(var='mailbox',
              value=L1097)

L1076.define(var='maildirectory',
              value=L1114)

L1077.define(var='false',
              value=L771)

L1077.define(var='numberguard',
              value=builtin.TypeGuard(sample_instance=0))

L1077.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L1077.define(var='makestamp',
              value=builtin.StampMaker())

L1077.define(var='booleanguard',
              value=builtin.TypeGuard(sample_instance=True))

L1077.define(var='makebox',
              value=L1082)

L1077.define(var='true',
              value=L1083)

L1077.define(var='stringguard',
              value=builtin.TypeGuard(sample_instance=''))

L1077.define(var='if',
              value=actors.Actor(env=L1077,
                                 script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                     inner_map={}),
                                                                              serial_id=0,
                                                                              parameters=['test',
                                                                                          'yes',
                                                                                          'no'],
                                                                              selector='true:then:else:')],
                                                      next_serial_id=1)))

L783.define(var='node',
             value=L329)

L783.define(var='guesser',
             value=L781)

L342.define(var='guessernode',
             value=L340)

L342.define(var='animal',
             value=L343)

L711.define(var='question',
             value=L709)

L651.define(var='mailbox',
             value=L700)

L651.define(var='inbox',
             value=L502)

L651.define(var='sender',
             value=L649)

L652.define(var='box',
             value=L670)

L652.define(var='makemailbox',
             value=L671)

L652.define(var='mailbox',
             value=L685)

L652.define(var='maildirectory',
             value=L695)

L652.define(var='message',
             value=L690)

L652.define(var='Foo',
             value=L697)

L653.define(var='false',
             value=L654)

L653.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L653.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L653.define(var='makestamp',
             value=builtin.StampMaker())

L653.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L653.define(var='makebox',
             value=L664)

L653.define(var='true',
             value=L635)

L653.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L653.define(var='if',
             value=actors.Actor(env=L653,
                                script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0,
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             selector='true:then:else:')],
                                                     next_serial_id=1)))

L242.define(var='query',
             value=L243)

L242.define(var='yesnoquestion',
             value=L240)

L242.define(var='onno',
             value=L211)

L242.define(var='onyes',
             value=L244)

L687.define(var='mailbox',
             value=L685)

L687.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=(L690,))))

L687.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L687),
                                script=L675))

L1296.define(var='makemailbox',
              value=actors.Actor(env=L1296,
                                 script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                                     inner_map={'sender': actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                                                                                                                                       inner_map={}),
                                                                                                                                                                serial_id=0,
                                                                                                                                                                parameters=['message'],
                                                                                                                                                                selector='send:')],
                                                                                                                                        next_serial_id=1),
                                                                                                                'mailbox': actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
                                                                                                                                                                                        inner_map={}),
                                                                                                                                                                 serial_id=0,
                                                                                                                                                                 parameters=[],
                                                                                                                                                                 selector='first'),
                                                                                                                                                   actors.Method(body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                                                                                                                                        inner_map={}),
                                                                                                                                                                 serial_id=1,
                                                                                                                                                                 parameters=[],
                                                                                                                                                                 selector='removefirst'),
                                                                                                                                                   actors.Method(body=actors.Expression(text='sender',
                                                                                                                                                                                        inner_map={}),
                                                                                                                                                                 serial_id=2,
                                                                                                                                                                 parameters=[],
                                                                                                                                                                 selector='sender')],
                                                                                                                                         next_serial_id=3)}),
                                                                              serial_id=0,
                                                                              parameters=[],
                                                                              selector='run')],
                                                      next_serial_id=1)))

L1296.define(var='maildirectory',
              value=builtin.MailDirectory(env=envs.Env(parent=L1297)))

L1297.define(var='false',
              value=builtin.Boolean(value=False,
                                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                                        inner_map={}),
                                                                                 serial_id=0,
                                                                                 parameters=[],
                                                                                 selector='not'),
                                                                   actors.Method(body=actors.Expression(text='falsevalue',
                                                                                                        inner_map={}),
                                                                                 serial_id=1,
                                                                                 parameters=['truevalue',
                                                                                             'falsevalue'],
                                                                                 selector='iftrue:iffalse:')],
                                                         next_serial_id=2)))

L1297.define(var='numberguard',
              value=builtin.TypeGuard(sample_instance=0))

L1297.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L1297.define(var='makestamp',
              value=builtin.StampMaker())

L1297.define(var='booleanguard',
              value=builtin.TypeGuard(sample_instance=True))

L1297.define(var='makebox',
              value=builtin.BoxMaker())

L1297.define(var='true',
              value=builtin.Boolean(value=True,
                                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                                        inner_map={}),
                                                                                 serial_id=0,
                                                                                 parameters=[],
                                                                                 selector='not'),
                                                                   actors.Method(body=actors.Expression(text='truevalue',
                                                                                                        inner_map={}),
                                                                                 serial_id=1,
                                                                                 parameters=['truevalue',
                                                                                             'falsevalue'],
                                                                                 selector='iftrue:iffalse:')],
                                                         next_serial_id=2)))

L1297.define(var='stringguard',
              value=builtin.TypeGuard(sample_instance=''))

L1297.define(var='if',
              value=actors.Actor(env=L1297,
                                 script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                     inner_map={}),
                                                                              serial_id=0,
                                                                              parameters=['test',
                                                                                          'yes',
                                                                                          'no'],
                                                                              selector='true:then:else:')],
                                                      next_serial_id=1)))

L249._add_result(result=L239,
                  actor=L251)

L252._add_result(result=L223,
                  actor=L251)

L254._add_result(result=L256,
                  actor=L251)

L259._add_result(result=L240,
                  actor=L251)

L123.define(var='false',
             value=L124)

L123.define(var='makebox',
             value=L130)

L123.define(var='true',
             value=L131)

L123.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L594.define(var='false',
             value=L513)

L594.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L594.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L594.define(var='makestamp',
             value=builtin.StampMaker())

L594.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L594.define(var='makebox',
             value=L599)

L594.define(var='true',
             value=L600)

L594.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L594.define(var='if',
             value=actors.Actor(env=L594,
                                script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0,
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             selector='true:then:else:')],
                                                     next_serial_id=1)))

L1654._add_result(result=L1648,
                   actor=L1650)

L1656._add_result(result=L1121,
                   actor=L1650)

L1659._add_result(result=L1094,
                   actor=L1650)

L1662._add_result(result=L770,
                   actor=L1650)

L1664._add_result(result=L1083,
                   actor=L1650)

L1666._add_result(result=L771,
                   actor=L1650)

L1668._add_result(result=L1576,
                   actor=L1650)

L1671._add_result(result=L1114,
                   actor=L1650)

L1674._add_result(result=L1097,
                   actor=L1650)

L1678._add_result(result=L1648,
                   actor=L1650)

L1680._add_result(result=L965,
                   actor=L1650)

L593.define(var='box',
             value=L512)

L593.define(var='makemailbox',
             value=L611)

L593.define(var='Foo',
             value=L625)

L593.define(var='maildirectory',
             value=L628)

L593.define(var='mailbox',
             value=L590)

L891._add_result(result=L893,
                  actor=L887)

L894._add_result(result=L896,
                  actor=L887)

L898._add_result(result=L625,
                  actor=L887)

L901._add_result(result=L512,
                  actor=L887)

L903._add_result(result=L600,
                  actor=L887)

L905._add_result(result=L513,
                  actor=L887)

L907._add_result(result=L909,
                  actor=L887)

L912._add_result(result=L628,
                  actor=L887)

L915._add_result(result=L590,
                  actor=L887)

L919._add_result(result=L887,
                  actor=L887)

L981.define(var='box',
             value=L971)

L981.define(var='makemailbox',
             value=L999)

L981.define(var='Foo',
             value=L1013)

L981.define(var='mailbox',
             value=L978)

L981.define(var='maildirectory',
             value=L1016)

L982.define(var='false',
             value=L881)

L982.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L982.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L982.define(var='makestamp',
             value=builtin.StampMaker())

L982.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L982.define(var='makebox',
             value=L987)

L982.define(var='true',
             value=L988)

L982.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L982.define(var='if',
             value=actors.Actor(env=L982,
                                script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0,
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             selector='true:then:else:')],
                                                     next_serial_id=1)))

L1042.define(var='true',
              value=builtin.Boolean(value=True,
                                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                                        inner_map={}),
                                                                                 serial_id=0,
                                                                                 parameters=[],
                                                                                 selector='not'),
                                                                   actors.Method(body=actors.Expression(text='trueaction run',
                                                                                                        inner_map={}),
                                                                                 serial_id=1,
                                                                                 parameters=['trueaction',
                                                                                             'falseaction'],
                                                                                 selector='iftrue:iffalse:')],
                                                         next_serial_id=2)))

L1042.define(var='makestamp',
              value=builtin.StampMaker())

L1042.define(var='false',
              value=builtin.Boolean(value=False,
                                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                                        inner_map={}),
                                                                                 serial_id=0,
                                                                                 parameters=[],
                                                                                 selector='not'),
                                                                   actors.Method(body=actors.Expression(text='falseaction run',
                                                                                                        inner_map={}),
                                                                                 serial_id=1,
                                                                                 parameters=['trueaction',
                                                                                             'falseaction'],
                                                                                 selector='iftrue:iffalse:')],
                                                         next_serial_id=2)))

L1042.define(var='makebox',
              value=builtin.BoxMaker())

L1042.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L370.define(var='node',
             value=L325)

L370.define(var='asker',
             value=L368)

L155.define(var='mailbox',
             value=L153)

L155.define(var='sender',
             value=L156)

L155.define(var='inbox',
             value=L158)

L122.define(var='box',
             value=L138)

L122.define(var='makemailbox',
             value=L139)

L122.define(var='mailbox',
             value=L153)

L122.define(var='maildirectory',
             value=L160)

L122.define(var='message',
             value=L162)

L122.define(var='Foo',
             value=L120)

L122.define(var='tome',
             value=L156)

L263.define(var='mailbox',
             value=L261)

L263.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L263),
                                script=L199))

L263.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=())))

L1685.define(var='node',
              value=L329)

L1685.define(var='asker',
              value=L1683)

L332.define(var='yesbox',
             value=builtin.Box(initial_value=L334))

L332.define(var='askernode',
             value=L330)

L332.define(var='question',
             value=L338)

L332.define(var='nobox',
             value=builtin.Box(initial_value=L340))

L927.define(var='terminus',
             value=L925)

L1263._add_result(result=L1029,
                   actor=L1259)

L1265._add_result(result=L768,
                   actor=L1259)

L1268._add_result(result=L270,
                   actor=L1259)

L1271._add_result(result=L194,
                   actor=L1259)

L1273._add_result(result=L183,
                   actor=L1259)

L1275._add_result(result=L172,
                   actor=L1259)

L1277._add_result(result=L1139,
                   actor=L1259)

L1280._add_result(result=L268,
                   actor=L1259)

L1283._add_result(result=L261,
                   actor=L1259)

L1287._add_result(result=L209,
                   actor=L1259)

L1289._add_result(result=L168,
                   actor=L1259)

L351._add_result(result=L300,
                  actor=L167)

L353._add_result(result=L278,
                  actor=L167)

L355._add_result(result=L305,
                  actor=L167)

L357._add_result(result='Error: No matching method: holding:',
                  actor=L167)

L359._add_result(result=L325,
                  actor=L167)

L361._add_result(result=L363,
                  actor=L167)

L366._add_result(result=L368,
                  actor=L167)

L371._add_result(result=L273,
                  actor=L167)

L1017.define(var='alice',
              value=L1018)

L1582._add_result(result=L1488,
                   actor=L1578)

L1584._add_result(result=L1066,
                   actor=L1578)

L1587._add_result(result=L494,
                   actor=L1578)

L1590._add_result(result=L394,
                   actor=L1578)

L1592._add_result(result=L379,
                   actor=L1578)

L1594._add_result(result=L386,
                   actor=L1578)

L1596._add_result(result=L778,
                   actor=L1578)

L1599._add_result(result=L487,
                   actor=L1578)

L1602._add_result(result=L374,
                   actor=L1578)

L1606._add_result(result=L395,
                   actor=L1578)

L447._add_result(result=L430,
                  actor=L449)

L450._add_result(result=L398,
                  actor=L449)

L452._add_result(result=L397,
                  actor=L449)

L454._add_result(result=L399,
                  actor=L449)

L456._add_result(result=L423,
                  actor=L449)

L458._add_result(result=L431,
                  actor=L449)

L460._add_result(result=L440,
                  actor=L449)

L462._add_result(result=L464,
                  actor=L449)

L465._add_result(result=L467,
                  actor=L449)

L468._add_result(result=L470,
                  actor=L449)

L471._add_result(result='Error: No matching method: show',
                  actor=L449)

L1549.define(var='true',
              value=builtin.Boolean(value=True,
                                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                                        inner_map={}),
                                                                                 serial_id=0,
                                                                                 parameters=[],
                                                                                 selector='not'),
                                                                   actors.Method(body=actors.Expression(text='trueaction run',
                                                                                                        inner_map={}),
                                                                                 serial_id=1,
                                                                                 parameters=['trueaction',
                                                                                             'falseaction'],
                                                                                 selector='iftrue:iffalse:')],
                                                         next_serial_id=2)))

L1549.define(var='makebox',
              value=builtin.BoxMaker())

L1549.define(var='false',
              value=builtin.Boolean(value=False,
                                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                                        inner_map={}),
                                                                                 serial_id=0,
                                                                                 parameters=[],
                                                                                 selector='not'),
                                                                   actors.Method(body=actors.Expression(text='falseaction run',
                                                                                                        inner_map={}),
                                                                                 serial_id=1,
                                                                                 parameters=['trueaction',
                                                                                             'falseaction'],
                                                                                 selector='iftrue:iffalse:')],
                                                         next_serial_id=2)))

L1549.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L1147._add_result(result=L507,
                   actor=L1143)

L1149._add_result(result=L1151,
                   actor=L1143)

L1153._add_result(result=L1013,
                   actor=L1143)

L1156._add_result(result=L971,
                   actor=L1143)

L1158._add_result(result=L988,
                   actor=L1143)

L1160._add_result(result=L881,
                   actor=L1143)

L1162._add_result(result=L1164,
                   actor=L1143)

L1167._add_result(result=L1016,
                   actor=L1143)

L1170._add_result(result=L978,
                   actor=L1143)

L1175._add_result(result=L988,
                   actor=L1143)

L592.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=())))

L592.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L592),
                                script=L615))

L592.define(var='mailbox',
             value=L590)

L72._add_result(result=L74,
                 actor=L3)

L75._add_result(result=L77,
                 actor=L3)

L79._add_result(result=L65,
                 actor=L3)

L82._add_result(result=L29,
                 actor=L3)

L84._add_result(result=L18,
                 actor=L3)

L86._add_result(result=L7,
                 actor=L3)

L88._add_result(result=L90,
                 actor=L3)

L93._add_result(result=L63,
                 actor=L3)

L96._add_result(result=L39,
                 actor=L3)

L100._add_result(result='Error: No matching method: size',
                  actor=L3)

L102._add_result(result=L104,
                  actor=L3)

L105._add_result(result=L30,
                  actor=L3)

L107._add_result(result=L109,
                  actor=L3)

L111._add_result(result=L55,
                  actor=L3)

L1380._add_result(result=L118,
                   actor=L1376)

L1382._add_result(result=L505,
                   actor=L1376)

L1385._add_result(result=L697,
                   actor=L1376)

L1388._add_result(result=L670,
                   actor=L1376)

L1390._add_result(result=L635,
                   actor=L1376)

L1392._add_result(result=L654,
                   actor=L1376)

L1394._add_result(result=L1396,
                   actor=L1376)

L1399._add_result(result=L695,
                   actor=L1376)

L1402._add_result(result=L685,
                   actor=L1376)

L1406._add_result(result=L1131,
                   actor=L1376)

L980.define(var='mailbox',
             value=L978)

L980.define(var='inbox',
             value=L1020)

L980.define(var='sender',
             value=L1018)

L646.define(var='question',
             value=L644)

L258.define(var='box',
             value=L239)

L258.define(var='guess',
             value=L256)

L258.define(var='animal',
             value=L2)

L1372.define(var='question',
              value=L1370)

L376.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=())))

L376.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L376),
                                script=L477))

L376.define(var='mailbox',
             value=L374)

L1498.define(var='false',
              value=builtin.Boolean(value=False,
                                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='true',
                                                                                                        inner_map={}),
                                                                                 serial_id=0,
                                                                                 parameters=[],
                                                                                 selector='not'),
                                                                   actors.Method(body=actors.Expression(text='falseaction run',
                                                                                                        inner_map={}),
                                                                                 serial_id=1,
                                                                                 parameters=['trueaction',
                                                                                             'falseaction'],
                                                                                 selector='iftrue:iffalse:')],
                                                         next_serial_id=2)))

L1498.define(var='makebox',
              value=builtin.BoxMaker())

L1498.define(var='true',
              value=builtin.Boolean(value=True,
                                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='false',
                                                                                                        inner_map={}),
                                                                                 serial_id=0,
                                                                                 parameters=[],
                                                                                 selector='not'),
                                                                   actors.Method(body=actors.Expression(text='trueaction run',
                                                                                                        inner_map={}),
                                                                                 serial_id=1,
                                                                                 parameters=['trueaction',
                                                                                             'falseaction'],
                                                                                 selector='iftrue:iffalse:')],
                                                         next_serial_id=2)))

L1498.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L529.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L529),
                                script=L559))

L529.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=(L576,))))

L529.define(var='mailbox',
             value=L527)

L32.define(var='inbox',
            value=L33)

L32.define(var='sender',
            value=L30)

L32.define(var='mailbox',
            value=L39)

L1519._add_result(result=L1246,
                   actor=L1515)

L1521._add_result(result=L1523,
                   actor=L1515)

L1525._add_result(result=L120,
                   actor=L1515)

L1528._add_result(result=L138,
                   actor=L1515)

L1530._add_result(result=L131,
                   actor=L1515)

L1532._add_result(result=L124,
                   actor=L1515)

L1534._add_result(result=L1068,
                   actor=L1515)

L1537._add_result(result=L160,
                   actor=L1515)

L1540._add_result(result=L153,
                   actor=L1515)

L1544._add_result(result=L156,
                   actor=L1515)

L1546._add_result(result=L1548,
                   actor=L1515)

L1565._add_result(result=L1567,
                   actor=L1515)

L1568._add_result(result='Error: exceptions.ZeroDivisionError: float division',
                   actor=L1515)

L1570._add_result(result='Error: Unbound: makestamp',
                   actor=L1515)

L1696.define(var='node',
              value=L345)

L1696.define(var='guesser',
              value=L1694)

L336.define(var='guessernode',
             value=L334)

L336.define(var='animal',
             value=builtin.String(str='fraidycat'))

L0
root = L0
