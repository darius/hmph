import actors
import builtin
import envs
import registry

L908 = envs.Env(parent=None)
L907 = envs.Env(parent=L908)
L929 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L932 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
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
L925 = actors.Actor(env=L907,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L929,
                                                                                                   'mailbox': L932}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L1445 = actors.ActorEditor(editable=True,
                           actor=L925)
L25 = envs.Env(parent=None)
L24 = envs.Env(parent=L25)
L50 = envs.Env(parent=L24)
L62 = envs.Env(parent=L50)
L106 = envs.Env(parent=L62)
L105 = envs.Env(parent=L106)
L1270 = envs.Env(parent=L105)
L69 = actors.Script(elements=[actors.Method(body=actors.Expression(text='question',
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
L1268 = actors.Actor(env=envs.Env(parent=L1270),
                     script=L69)
L1267 = actors.ActorEditor(editable=True,
                           actor=L1268)
L777 = builtin.Box(initial_value=builtin.List(elements=()))
L1746 = actors.ActorEditor(editable=False,
                           actor=L777)
L23 = envs.Env(parent=L24)
L178 = envs.Env(parent=L23)
L209 = envs.Env(parent=L178)
L208 = envs.Env(parent=L209)
L962 = envs.Env(parent=L208)
L187 = actors.Script(elements=[actors.Text(body="I'm out of guesses about your animal.  Please tell me its name and a new question I can ask, so that your animal has a yes answer.  Thanks!",
                                           serial_id=0),
                               actors.Method(body=actors.Expression(text="box <- (makequestion asking: question ifyes: (makeguess name: animal parent: box) ifno: (box get)).\r\n'OK!'\r\n",
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=['animal',
                                                         'question'],
                                             selector='name:question:')],
                     next_serial_id=2)
L960 = actors.Actor(env=envs.Env(parent=L962),
                    script=L187)
L959 = actors.ActorEditor(editable=True,
                          actor=L960)
L1083 = builtin.List(elements=(builtin.String(str='hello'),))
L1728 = actors.ActorEditor(editable=False,
                           actor=L1083)
L487 = builtin.BoxMaker()
L1039 = actors.ActorEditor(editable=False,
                           actor=L487)
L312 = envs.Env(parent=None)
L311 = envs.Env(parent=L312)
L357 = envs.Env(parent=L311)
L343 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
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
L355 = actors.Actor(env=envs.Env(parent=L357),
                    script=L343)
L1466 = actors.ActorEditor(editable=True,
                           actor=L355)
L26 = builtin.Boolean(value=False,
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
L48 = builtin.Box(initial_value=L26)
L1742 = actors.ActorEditor(editable=False,
                           actor=L48)
L110 = envs.Env(parent=L62)
L109 = envs.Env(parent=L110)
L66 = actors.Script(elements=[actors.Method(body=actors.Expression(text='make asker',
                                                                   inner_map={'asker': L69}),
                                            serial_id=0,
                                            parameters=['node'],
                                            selector='on:')],
                    next_serial_id=1)
L108 = actors.Actor(env=L109,
                    script=L66)
L107 = builtin.Box(initial_value=L108)
L846 = actors.ActorEditor(editable=False,
                          actor=L107)
L308 = builtin.BoxMaker()
L307 = actors.ActorEditor(editable=False,
                          actor=L308)
L988 = builtin.List(elements=(builtin.String(str='hello'),))
L987 = actors.ActorEditor(editable=False,
                          actor=L988)
L37 = builtin.Boolean(value=True,
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
L1036 = actors.ActorEditor(editable=False,
                           actor=L37)
L600 = builtin.Boolean(value=True,
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
L1753 = actors.ActorEditor(editable=False,
                           actor=L600)
L742 = envs.Env(parent=None)
L741 = envs.Env(parent=L742)
L774 = envs.Env(parent=L741)
L762 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L775 = actors.Actor(env=envs.Env(parent=L774),
                    script=L762)
L1397 = actors.ActorEditor(editable=True,
                           actor=L775)
L783 = actors.Script(elements=[actors.Text(body='Hi me, how are me?\r\n',
                                           serial_id=0)],
                     next_serial_id=1)
L781 = actors.Actor(env=envs.Env(parent=L741),
                    script=L783)
L1266 = actors.ActorEditor(editable=True,
                           actor=L781)
L532 = builtin.Boolean(value=True,
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
L1402 = actors.ActorEditor(editable=False,
                           actor=L532)
L1026 = builtin.String(str='Thanks, I will remember.')
L1025 = actors.ActorEditor(editable=False,
                           actor=L1026)
L1312 = builtin.String(str='Is it a cat?')
L1311 = actors.ActorEditor(editable=False,
                           actor=L1312)
L116 = builtin.String(str='Is it easily frightened?')
L1737 = actors.ActorEditor(editable=False,
                           actor=L116)
L558 = builtin.List(elements=())
L557 = builtin.Box(initial_value=L558)
L1320 = actors.ActorEditor(editable=False,
                           actor=L557)
L858 = builtin.Number(n=25.0)
L1260 = actors.ActorEditor(editable=False,
                           actor=L858)
L1046 = builtin.Boolean(value=True,
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
L1045 = actors.ActorEditor(editable=False,
                           actor=L1046)
L1646 = builtin.List(elements=(builtin.String(str='hello'),))
L1735 = actors.ActorEditor(editable=False,
                           actor=L1646)
L422 = builtin.BoxMaker()
L1393 = actors.ActorEditor(editable=False,
                           actor=L422)
L241 = envs.Env(parent=None)
L240 = envs.Env(parent=L241)
L281 = envs.Env(parent=L240)
L272 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
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
L279 = actors.Actor(env=envs.Env(parent=L281),
                    script=L272)
L1738 = actors.ActorEditor(editable=True,
                           actor=L279)
L1056 = builtin.String(str='Is it a dog?')
L1055 = actors.ActorEditor(editable=False,
                           actor=L1056)
L1053 = builtin.String(str='Is it a dog?')
L1052 = actors.ActorEditor(editable=False,
                           actor=L1053)
L417 = envs.Env(parent=None)
L416 = envs.Env(parent=L417)
L853 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                   inner_map={}),
                      serial_id=1)
L856 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                   inner_map={}),
                      serial_id=2)
L467 = actors.Script(elements=[],
                     next_serial_id=0)
L860 = actors.Example(expression=actors.Expression(text='make Foo',
                                                   inner_map={'Foo': L467}),
                      serial_id=4)
L863 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                   inner_map={}),
                      serial_id=6)
L865 = actors.Example(expression=actors.Expression(text='box get',
                                                   inner_map={}),
                      serial_id=7)
L867 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                   inner_map={}),
                      serial_id=8)
L869 = actors.Example(expression=actors.Expression(text="['hello']",
                                                   inner_map={}),
                      serial_id=9)
L874 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                   inner_map={}),
                      serial_id=11)
L877 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                   inner_map={}),
                      serial_id=13)
L442 = actors.Script(elements=[actors.Text(body='Hi - time to vote on where to go out for lunch.  Pick a method for the restaurant you like and click it.',
                                           serial_id=0),
                               actors.Method(body=actors.Expression(text='',
                                                                    inner_map={}),
                                             serial_id=1,
                                             parameters=[],
                                             selector='voteforstarbucks')],
                     next_serial_id=2)
L881 = actors.Example(expression=actors.Expression(text='mailbox sender send: make message',
                                                   inner_map={'message': L442}),
                      serial_id=16)
L885 = actors.Example(expression=actors.Expression(text='makek makeballot',
                                                   inner_map={}),
                      serial_id=17)
L460 = actors.Script(elements=[actors.Method(body=actors.Expression(text='let ballotbox = makebox holding: 0',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='run')],
                     next_serial_id=1)
L887 = actors.Example(expression=actors.Expression(text='make makeballot',
                                                   inner_map={'makeballot': L460}),
                      serial_id=18)
L850 = actors.Actor(env=L416,
                    script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                               serial_id=0),
                                                   L853,
                                                   L856,
                                                   actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                               serial_id=3),
                                                   L860,
                                                   actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                               serial_id=5),
                                                   L863,
                                                   L865,
                                                   L867,
                                                   L869,
                                                   actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                               serial_id=10),
                                                   L874,
                                                   actors.Text(body='You can create your own mailbox:',
                                                               serial_id=12),
                                                   L877,
                                                   actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                               serial_id=14),
                                                   actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                               serial_id=15),
                                                   L881,
                                                   L885,
                                                   L887],
                                         next_serial_id=19))
L849 = actors.ActorEditor(editable=True,
                          actor=L850)
L1167 = envs.Env(parent=L208)
L1165 = actors.Actor(env=envs.Env(parent=L1167),
                     script=L187)
L1164 = actors.ActorEditor(editable=True,
                           actor=L1165)
L520 = envs.Env(parent=None)
L519 = envs.Env(parent=L520)
L546 = actors.Script(elements=[],
                     next_serial_id=0)
L544 = actors.Actor(env=envs.Env(parent=L519),
                    script=L546)
L1566 = actors.ActorEditor(editable=True,
                           actor=L544)
L340 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L336 = actors.Actor(env=L311,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L340,
                                                                                                   'mailbox': L343}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L1054 = actors.ActorEditor(editable=True,
                           actor=L336)
L84 = envs.Env(parent=L50)
L120 = envs.Env(parent=L84)
L119 = envs.Env(parent=L120)
L99 = actors.Script(elements=[actors.Text(body="I'm out of ideas about your animal -- please tell me its name and a question to ask in the future, such that yes is the right answer for it.",
                                          serial_id=0),
                              actors.Method(body=actors.Expression(text="node <- (makebranch on: question ifyes: (makebox holding: (makeguess for: animal)) ifno: (makebox holding: guessernode)).\r\n'Thanks, I will remember.'",
                                                                   inner_map={}),
                                            serial_id=2,
                                            parameters=['animal',
                                                        'question'],
                                            selector='name:question:')],
                    next_serial_id=3)
L92 = actors.Script(elements=[actors.Method(body=actors.Expression(text="'Is it a ' + animal + '?'",
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
                                                                   inner_map={'terminus': L99}),
                                            serial_id=2,
                                            parameters=[],
                                            selector='no')],
                    next_serial_id=3)
L89 = actors.Script(elements=[actors.Method(body=actors.Expression(text='make guesser',
                                                                   inner_map={'guesser': L92}),
                                            serial_id=0,
                                            parameters=['node'],
                                            selector='on:')],
                    next_serial_id=1)
L118 = actors.Actor(env=L119,
                    script=L89)
L1259 = actors.ActorEditor(editable=True,
                           actor=L118)
L614 = builtin.Stamp()
L615 = builtin.StampGuard(stamp=L614)
L613 = builtin.List(elements=(L614,
                              L615))
L1263 = actors.ActorEditor(editable=False,
                           actor=L613)
L235 = builtin.String(str='hello world!hello world!')
L234 = actors.ActorEditor(editable=False,
                          actor=L235)
L1586 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1589 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L224 = actors.Script(elements=[],
                     next_serial_id=0)
L1592 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L224}),
                       serial_id=4)
L1595 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1597 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1599 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1601 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1604 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1607 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L168 = actors.Example(expression=actors.Expression(text='let gamebox = makebox holding: 0',
                                                   inner_map={}),
                      serial_id=1)
L180 = actors.Script(elements=[actors.Method(body=actors.Expression(text="'Is it a ' + animal + '?'\r\n",
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
                                                                    inner_map={'question': L187}),
                                             serial_id=2,
                                             parameters=[],
                                             selector='no')],
                     next_serial_id=3)
L201 = actors.Script(elements=[actors.Method(body=actors.Expression(text='make guess\r\n',
                                                                    inner_map={'guess': L180}),
                                             serial_id=0,
                                             parameters=['animal',
                                                         'box'],
                                             selector='name:parent:')],
                     next_serial_id=1)
L199 = actors.Example(expression=actors.Expression(text='make makeguess',
                                                   inner_map={'makeguess': L201}),
                      serial_id=2)
L205 = actors.Example(expression=actors.Expression(text="makeguess name: 'dog' parent: gamebox",
                                                   inner_map={}),
                      serial_id=3)
L211 = actors.Example(expression=actors.Expression(text='gamebox get',
                                                   inner_map={}),
                      serial_id=4)
L167 = actors.Script(elements=[L168,
                               L199,
                               L205,
                               L211],
                     next_serial_id=5)
L1611 = actors.Example(expression=actors.Expression(text='make animalgame',
                                                    inner_map={'animalgame': L167}),
                       serial_id=16)
L58 = actors.Script(elements=[actors.Method(body=actors.Expression(text='(box get) on: box',
                                                                   inner_map={}),
                                            serial_id=0,
                                            parameters=['box'],
                                            selector='on:')],
                    next_serial_id=1)
L129 = actors.Example(expression=actors.Expression(text='make call',
                                                   inner_map={'call': L58}),
                      serial_id=0)
L76 = actors.Script(elements=[actors.Method(body=actors.Expression(text='question',
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
L63 = actors.Script(elements=[actors.Method(body=actors.Expression(text='make askernode\r\n',
                                                                   inner_map={'askernode': L66,
                                                                              'asker': L76}),
                                            serial_id=0,
                                            parameters=['question',
                                                        'yesbox',
                                                        'nobox'],
                                            selector='on:ifyes:ifno:')],
                    next_serial_id=1)
L132 = actors.Example(expression=actors.Expression(text='make makebranch',
                                                   inner_map={'makebranch': L63}),
                      serial_id=1)
L88 = actors.Script(elements=[],
                    next_serial_id=0)
L85 = actors.Script(elements=[actors.Method(body=actors.Expression(text='make guessernode',
                                                                   inner_map={'guesser': L88,
                                                                              'guessernode': L89}),
                                            serial_id=0,
                                            parameters=['animal'],
                                            selector='for:')],
                    next_serial_id=1)
L134 = actors.Example(expression=actors.Expression(text='make makeguess',
                                                   inner_map={'makeguess': L85}),
                      serial_id=2)
L136 = actors.Example(expression=actors.Expression(text="let root = box holding: (makeguess for: 'dog')",
                                                   inner_map={}),
                      serial_id=3)
L138 = actors.Example(expression=actors.Expression(text="let root = makebox holding: (makeguess for: 'dog')",
                                                   inner_map={}),
                      serial_id=4)
L140 = actors.Example(expression=actors.Expression(text='call on: root',
                                                   inner_map={}),
                      serial_id=6)
L145 = actors.Example(expression=actors.Expression(text='call on: root',
                                                   inner_map={}),
                      serial_id=7)
L53 = actors.Script(elements=[actors.Method(body=actors.Expression(text='call on: root',
                                                                   inner_map={}),
                                            serial_id=0,
                                            parameters=[],
                                            selector='run')],
                    next_serial_id=1)
L150 = actors.Example(expression=actors.Expression(text='make playgame',
                                                   inner_map={'playgame': L53}),
                      serial_id=8)
L128 = actors.Script(elements=[L129,
                               L132,
                               L134,
                               L136,
                               L138,
                               L140,
                               L145,
                               L150],
                     next_serial_id=9)
L1613 = actors.Example(expression=actors.Expression(text='make newanimalgame',
                                                    inner_map={'newanimalgame': L128}),
                       serial_id=17)
L1583 = actors.Actor(env=L24,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1586,
                                                    L1589,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1592,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1595,
                                                    L1597,
                                                    L1599,
                                                    L1601,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1604,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1607,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1611,
                                                    L1613],
                                          next_serial_id=18))
L1582 = actors.ActorEditor(editable=True,
                           actor=L1583)
L1317 = builtin.String(str='hello world!')
L1316 = actors.ActorEditor(editable=False,
                           actor=L1317)
L405 = builtin.Boolean(value=True,
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
L404 = actors.ActorEditor(editable=False,
                          actor=L405)
L383 = builtin.String(str='hello')
L382 = builtin.List(elements=(L383,))
L1399 = actors.ActorEditor(editable=False,
                           actor=L382)
L210 = builtin.String(str='dog')
L1409 = actors.ActorEditor(editable=False,
                           actor=L210)
L476 = envs.Env(parent=None)
L475 = envs.Env(parent=L476)
L510 = actors.Script(elements=[],
                     next_serial_id=0)
L508 = actors.Actor(env=envs.Env(parent=L475),
                    script=L510)
L994 = actors.ActorEditor(editable=True,
                          actor=L508)
L750 = builtin.Boolean(value=False,
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
L967 = actors.ActorEditor(editable=False,
                          actor=L750)
L104 = actors.Actor(env=L105,
                    script=L66)
L103 = builtin.Box(initial_value=L104)
L1544 = actors.ActorEditor(editable=False,
                           actor=L103)
L51 = actors.Actor(env=envs.Env(parent=L50),
                   script=L53)
L1745 = actors.ActorEditor(editable=True,
                           actor=L51)
L252 = builtin.BoxMaker()
L1313 = actors.ActorEditor(editable=False,
                           actor=L252)
L1033 = builtin.Number(n=6.0)
L1032 = actors.ActorEditor(editable=False,
                           actor=L1033)
L294 = builtin.Box(initial_value=builtin.List(elements=()))
L1380 = actors.ActorEditor(editable=False,
                           actor=L294)
L599 = builtin.StampMaker()
L1734 = actors.ActorEditor(editable=False,
                           actor=L599)
L448 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L451 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
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
L415 = actors.Actor(env=L416,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L448,
                                                                                                   'mailbox': L451}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L414 = actors.ActorEditor(editable=True,
                          actor=L415)
L823 = envs.Env(parent=None)
L822 = actors.Actor(env=L823,
                    script=actors.Script(elements=[],
                                         next_serial_id=0))
L1168 = actors.ActorEditor(editable=True,
                           actor=L822)
L965 = builtin.String(str='Is it a dog?')
L964 = actors.ActorEditor(editable=False,
                          actor=L965)
L581 = builtin.Boolean(value=False,
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
L580 = builtin.Box(initial_value=L581)
L579 = actors.ActorEditor(editable=False,
                          actor=L580)
L1283 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1285 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1289 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L510}),
                       serial_id=4)
L1292 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1294 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1296 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1298 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1301 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1304 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1309 = actors.Example(expression=actors.Expression(text="maildirectory at: 'alice' put: mailbox sender",
                                                    inner_map={}),
                       serial_id=17)
L1280 = actors.Actor(env=L475,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1283,
                                                    L1285,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1289,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1292,
                                                    L1294,
                                                    L1296,
                                                    L1298,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1301,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1304,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    actors.Text(body="maildirectory at: 'alice' put: mailbox sender",
                                                                serial_id=16),
                                                    L1309],
                                          next_serial_id=18))
L1279 = actors.ActorEditor(editable=True,
                           actor=L1280)
L727 = builtin.Boolean(value=False,
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
L1323 = actors.ActorEditor(editable=False,
                           actor=L727)
L592 = envs.Env(parent=None)
L591 = envs.Env(parent=L592)
L688 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L691 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
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
L684 = actors.Actor(env=L591,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L688,
                                                                                                   'mailbox': L691}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L1580 = actors.ActorEditor(editable=True,
                           actor=L684)
L122 = builtin.String(str='Does it meow?')
L1030 = actors.ActorEditor(editable=False,
                           actor=L122)
L787 = actors.Script(elements=[],
                     next_serial_id=0)
L785 = actors.Actor(env=envs.Env(parent=L741),
                    script=L787)
L1396 = actors.ActorEditor(editable=True,
                           actor=L785)
L18 = builtin.BoxMaker()
L966 = actors.ActorEditor(editable=False,
                          actor=L18)
L4 = envs.Env(parent=None)
L2 = builtin.MailDirectory(env=envs.Env(parent=L4))
L1 = actors.ActorEditor(editable=False,
                        actor=L2)
L49 = actors.Actor(env=L50,
                   script=L128)
L131 = actors.ActorEditor(editable=True,
                          actor=L49)
L1099 = envs.Env(parent=None)
L1098 = envs.Env(parent=L1099)
L1097 = actors.Actor(env=L1098,
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
L1096 = actors.ActorEditor(editable=True,
                           actor=L1097)
L893 = envs.Env(parent=None)
L1184 = envs.Env(parent=L893)
L1183 = envs.Env(parent=L1184)
L1189 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                     inner_map={}),
                                              serial_id=0,
                                              parameters=['message'],
                                              selector='send:')],
                      next_serial_id=1)
L1181 = actors.Actor(env=envs.Env(parent=L1183),
                     script=L1189)
L1180 = actors.ActorEditor(editable=True,
                           actor=L1181)
L998 = envs.Env(parent=L4)
L1021 = actors.Script(elements=[],
                      next_serial_id=0)
L996 = actors.Actor(env=envs.Env(parent=L998),
                    script=L1021)
L995 = actors.ActorEditor(editable=True,
                          actor=L996)
L590 = envs.Env(parent=L591)
L1577 = actors.Script(elements=[],
                      next_serial_id=0)
L1575 = actors.Actor(env=envs.Env(parent=L590),
                     script=L1577)
L1574 = actors.ActorEditor(editable=True,
                           actor=L1575)
L239 = envs.Env(parent=L240)
L269 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L296 = actors.Actor(env=envs.Env(parent=L239),
                    script=L269)
L738 = actors.ActorEditor(editable=True,
                          actor=L296)
L313 = builtin.Boolean(value=False,
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
L335 = builtin.Box(initial_value=L313)
L717 = actors.ActorEditor(editable=False,
                          actor=L335)
L1276 = envs.Env(parent=L119)
L1275 = envs.Env(parent=L1276)
L1277 = actors.Actor(env=L1275,
                     script=L92)
L1618 = actors.ActorEditor(editable=True,
                           actor=L1277)
L790 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                   inner_map={}),
                      serial_id=1)
L793 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                   inner_map={}),
                      serial_id=2)
L797 = actors.Example(expression=actors.Expression(text='make Foo',
                                                   inner_map={'Foo': L787}),
                      serial_id=4)
L800 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                   inner_map={}),
                      serial_id=6)
L802 = actors.Example(expression=actors.Expression(text='box get',
                                                   inner_map={}),
                      serial_id=7)
L804 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                   inner_map={}),
                      serial_id=8)
L806 = actors.Example(expression=actors.Expression(text="['hello']",
                                                   inner_map={}),
                      serial_id=9)
L811 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                   inner_map={}),
                      serial_id=11)
L814 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                   inner_map={}),
                      serial_id=13)
L818 = actors.Example(expression=actors.Expression(text='let tome = mailbox sender',
                                                   inner_map={}),
                      serial_id=16)
L820 = actors.Example(expression=actors.Expression(text='tome send: make message',
                                                   inner_map={'message': L783}),
                      serial_id=17)
L839 = actors.Example(expression=actors.Expression(text='2 * 3',
                                                   inner_map={}),
                      serial_id=18)
L842 = actors.Example(expression=actors.Expression(text='2 / 0',
                                                   inner_map={}),
                      serial_id=19)
L844 = actors.Example(expression=actors.Expression(text='let pair = makestamp run',
                                                   inner_map={}),
                      serial_id=20)
L740 = actors.Actor(env=L741,
                    script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                               serial_id=0),
                                                   L790,
                                                   L793,
                                                   actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                               serial_id=3),
                                                   L797,
                                                   actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                               serial_id=5),
                                                   L800,
                                                   L802,
                                                   L804,
                                                   L806,
                                                   actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                               serial_id=10),
                                                   L811,
                                                   actors.Text(body='You can create your own mailbox:',
                                                               serial_id=12),
                                                   L814,
                                                   actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                               serial_id=14),
                                                   actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                               serial_id=15),
                                                   L818,
                                                   L820,
                                                   L839,
                                                   L842,
                                                   L844],
                                         next_serial_id=21))
L739 = actors.ActorEditor(editable=True,
                          actor=L740)
L1336 = envs.Env(parent=None)
L1368 = builtin.MailDirectory(env=envs.Env(parent=L1336))
L1563 = actors.ActorEditor(editable=False,
                           actor=L1368)
L22 = envs.Env(parent=L23)
L1550 = envs.Env(parent=L22)
L1553 = actors.Script(elements=[],
                      next_serial_id=0)
L1548 = actors.Actor(env=envs.Env(parent=L1550),
                     script=L1553)
L1547 = actors.ActorEditor(editable=True,
                           actor=L1548)
L1215 = actors.Script(elements=[actors.Method(body=actors.Expression(text="'Hello, Alex! How are you?'",
                                                                     inner_map={}),
                                              serial_id=0,
                                              parameters=[],
                                              selector='greet')],
                      next_serial_id=1)
L1213 = actors.Actor(env=envs.Env(parent=L1184),
                     script=L1215)
L1467 = actors.ActorEditor(editable=True,
                           actor=L1213)
L498 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L501 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
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
L494 = actors.Actor(env=L475,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L498,
                                                                                                   'mailbox': L501}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L1567 = actors.ActorEditor(editable=True,
                           actor=L494)
L678 = builtin.String(str='<blockquote></blockquote>')
L1319 = actors.ActorEditor(editable=False,
                           actor=L678)
L324 = builtin.Boolean(value=True,
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
L1446 = actors.ActorEditor(editable=False,
                           actor=L324)
L1471 = actors.ActorEditor(editable=False,
                           actor=L615)
L593 = builtin.Boolean(value=False,
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
L608 = builtin.Box(initial_value=L593)
L1318 = actors.ActorEditor(editable=False,
                           actor=L608)
L1274 = envs.Env(parent=L1275)
L1272 = actors.Actor(env=envs.Env(parent=L1274),
                     script=L99)
L1271 = actors.ActorEditor(editable=True,
                           actor=L1272)
L398 = builtin.Boolean(value=False,
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
L434 = builtin.Box(initial_value=L398)
L574 = actors.ActorEditor(editable=False,
                          actor=L434)
L289 = builtin.MailDirectory(env=envs.Env(parent=L241))
L1392 = actors.ActorEditor(editable=False,
                           actor=L289)
L174 = builtin.String(str='Does it meow?')
L1740 = actors.ActorEditor(editable=False,
                           actor=L174)
L808 = builtin.List(elements=(builtin.String(str='hello'),))
L1322 = actors.ActorEditor(editable=False,
                           actor=L808)
L649 = actors.Script(elements=[actors.Method(body=actors.Expression(text="markup lonetag: 'p'",
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
L654 = actors.Actor(env=envs.Env(parent=L590),
                    script=L649)
L718 = actors.ActorEditor(editable=True,
                          actor=L654)
L1765 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1767 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1770 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L1215}),
                       serial_id=4)
L1773 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1775 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1777 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1779 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1782 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1785 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1789 = actors.Example(expression=actors.Expression(text="'hello alex' size",
                                                    inner_map={}),
                       serial_id=16)
L1791 = actors.Example(expression=actors.Expression(text="'hello alex' length",
                                                    inner_map={}),
                       serial_id=17)
L1793 = actors.Example(expression=actors.Expression(text='let sender = mailbox sender',
                                                    inner_map={}),
                       serial_id=18)
L1211 = actors.Script(elements=[actors.Text(body='Hi, there.  ',
                                            serial_id=0)],
                      next_serial_id=1)
L1795 = actors.Example(expression=actors.Expression(text='sender send: make message',
                                                    inner_map={'message': L1211}),
                       serial_id=19)
L1206 = actors.Script(elements=[actors.Method(body=actors.Expression(text='votesformcdonalds <- (votesformcdonalds get + 1)',
                                                                     inner_map={}),
                                              serial_id=0,
                                              parameters=[],
                                              selector='votemcdonalds')],
                      next_serial_id=1)
L1203 = actors.Script(elements=[actors.Method(body=actors.Expression(text='let votesformcdonalds = makebox holding: 0.\r\nmake ballot',
                                                                     inner_map={'ballot': L1206}),
                                              serial_id=0,
                                              parameters=[],
                                              selector='run')],
                      next_serial_id=1)
L1797 = actors.Example(expression=actors.Expression(text='make makeballot',
                                                    inner_map={'makeballot': L1203}),
                       serial_id=20)
L1762 = actors.Actor(env=L1184,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1765,
                                                    L1767,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1770,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1773,
                                                    L1775,
                                                    L1777,
                                                    L1779,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1782,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1785,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1789,
                                                    L1791,
                                                    L1793,
                                                    L1795,
                                                    L1797],
                                          next_serial_id=21))
L1761 = actors.ActorEditor(editable=True,
                           actor=L1762)
L1736 = actors.ActorEditor(editable=False,
                           actor=L313)
L293 = actors.Script(elements=[],
                     next_serial_id=0)
L291 = actors.Actor(env=envs.Env(parent=L240),
                    script=L293)
L1579 = actors.ActorEditor(editable=True,
                           actor=L291)
L1508 = builtin.Number(n=25.0)
L1507 = actors.ActorEditor(editable=False,
                           actor=L1508)
L723 = builtin.List(elements=(builtin.String(str='hello'),))
L722 = actors.ActorEditor(editable=False,
                          actor=L723)
L477 = builtin.Boolean(value=False,
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
L493 = builtin.Box(initial_value=L477)
L736 = actors.ActorEditor(editable=False,
                          actor=L493)
L126 = envs.Env(parent=L84)
L125 = envs.Env(parent=L126)
L144 = envs.Env(parent=L125)
L143 = envs.Env(parent=L144)
L142 = actors.Actor(env=L143,
                    script=L92)
L1511 = actors.ActorEditor(editable=True,
                           actor=L142)
L1510 = actors.ActorEditor(editable=False,
                           actor=L593)
L465 = actors.Actor(env=envs.Env(parent=L416),
                    script=L467)
L1744 = actors.ActorEditor(editable=True,
                           actor=L465)
L1661 = envs.Env(parent=None)
L1660 = envs.Env(parent=L1661)
L1659 = actors.Actor(env=L1660,
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
L1658 = actors.ActorEditor(editable=True,
                           actor=L1659)
L1733 = builtin.String(str='<p/>')
L1732 = actors.ActorEditor(editable=False,
                           actor=L1733)
L474 = envs.Env(parent=L475)
L472 = actors.Actor(env=envs.Env(parent=L474),
                    script=L501)
L471 = actors.ActorEditor(editable=True,
                          actor=L472)
L551 = envs.Env(parent=L519)
L559 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
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
L549 = actors.Actor(env=envs.Env(parent=L551),
                    script=L559)
L575 = actors.ActorEditor(editable=True,
                          actor=L549)
L396 = builtin.Number(n=40.0)
L1261 = actors.ActorEditor(editable=False,
                           actor=L396)
L1042 = builtin.BoxMaker()
L1041 = actors.ActorEditor(editable=False,
                           actor=L1042)
L721 = builtin.Number(n=5.0)
L720 = actors.ActorEditor(editable=False,
                          actor=L721)
L1480 = builtin.Number(n=25.0)
L1731 = actors.ActorEditor(editable=False,
                           actor=L1480)
L570 = builtin.List(elements=(builtin.String(str='hello'),))
L569 = actors.ActorEditor(editable=False,
                          actor=L570)
L1335 = envs.Env(parent=L1336)
L1351 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                     inner_map={}),
                                              serial_id=0,
                                              parameters=['message'],
                                              selector='send:')],
                      next_serial_id=1)
L1354 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
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
L1347 = actors.Actor(env=L1335,
                     script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                         inner_map={'sender': L1351,
                                                                                                    'mailbox': L1354}),
                                                                  serial_id=0,
                                                                  parameters=[],
                                                                  selector='run')],
                                          next_serial_id=1))
L1750 = actors.ActorEditor(editable=True,
                           actor=L1347)
L945 = builtin.MailDirectory(env=envs.Env(parent=L908))
L1040 = actors.ActorEditor(editable=False,
                           actor=L945)
L242 = builtin.Boolean(value=False,
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
L264 = builtin.Box(initial_value=L242)
L1057 = actors.ActorEditor(editable=False,
                           actor=L264)
L891 = builtin.MailDirectory(env=envs.Env(parent=L893))
L890 = actors.ActorEditor(editable=False,
                          actor=L891)
L749 = builtin.BoxMaker()
L1395 = actors.ActorEditor(editable=False,
                           actor=L749)
L299 = builtin.Boolean(value=True,
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
L298 = actors.ActorEditor(editable=False,
                          actor=L299)
L232 = builtin.Stamp()
L707 = actors.StampedActor(stamp=L232,
                           actor=builtin.String(str='hello'))
L1568 = actors.ActorEditor(editable=False,
                           actor=L707)
L1588 = builtin.Number(n=5.0)
L1730 = actors.ActorEditor(editable=False,
                           actor=L1588)
L1758 = envs.Env(parent=L125)
L1756 = actors.Actor(env=envs.Env(parent=L1758),
                     script=L92)
L1755 = actors.ActorEditor(editable=True,
                           actor=L1756)
L906 = envs.Env(parent=L907)
L904 = actors.Actor(env=envs.Env(parent=L906),
                    script=L932)
L903 = actors.ActorEditor(editable=True,
                          actor=L904)
L554 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L518 = actors.Actor(env=L519,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L554,
                                                                                                   'mailbox': L559}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L517 = actors.ActorEditor(editable=True,
                          actor=L518)
L222 = actors.Actor(env=envs.Env(parent=L24),
                    script=L224)
L1545 = actors.ActorEditor(editable=True,
                           actor=L222)
L1067 = builtin.Number(n=5.0)
L1542 = actors.ActorEditor(editable=False,
                           actor=L1067)
L1570 = builtin.List(elements=())
L1569 = actors.ActorEditor(editable=False,
                           actor=L1570)
L5 = builtin.Boolean(value=False,
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
L999 = builtin.Box(initial_value=L5)
L1729 = actors.ActorEditor(editable=False,
                           actor=L999)
L991 = builtin.Number(n=29.0)
L990 = actors.ActorEditor(editable=False,
                          actor=L991)
L1327 = actors.ActorEditor(editable=False,
                           actor=L242)
L124 = actors.Actor(env=L125,
                    script=L89)
L123 = builtin.Box(initial_value=L124)
L1623 = actors.ActorEditor(editable=False,
                           actor=L123)
L177 = envs.Env(parent=L178)
L176 = envs.Env(parent=L177)
L175 = actors.Actor(env=L176,
                    script=L180)
L1624 = actors.ActorEditor(editable=True,
                           actor=L175)
L1209 = actors.Actor(env=envs.Env(parent=L1184),
                     script=L1211)
L1385 = actors.ActorEditor(editable=True,
                           actor=L1209)
L1173 = builtin.Boolean(value=False,
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
L1172 = actors.ActorEditor(editable=False,
                           actor=L1173)
L1387 = builtin.Number(n=5.0)
L1386 = actors.ActorEditor(editable=False,
                           actor=L1387)
L1060 = actors.ActorEditor(editable=False,
                           actor=L5)
L792 = builtin.Number(n=5.0)
L963 = actors.ActorEditor(editable=False,
                          actor=L792)
L735 = builtin.String(str='<p>')
L734 = actors.ActorEditor(editable=False,
                          actor=L735)
L149 = envs.Env(parent=L105)
L147 = actors.Actor(env=envs.Env(parent=L149),
                    script=L69)
L1620 = actors.ActorEditor(editable=True,
                           actor=L147)
L1416 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1419 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L711 = actors.Script(elements=[],
                     next_serial_id=0)
L1422 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L711}),
                       serial_id=4)
L1425 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1427 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1429 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1431 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1436 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1439 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L611 = actors.Example(expression=actors.Expression(text='let stamppair = makestamp run',
                                                   inner_map={}),
                      serial_id=0)
L617 = actors.Example(expression=actors.Expression(text='let htmlstamp = stamppair at: 1',
                                                   inner_map={}),
                      serial_id=1)
L619 = actors.Example(expression=actors.Expression(text='let htmlguard = stamppair at: 2',
                                                   inner_map={}),
                      serial_id=2)
L626 = actors.Script(elements=[actors.Method(body=actors.Expression(text="'<' + tag + (attributes foldr: showattr initially: '>')",
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='show')],
                     next_serial_id=1)
L634 = actors.Script(elements=[actors.Method(body=actors.Expression(text="'<' + tag + (attributes foldr: showattr initially: '>') + \r\n  (elements foldr: showattr initially: '') + \r\n  '</' + tag + '>'",
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='show')],
                     next_serial_id=1)
L641 = actors.Script(elements=[],
                     next_serial_id=0)
L642 = actors.Script(elements=[],
                     next_serial_id=0)
L643 = actors.Script(elements=[],
                     next_serial_id=0)
L644 = actors.Script(elements=[],
                     next_serial_id=0)
L623 = actors.Script(elements=[actors.Method(body=actors.Expression(text='stringguard check: tag.\r\nlistguard check: attributes.\r\nhtmlstamp stamp: make element',
                                                                    inner_map={'element': L626}),
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
                                                                    inner_map={'element': L634}),
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
                                                                    inner_map={'onerror': L641,
                                                                               'onlist': L642,
                                                                               'onhtml': L643,
                                                                               'onstring': L644}),
                                             serial_id=5,
                                             parameters=['object'],
                                             selector='coerce:')],
                     next_serial_id=6)
L621 = actors.Example(expression=actors.Expression(text='make markup',
                                                   inner_map={'markup': L623}),
                      serial_id=4)
L647 = actors.Example(expression=actors.Expression(text='make html',
                                                   inner_map={'html': L649}),
                      serial_id=5)
L661 = actors.Script(elements=[actors.Method(body=actors.Expression(text='name htmlescaped + \'="\' +value htmlescaped + \'"\'',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=[],
                                             selector='show'),
                               actors.Text(body='XXX need to html-escape the strings',
                                           serial_id=1)],
                     next_serial_id=2)
L658 = actors.Script(elements=[actors.Method(body=actors.Expression(text='stringguard check: name.\r\nstringguard check: value.\r\nmake attribute',
                                                                    inner_map={'attribute': L661}),
                                             serial_id=0,
                                             parameters=['name',
                                                         'value'],
                                             selector='name:value:')],
                     next_serial_id=1)
L656 = actors.Example(expression=actors.Expression(text='make makeattr',
                                                   inner_map={'makeattr': L658}),
                      serial_id=8)
L669 = actors.Script(elements=[actors.Method(body=actors.Expression(text="' ' + attribute show + string",
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['attribute',
                                                         'string'],
                                             selector='left:right:'),
                               actors.Text(body='XXX rename this since it generically applies to html elements',
                                           serial_id=1)],
                     next_serial_id=2)
L667 = actors.Example(expression=actors.Expression(text='make showattr',
                                                   inner_map={'showattr': L669}),
                      serial_id=9)
L673 = actors.Example(expression=actors.Expression(text='html p show',
                                                   inner_map={}),
                      serial_id=12)
L676 = actors.Example(expression=actors.Expression(text='(html blockquote: []) show',
                                                   inner_map={}),
                      serial_id=14)
L679 = actors.Example(expression=actors.Expression(text='(html blockquote: [html p]) show',
                                                   inner_map={}),
                      serial_id=15)
L682 = actors.Example(expression=actors.Expression(text="(html blockquote: ['hello']) show",
                                                   inner_map={}),
                      serial_id=16)
L610 = actors.Script(elements=[L611,
                               L617,
                               L619,
                               L621,
                               L647,
                               L656,
                               L667,
                               L673,
                               L676,
                               L679,
                               L682],
                     next_serial_id=17)
L1443 = actors.Example(expression=actors.Expression(text='make htmlmodule',
                                                    inner_map={'htmlmodule': L610}),
                       serial_id=25)
L1413 = actors.Actor(env=L591,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1416,
                                                    L1419,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1422,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1425,
                                                    L1427,
                                                    L1429,
                                                    L1431,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1436,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1439,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1443],
                                          next_serial_id=26))
L1412 = actors.ActorEditor(editable=True,
                           actor=L1413)
L229 = builtin.Number(n=120.0)
L228 = actors.ActorEditor(editable=False,
                          actor=L229)
L306 = builtin.Number(n=42.0)
L305 = actors.ActorEditor(editable=False,
                          actor=L306)
L665 = actors.Actor(env=envs.Env(parent=L590),
                    script=L658)
L1381 = actors.ActorEditor(editable=True,
                           actor=L665)
L233 = actors.ActorEditor(editable=True,
                          actor=L124)
L1229 = builtin.Number(n=25.0)
L1799 = actors.ActorEditor(editable=False,
                           actor=L1229)
L1029 = builtin.Number(n=5.0)
L1028 = actors.ActorEditor(editable=False,
                           actor=L1029)
L947 = builtin.Box(initial_value=builtin.List(elements=()))
L1022 = actors.ActorEditor(editable=False,
                           actor=L947)
L1521 = builtin.Number(n=25.0)
L1622 = actors.ActorEditor(editable=False,
                           actor=L1521)
L1038 = builtin.Box(initial_value=L306)
L1037 = actors.ActorEditor(editable=False,
                           actor=L1038)
L1070 = builtin.Number(n=25.0)
L1560 = actors.ActorEditor(editable=False,
                           actor=L1070)
L1224 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1227 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1231 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L293}),
                       serial_id=4)
L1234 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1236 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1238 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1240 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1243 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1246 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L286 = actors.Script(elements=[],
                     next_serial_id=0)
L1250 = actors.Example(expression=actors.Expression(text='mailbox sender send: make message',
                                                    inner_map={'message': L286}),
                       serial_id=16)
L1221 = actors.Actor(env=L240,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1224,
                                                    L1227,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1231,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1234,
                                                    L1236,
                                                    L1238,
                                                    L1240,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1243,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1246,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1250],
                                          next_serial_id=17))
L1220 = actors.ActorEditor(editable=True,
                           actor=L1221)
L1629 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1632 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1370 = actors.Script(elements=[],
                      next_serial_id=0)
L1635 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L1370}),
                       serial_id=4)
L1638 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1640 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1642 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1644 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1649 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1652 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1656 = actors.Example(expression=actors.Expression(text='http://localhost:8080/id/5292533547202728044',
                                                    inner_map={}),
                       serial_id=16)
L1626 = actors.Actor(env=L1335,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1629,
                                                    L1632,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1635,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1638,
                                                    L1640,
                                                    L1642,
                                                    L1644,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1649,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1652,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1656],
                                          next_serial_id=17))
L1625 = actors.ActorEditor(editable=True,
                           actor=L1626)
L855 = builtin.Number(n=5.0)
L1095 = actors.ActorEditor(editable=False,
                           actor=L855)
L1059 = builtin.String(str='Is it a dog?')
L1058 = actors.ActorEditor(editable=False,
                           actor=L1059)
L366 = builtin.Number(n=5.0)
L1027 = actors.ActorEditor(editable=False,
                           actor=L366)
L1287 = builtin.Number(n=25.0)
L1573 = actors.ActorEditor(editable=False,
                           actor=L1287)
L913 = builtin.BoxMaker()
L1390 = actors.ActorEditor(editable=False,
                           actor=L913)
L705 = builtin.MailDirectory(env=envs.Env(parent=L592))
L1035 = actors.ActorEditor(editable=False,
                           actor=L705)
L166 = actors.Actor(env=L23,
                    script=L167)
L198 = actors.ActorEditor(editable=True,
                          actor=L166)
L700 = envs.Env(parent=L591)
L698 = actors.Actor(env=envs.Env(parent=L700),
                    script=L691)
L737 = actors.ActorEditor(editable=True,
                          actor=L698)
L1518 = builtin.Number(n=5.0)
L1616 = actors.ActorEditor(editable=False,
                           actor=L1518)
L369 = builtin.Number(n=25.0)
L1031 = actors.ActorEditor(editable=False,
                           actor=L369)
L1760 = actors.ActorEditor(editable=False,
                           actor=L383)
L437 = envs.Env(parent=L416)
L435 = actors.Actor(env=envs.Env(parent=L437),
                    script=L451)
L1406 = actors.ActorEditor(editable=True,
                           actor=L435)
L795 = builtin.Number(n=25.0)
L1171 = actors.ActorEditor(editable=False,
                           actor=L795)
L681 = builtin.String(str='<blockquote> <p></blockquote>')
L1179 = actors.ActorEditor(editable=False,
                           actor=L681)
L1389 = builtin.String(str='Hello, Alex!')
L1388 = actors.ActorEditor(editable=False,
                           actor=L1389)
L1325 = builtin.List(elements=(builtin.String(str='hello'),))
L1324 = actors.ActorEditor(editable=False,
                           actor=L1325)
L207 = actors.Actor(env=L208,
                    script=L180)
L1621 = actors.ActorEditor(editable=True,
                           actor=L207)
L56 = actors.Actor(env=envs.Env(parent=L50),
                   script=L58)
L1505 = actors.ActorEditor(editable=True,
                           actor=L56)
L61 = actors.Actor(env=L62,
                   script=L63)
L992 = actors.ActorEditor(editable=True,
                          actor=L61)
L588 = actors.Actor(env=envs.Env(parent=L590),
                    script=L669)
L587 = actors.ActorEditor(editable=True,
                          actor=L588)
L1631 = builtin.Number(n=5.0)
L1739 = actors.ActorEditor(editable=False,
                           actor=L1631)
L512 = envs.Env(parent=L476)
L511 = builtin.MailDirectory(env=L512)
L1169 = actors.ActorEditor(editable=False,
                           actor=L511)
L265 = actors.Actor(env=L240,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L269,
                                                                                                   'mailbox': L272}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L1751 = actors.ActorEditor(editable=True,
                           actor=L265)
L1562 = builtin.Number(n=25.0)
L1561 = actors.ActorEditor(editable=False,
                           actor=L1562)
L1252 = actors.Actor(env=L241,
                     script=actors.Script(elements=[],
                                          next_serial_id=0))
L1329 = actors.ActorEditor(editable=True,
                           actor=L1252)
L215 = envs.Env(parent=L24)
L159 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
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
L213 = actors.Actor(env=envs.Env(parent=L215),
                    script=L159)
L1034 = actors.ActorEditor(editable=True,
                           actor=L213)
L513 = actors.Actor(env=envs.Env(parent=L474),
                    script=L498)
L1265 = actors.ActorEditor(editable=True,
                           actor=L513)
L83 = actors.Actor(env=L84,
                   script=L85)
L1328 = actors.ActorEditor(editable=True,
                           actor=L83)
L231 = builtin.StampGuard(stamp=L232)
L413 = builtin.List(elements=(L232,
                              L231))
L412 = actors.ActorEditor(editable=False,
                          actor=L413)
L12 = builtin.Boolean(value=True,
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
L411 = actors.ActorEditor(editable=False,
                          actor=L12)
L914 = builtin.Boolean(value=True,
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
L1752 = actors.ActorEditor(editable=False,
                           actor=L914)
L323 = builtin.BoxMaker()
L1504 = actors.ActorEditor(editable=False,
                           actor=L323)
L1192 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
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
L1185 = actors.Actor(env=L1184,
                     script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                         inner_map={'sender': L1189,
                                                                                                    'mailbox': L1192}),
                                                                  serial_id=0,
                                                                  parameters=[],
                                                                  selector='run')],
                                          next_serial_id=1))
L1543 = actors.ActorEditor(editable=True,
                           actor=L1185)
L709 = actors.Actor(env=envs.Env(parent=L591),
                    script=L711)
L1470 = actors.ActorEditor(editable=True,
                           actor=L709)
L757 = builtin.Box(initial_value=L750)
L1743 = actors.ActorEditor(editable=False,
                           actor=L757)
L1405 = builtin.String(str='Wavy!')
L1404 = actors.ActorEditor(editable=False,
                           actor=L1405)
L173 = envs.Env(parent=L22)
L191 = actors.Script(elements=[actors.Method(body=actors.Expression(text='query',
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
L171 = actors.Actor(env=envs.Env(parent=L173),
                    script=L191)
L1503 = actors.ActorEditor(editable=True,
                           actor=L171)
L1372 = builtin.Number(n=25.0)
L1371 = actors.ActorEditor(editable=False,
                           actor=L1372)
L713 = builtin.List(elements=(builtin.String(str='hello'),))
L712 = actors.ActorEditor(editable=False,
                          actor=L713)
L848 = builtin.String(str='Is it a cat?')
L847 = actors.ActorEditor(editable=False,
                          actor=L848)
L578 = builtin.String(str='Thank you!')
L577 = actors.ActorEditor(editable=False,
                          actor=L578)
L743 = builtin.Boolean(value=True,
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
L1391 = actors.ActorEditor(editable=False,
                           actor=L743)
L170 = builtin.Box(initial_value=L171)
L1748 = actors.ActorEditor(editable=False,
                           actor=L170)
L841 = builtin.Number(n=6.0)
L1254 = actors.ActorEditor(editable=False,
                           actor=L841)
L1363 = envs.Env(parent=L1335)
L1361 = actors.Actor(env=envs.Env(parent=L1363),
                     script=L1354)
L1400 = actors.ActorEditor(editable=True,
                           actor=L1361)
L1449 = envs.Env(parent=None)
L1448 = actors.Actor(env=L1449,
                     script=actors.Script(elements=[],
                                          next_serial_id=0))
L1447 = actors.ActorEditor(editable=True,
                           actor=L1448)
L423 = builtin.Boolean(value=True,
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
L1278 = actors.ActorEditor(editable=False,
                           actor=L423)
L1556 = builtin.String(str='Is it a dog?')
L1555 = actors.ActorEditor(editable=False,
                           actor=L1556)
L1333 = actors.Actor(env=envs.Env(parent=L1335),
                     script=L1370)
L1332 = actors.ActorEditor(editable=True,
                           actor=L1333)
L204 = actors.Actor(env=L178,
                    script=L201)
L1741 = actors.ActorEditor(editable=True,
                           actor=L204)
L675 = builtin.String(str='<p>')
L1754 = actors.ActorEditor(editable=False,
                           actor=L675)
L237 = actors.Actor(env=envs.Env(parent=L239),
                    script=L272)
L236 = actors.ActorEditor(editable=True,
                          actor=L237)
L576 = actors.ActorEditor(editable=False,
                          actor=L26)
L1581 = actors.ActorEditor(editable=False,
                           actor=L232)
L606 = builtin.BoxMaker()
L1747 = actors.ActorEditor(editable=False,
                           actor=L606)
L609 = actors.Actor(env=L590,
                    script=L610)
L616 = actors.ActorEditor(editable=True,
                          actor=L609)
L156 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0,
                                             parameters=['message'],
                                             selector='send:')],
                     next_serial_id=1)
L152 = actors.Actor(env=L24,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L156,
                                                                                                   'mailbox': L159}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L1615 = actors.ActorEditor(editable=True,
                           actor=L152)
L1408 = builtin.Number(n=7.0)
L1407 = actors.ActorEditor(editable=False,
                           actor=L1408)
L1004 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                     inner_map={}),
                                              serial_id=0,
                                              parameters=['message'],
                                              selector='send:')],
                      next_serial_id=1)
L1007 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
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
L1000 = actors.Actor(env=L998,
                     script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                         inner_map={'sender': L1004,
                                                                                                    'mailbox': L1007}),
                                                                  serial_id=0,
                                                                  parameters=[],
                                                                  selector='run')],
                                          next_serial_id=1))
L1401 = actors.ActorEditor(editable=True,
                           actor=L1000)
L521 = builtin.Boolean(value=False,
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
L543 = builtin.Box(initial_value=L521)
L986 = actors.ActorEditor(editable=False,
                          actor=L543)
L1346 = builtin.Box(initial_value=L1173)
L1726 = actors.ActorEditor(editable=False,
                           actor=L1346)
L458 = actors.Actor(env=envs.Env(parent=L416),
                    script=L460)
L1410 = actors.ActorEditor(editable=True,
                           actor=L458)
L1558 = builtin.List(elements=(builtin.String(str='hello'),))
L1557 = actors.ActorEditor(editable=False,
                           actor=L1558)
L1476 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1478 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1482 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L546}),
                       serial_id=4)
L1485 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1487 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1489 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1491 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1494 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1497 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1501 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=16)
L1473 = actors.Actor(env=L519,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1476,
                                                    L1478,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1482,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1485,
                                                    L1487,
                                                    L1489,
                                                    L1491,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1494,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1497,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1501],
                                          next_serial_id=17))
L1472 = actors.ActorEditor(editable=True,
                           actor=L1473)
L121 = builtin.String(str='cat')
L889 = actors.ActorEditor(editable=False,
                          actor=L121)
L1418 = builtin.Number(n=5.0)
L1749 = actors.ActorEditor(editable=False,
                           actor=L1418)
L179 = builtin.String(str='cat')
L1394 = actors.ActorEditor(editable=False,
                           actor=L179)
L220 = builtin.MailDirectory(env=envs.Env(parent=L25))
L1170 = actors.ActorEditor(editable=False,
                           actor=L220)
L1199 = actors.Actor(env=envs.Env(parent=L1183),
                     script=L1192)
L1398 = actors.ActorEditor(editable=True,
                           actor=L1199)
L970 = envs.Env(parent=None)
L969 = actors.Actor(env=L970,
                    script=actors.Script(elements=[],
                                         next_serial_id=0))
L968 = actors.ActorEditor(editable=True,
                          actor=L969)
L11 = builtin.StampMaker()
L1572 = actors.ActorEditor(editable=False,
                           actor=L11)
L1331 = builtin.String(str='OK!')
L1330 = actors.ActorEditor(editable=False,
                           actor=L1331)
L352 = actors.Script(elements=[],
                     next_serial_id=0)
L350 = actors.Actor(env=envs.Env(parent=L311),
                    script=L352)
L1506 = actors.ActorEditor(editable=True,
                           actor=L350)
L253 = builtin.Boolean(value=True,
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
L719 = actors.ActorEditor(editable=False,
                          actor=L253)
L515 = builtin.Box(initial_value=builtin.List(elements=()))
L1314 = actors.ActorEditor(editable=False,
                           actor=L515)
L1469 = actors.ActorEditor(editable=False,
                           actor=L614)
L1258 = builtin.Number(n=0)
L1257 = actors.ActorEditor(editable=False,
                           actor=L1258)
L1433 = builtin.List(elements=(builtin.String(str='hello'),))
L1571 = actors.ActorEditor(editable=False,
                           actor=L1433)
L1024 = builtin.Number(n=10)
L1023 = actors.ActorEditor(editable=False,
                           actor=L1024)
L726 = builtin.Box(initial_value=L727)
L725 = actors.ActorEditor(editable=False,
                          actor=L726)
L765 = actors.Script(elements=[actors.Method(body=actors.Expression(text='inbox get at: 1',
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
L772 = actors.Actor(env=envs.Env(parent=L774),
                    script=L765)
L1619 = actors.ActorEditor(editable=True,
                           actor=L772)
L397 = actors.ActorEditor(editable=False,
                          actor=L398)
L1218 = builtin.Box(initial_value=builtin.List(elements=(L1209,)))
L1554 = actors.ActorEditor(editable=False,
                           actor=L1218)
L531 = builtin.BoxMaker()
L1564 = actors.ActorEditor(editable=False,
                           actor=L531)
L1376 = envs.Env(parent=L176)
L1374 = actors.Actor(env=envs.Env(parent=L1376),
                     script=L187)
L1373 = actors.ActorEditor(editable=True,
                           actor=L1374)
L871 = builtin.List(elements=(builtin.String(str='hello'),))
L1264 = actors.ActorEditor(editable=False,
                           actor=L871)
L1044 = builtin.Number(n=25.0)
L1043 = actors.ActorEditor(editable=False,
                           actor=L1044)
L230 = actors.ActorEditor(editable=False,
                          actor=L231)
L127 = builtin.String(str='dog')
L1546 = actors.ActorEditor(editable=False,
                           actor=L127)
L758 = actors.Actor(env=L741,
                    script=actors.Script(elements=[actors.Method(body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L762,
                                                                                                   'mailbox': L765}),
                                                                 serial_id=0,
                                                                 parameters=[],
                                                                 selector='run')],
                                         next_serial_id=1))
L1578 = actors.ActorEditor(editable=True,
                           actor=L758)
L942 = actors.Example(expression=actors.Expression(text='1 * 2 * 3 * 4 * 5',
                                                   inner_map={}),
                      serial_id=0)
L941 = actors.Script(elements=[L942],
                     next_serial_id=1)
L939 = actors.Actor(env=envs.Env(parent=L907),
                    script=L941)
L944 = actors.ActorEditor(editable=True,
                          actor=L939)
L883 = actors.Actor(env=L417,
                    script=actors.Script(elements=[],
                                         next_serial_id=0))
L1411 = actors.ActorEditor(editable=True,
                           actor=L883)
L1383 = actors.Actor(env=L893,
                     script=actors.Script(elements=[],
                                          next_serial_id=0))
L1382 = actors.ActorEditor(editable=True,
                           actor=L1383)
L353 = builtin.MailDirectory(env=envs.Env(parent=L312))
L1377 = actors.ActorEditor(editable=False,
                           actor=L353)
L954 = envs.Env(parent=L143)
L952 = actors.Actor(env=envs.Env(parent=L954),
                    script=L99)
L951 = actors.ActorEditor(editable=True,
                          actor=L952)
L364 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                   inner_map={}),
                      serial_id=1)
L367 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                   inner_map={}),
                      serial_id=2)
L371 = actors.Example(expression=actors.Expression(text='make Foo',
                                                   inner_map={'Foo': L352}),
                      serial_id=4)
L374 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                   inner_map={}),
                      serial_id=6)
L376 = actors.Example(expression=actors.Expression(text='box get',
                                                   inner_map={}),
                      serial_id=7)
L378 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                   inner_map={}),
                      serial_id=8)
L380 = actors.Example(expression=actors.Expression(text="['hello']",
                                                   inner_map={}),
                      serial_id=9)
L385 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                   inner_map={}),
                      serial_id=11)
L388 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                   inner_map={}),
                      serial_id=13)
L392 = actors.Example(expression=actors.Expression(text='http://localhost:8080/id/5186614581370432354',
                                                   inner_map={}),
                      serial_id=16)
L394 = actors.Example(expression=actors.Expression(text='8 * 5',
                                                   inner_map={}),
                      serial_id=17)
L310 = actors.Actor(env=L311,
                    script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                               serial_id=0),
                                                   L364,
                                                   L367,
                                                   actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                               serial_id=3),
                                                   L371,
                                                   actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                               serial_id=5),
                                                   L374,
                                                   L376,
                                                   L378,
                                                   L380,
                                                   actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                               serial_id=10),
                                                   L385,
                                                   actors.Text(body='You can create your own mailbox:',
                                                               serial_id=12),
                                                   L388,
                                                   actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                               serial_id=14),
                                                   actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                               serial_id=15),
                                                   L392,
                                                   L394],
                                         next_serial_id=18))
L309 = actors.ActorEditor(editable=True,
                          actor=L310)
L1565 = actors.ActorEditor(editable=False,
                           actor=L581)
L1256 = builtin.String(str='Thanks, I will remember.')
L1255 = actors.ActorEditor(editable=False,
                           actor=L1256)
L958 = envs.Env(parent=L109)
L956 = actors.Actor(env=envs.Env(parent=L958),
                    script=L69)
L955 = actors.ActorEditor(editable=True,
                          actor=L956)
L716 = builtin.Number(n=0.0)
L715 = actors.ActorEditor(editable=False,
                          actor=L716)
L645 = actors.Actor(env=envs.Env(parent=L590),
                    script=L623)
L1759 = actors.ActorEditor(editable=True,
                           actor=L645)
L1201 = actors.Actor(env=envs.Env(parent=L1184),
                     script=L1203)
L1509 = actors.ActorEditor(editable=True,
                           actor=L1201)
L573 = builtin.Number(n=5.0)
L572 = actors.ActorEditor(editable=False,
                          actor=L573)
L225 = actors.Script(elements=[actors.Method(body=actors.Expression(text='make yesnoquestion\r\n',
                                                                    inner_map={'yesnoquestion': L191}),
                                             serial_id=2,
                                             parameters=['query',
                                                         'onyes',
                                                         'onno'],
                                             selector='asking:ifyes:ifno:')],
                     next_serial_id=3)
L21 = actors.Actor(env=L22,
                   script=L225)
L20 = actors.ActorEditor(editable=True,
                         actor=L21)
L1262 = actors.ActorEditor(editable=False,
                           actor=L521)
L949 = actors.Actor(env=envs.Env(parent=L906),
                    script=L929)
L1727 = actors.ActorEditor(editable=True,
                           actor=L949)
L547 = builtin.MailDirectory(env=envs.Env(parent=L520))
L993 = actors.ActorEditor(editable=False,
                          actor=L547)
L1226 = builtin.Number(n=5.0)
L1617 = actors.ActorEditor(editable=False,
                           actor=L1226)
L1378 = actors.ActorEditor(editable=False,
                           actor=L477)
L607 = builtin.TypeGuard(sample_instance=())
L1379 = actors.ActorEditor(editable=False,
                           actor=L607)
L1016 = envs.Env(parent=L998)
L1014 = actors.Actor(env=envs.Env(parent=L1016),
                     script=L1007)
L1315 = actors.ActorEditor(editable=True,
                           actor=L1014)
L779 = builtin.MailDirectory(env=envs.Env(parent=L742))
L1403 = actors.ActorEditor(editable=False,
                           actor=L779)
L552 = actors.Actor(env=envs.Env(parent=L551),
                    script=L554)
L733 = actors.ActorEditor(editable=True,
                          actor=L552)
L1065 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1068 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1072 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L1021}),
                       serial_id=4)
L1075 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1077 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1079 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1081 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1086 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1089 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1093 = actors.Example(expression=actors.Expression(text='let pair = makestamp run',
                                                    inner_map={}),
                       serial_id=16)
L1062 = actors.Actor(env=L998,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1065,
                                                    L1068,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1072,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1075,
                                                    L1077,
                                                    L1079,
                                                    L1081,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1086,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1089,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1093],
                                          next_serial_id=17))
L1061 = actors.ActorEditor(editable=True,
                           actor=L1062)
L463 = builtin.MailDirectory(env=envs.Env(parent=L417))
L1468 = actors.ActorEditor(editable=False,
                           actor=L463)
L1516 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1519 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1523 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L941}),
                       serial_id=4)
L1526 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1528 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1530 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1532 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1535 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1538 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1513 = actors.Actor(env=L907,
                     script=actors.Script(elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1516,
                                                    L1519,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1523,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1526,
                                                    L1528,
                                                    L1530,
                                                    L1532,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1535,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1538,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15)],
                                          next_serial_id=16))
L1512 = actors.ActorEditor(editable=True,
                           actor=L1513)
L36 = builtin.BoxMaker()
L1321 = actors.ActorEditor(editable=False,
                           actor=L36)
L0 = registry.HmphSystem(editor_of_actor={L925: L1445,
                                          L422: L1393,
                                          L960: L959,
                                          L792: L963,
                                          L231: L230,
                                          L107: L846,
                                          L308: L307,
                                          L1448: L1447,
                                          L707: L1568,
                                          L573: L572,
                                          L37: L1036,
                                          L1185: L1543,
                                          L698: L737,
                                          L1026: L1025,
                                          L723: L722,
                                          L949: L1727,
                                          L593: L1510,
                                          L858: L1260,
                                          L1046: L1045,
                                          L61: L992,
                                          L1056: L1055,
                                          L508: L994,
                                          L543: L986,
                                          L1199: L1398,
                                          L779: L1403,
                                          L743: L1391,
                                          L229: L228,
                                          L336: L1054,
                                          L56: L1505,
                                          L435: L1406,
                                          L588: L587,
                                          L494: L1567,
                                          L405: L404,
                                          L21: L20,
                                          L382: L1399,
                                          L750: L967,
                                          L252: L1313,
                                          L1033: L1032,
                                          L757: L1743,
                                          L415: L414,
                                          L1508: L1507,
                                          L1408: L1407,
                                          L965: L964,
                                          L580: L579,
                                          L121: L889,
                                          L606: L1747,
                                          L116: L1737,
                                          L684: L1580,
                                          L122: L1030,
                                          L518: L517,
                                          L1521: L1622,
                                          L532: L1402,
                                          L1762: L1761,
                                          L952: L951,
                                          L1097: L1096,
                                          L1413: L1412,
                                          L996: L995,
                                          L1562: L1561,
                                          L772: L1619,
                                          L487: L1039,
                                          L313: L1736,
                                          L578: L577,
                                          L740: L739,
                                          L423: L1278,
                                          L174: L1740,
                                          L1213: L1467,
                                          L749: L1395,
                                          L324: L1446,
                                          L310: L309,
                                          L1029: L1028,
                                          L1042: L1041,
                                          L434: L574,
                                          L18: L966,
                                          L1325: L1324,
                                          L220: L1170,
                                          L253: L719,
                                          L808: L1322,
                                          L1277: L1618,
                                          L1312: L1311,
                                          L493: L736,
                                          L609: L616,
                                          L142: L1511,
                                          L607: L1379,
                                          L1659: L1658,
                                          L665: L1381,
                                          L969: L968,
                                          L549: L575,
                                          L396: L1261,
                                          L1181: L1180,
                                          L721: L720,
                                          L613: L1263,
                                          L1389: L1388,
                                          L1201: L1509,
                                          L945: L1040,
                                          L472: L471,
                                          L822: L1168,
                                          L1433: L1571,
                                          L299: L298,
                                          L289: L1392,
                                          L296: L738,
                                          L1044: L1043,
                                          L713: L712,
                                          L705: L1035,
                                          L235: L234,
                                          L678: L1319,
                                          L264: L1057,
                                          L1570: L1569,
                                          L785: L1396,
                                          L552: L733,
                                          L242: L1327,
                                          L123: L1623,
                                          L175: L1624,
                                          L1209: L1385,
                                          L222: L1545,
                                          L1387: L1386,
                                          L777: L1746,
                                          L544: L1566,
                                          L775: L1397,
                                          L1268: L1267,
                                          L850: L849,
                                          L306: L305,
                                          L463: L1468,
                                          L781: L1266,
                                          L26: L576,
                                          L608: L1318,
                                          L147: L1620,
                                          L413: L412,
                                          L1258: L1257,
                                          L1070: L1560,
                                          L999: L1729,
                                          L1626: L1625,
                                          L1480: L1731,
                                          L513: L1265,
                                          L103: L1544,
                                          L210: L1409,
                                          L913: L1390,
                                          L600: L1753,
                                          L166: L198,
                                          L1272: L1271,
                                          L383: L1760,
                                          L795: L1171,
                                          L547: L993,
                                          L904: L903,
                                          L681: L1179,
                                          L599: L1734,
                                          L570: L569,
                                          L207: L1621,
                                          L891: L890,
                                          L355: L1466,
                                          L1221: L1220,
                                          L279: L1738,
                                          L1000: L1401,
                                          L1513: L1512,
                                          L1252: L1329,
                                          L1173: L1172,
                                          L265: L1751,
                                          L557: L1320,
                                          L11: L1572,
                                          L511: L1169,
                                          L83: L1328,
                                          L1575: L1574,
                                          L1583: L1582,
                                          L855: L1095,
                                          L645: L1759,
                                          L465: L1744,
                                          L51: L1745,
                                          L1405: L1404,
                                          L171: L1503,
                                          L1372: L1371,
                                          L615: L1471,
                                          L848: L847,
                                          L1083: L1728,
                                          L991: L990,
                                          L841: L1254,
                                          L1361: L1400,
                                          L323: L1504,
                                          L48: L1742,
                                          L1556: L1555,
                                          L1333: L1332,
                                          L204: L1741,
                                          L675: L1754,
                                          L1548: L1547,
                                          L1317: L1316,
                                          L232: L1581,
                                          L1518: L1616,
                                          L152: L1615,
                                          L654: L718,
                                          L1368: L1563,
                                          L369: L1031,
                                          L1383: L1382,
                                          L1346: L1726,
                                          L458: L1410,
                                          L1558: L1557,
                                          L1473: L1472,
                                          L1756: L1755,
                                          L515: L1314,
                                          L237: L236,
                                          L1418: L1749,
                                          L939: L944,
                                          L179: L1394,
                                          L124: L233,
                                          L1733: L1732,
                                          L1280: L1279,
                                          L1588: L1730,
                                          L1331: L1330,
                                          L350: L1506,
                                          L1165: L1164,
                                          L2: L1,
                                          L614: L1469,
                                          L291: L1579,
                                          L1287: L1573,
                                          L1024: L1023,
                                          L726: L725,
                                          L12: L411,
                                          L294: L1380,
                                          L1218: L1554,
                                          L1631: L1739,
                                          L1374: L1373,
                                          L871: L1264,
                                          L366: L1027,
                                          L335: L717,
                                          L1067: L1542,
                                          L127: L1546,
                                          L1229: L1799,
                                          L5: L1060,
                                          L727: L1323,
                                          L883: L1411,
                                          L914: L1752,
                                          L353: L1377,
                                          L1059: L1058,
                                          L988: L987,
                                          L735: L734,
                                          L581: L1565,
                                          L947: L1022,
                                          L1256: L1255,
                                          L956: L955,
                                          L716: L715,
                                          L758: L1578,
                                          L170: L1748,
                                          L1038: L1037,
                                          L213: L1034,
                                          L521: L1262,
                                          L398: L397,
                                          L709: L1470,
                                          L1226: L1617,
                                          L477: L1378,
                                          L1646: L1735,
                                          L1014: L1315,
                                          L1053: L1052,
                                          L49: L131,
                                          L118: L1259,
                                          L1062: L1061,
                                          L1347: L1750,
                                          L531: L1564,
                                          L36: L1321},
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
                                   '6737ab2d99858d2cb98e',
                                   '5b74f62f6857b7956095'],
                         at_id={'ab0fef7f36dd3d6e5a6e': registry.Entry(timestamp=1208019537.3862081,
                                                                       actor=L517),
                                '3852696174487011421': registry.Entry(timestamp=1104697525.0871,
                                                                      actor=L1469),
                                'd0f449aa58533e36ea69': registry.Entry(timestamp=1109433966.3965299,
                                                                       actor=L88),
                                '785dd82fa6b01f374f86': registry.Entry(timestamp=1208019245.832073,
                                                                       actor=L993),
                                '389f782794ad82bf42c2': registry.Entry(timestamp=1109435020.479353,
                                                                       actor=L1311),
                                'fc1d1a3284d605538654': registry.Entry(timestamp=1109422775.0987959,
                                                                       actor=L224),
                                '50c6025c3f7c1b17b359': registry.Entry(timestamp=1190664334.063704,
                                                                       actor=L1378),
                                '92077dd35d38c54b1d7a': registry.Entry(timestamp=1109433506.8028109,
                                                                       actor=L58),
                                'e0a19b1b2095e54a1a98': registry.Entry(timestamp=1109428828.339134,
                                                                       actor=L171),
                                '563ca179481499c18ab6': registry.Entry(timestamp=1109435048.1022961,
                                                                       actor=L1026),
                                '177af5534bd8e4a0efef': registry.Entry(timestamp=1109434948.9887691,
                                                                       actor=L1321),
                                '33e43cb0a69702868a1b': registry.Entry(timestamp=1109435117.5115161,
                                                                       actor=L1755),
                                'a9dd87deafb6771dc685': registry.Entry(timestamp=1109433538.641732,
                                                                       actor=L48),
                                '661509098043722411': registry.Entry(timestamp=1104650549.6519859,
                                                                     actor=L966),
                                '9e4059674b42ebb77e80': registry.Entry(timestamp=1190664333.9055829,
                                                                       actor=L1280),
                                'db48f7ce53f52a1be8ef': registry.Entry(timestamp=1208019245.829556,
                                                                       actor=L1564),
                                '2452790028842326399': registry.Entry(timestamp=1104650712.6615851,
                                                                      actor=L1747),
                                '244593790248987534': registry.Entry(timestamp=1104696067.7436399,
                                                                     actor=L1381),
                                '7733755804024661725': registry.Entry(timestamp=1104730507.793503,
                                                                      actor=L352),
                                'd3f069172de864d5ed94': registry.Entry(timestamp=1105921788.5114219,
                                                                       actor=L1393),
                                '585cf6e821add948341f': registry.Entry(timestamp=1108956454.2687061,
                                                                       actor=L1033),
                                '9923278975221135661': registry.Entry(timestamp=1104650760.2987189,
                                                                      actor=L230),
                                '12946586331713097828': registry.Entry(timestamp=1104650753.210412,
                                                                       actor=L232),
                                '701718880621245410': registry.Entry(timestamp=1104689955.3227019,
                                                                     actor=L623),
                                '2169573376375311512': registry.Entry(timestamp=1104732128.235605,
                                                                      actor=L1407),
                                '425401d16cbbcb013414': registry.Entry(timestamp=1109424299.651423,
                                                                       actor=L1409),
                                '7488614337481629366': registry.Entry(timestamp=1104732124.7329731,
                                                                      actor=L1027),
                                'b02f708094d7017ff9ca': registry.Entry(timestamp=1109428831.4527409,
                                                                       actor=L174),
                                '4716280173295595176': registry.Entry(timestamp=1104632228.340987,
                                                                      actor=L1171),
                                '6ea8e4e7c59015808866': registry.Entry(timestamp=1108956215.9937069,
                                                                       actor=L725),
                                '809ca9a6a52e472c2232': registry.Entry(timestamp=1108956539.881407,
                                                                       actor=L1388),
                                '2fe08bfff563b4be7b88': registry.Entry(timestamp=1109428875.280458,
                                                                       actor=L1052),
                                '14f6bb412e4e8dba28e7': registry.Entry(timestamp=1105921513.4537351,
                                                                       actor=L1260),
                                '94c3545f0b71f518f49b': registry.Entry(timestamp=1208019245.82639,
                                                                       actor=L1386),
                                '752780470375236548': registry.Entry(timestamp=1104650712.6552,
                                                                     actor=L1470),
                                '13472432016877657261': registry.Entry(timestamp=1104650549.645519,
                                                                       actor=L995),
                                '86494131c70f31e05c76': registry.Entry(timestamp=1105921566.047498,
                                                                       actor=L1744),
                                '95e56b4ad9bd4778155e': registry.Entry(timestamp=1109435020.4820459,
                                                                       actor=L1312),
                                'aeca121725efb320e1bd': registry.Entry(timestamp=1109435097.3057289,
                                                                       actor=L1267),
                                '10397032148789093459': registry.Entry(timestamp=1104732128.235873,
                                                                       actor=L1408),
                                '6ad807ecfa9819fc5274': registry.Entry(timestamp=1108956554.296838,
                                                                       actor=L1467),
                                '27a3eaafc2929449c2': registry.Entry(timestamp=1108412240.3505909,
                                                                     actor=L1329),
                                'f6599863150eeb0c6b2c': registry.Entry(timestamp=1109434795.847883,
                                                                       actor=L142),
                                '7773452571940476712': registry.Entry(timestamp=1104697525.0874059,
                                                                      actor=L614),
                                '8260809509679861109': registry.Entry(timestamp=1104633042.4136021,
                                                                      actor=L1397),
                                '13289750248154104862': registry.Entry(timestamp=1104730109.325695,
                                                                       actor=L1172),
                                '9876815513572400324': registry.Entry(timestamp=1104650549.6620231,
                                                                      actor=L1728),
                                '4023b3c507c036f50e56': registry.Entry(timestamp=1104797071.70976,
                                                                       actor=L1616),
                                '4c09de69dcaeb7cc983c': registry.Entry(timestamp=1109428388.68279,
                                                                       actor=L1748),
                                'afe0f8475c226480003e': registry.Entry(timestamp=1104797063.4905939,
                                                                       actor=L1040),
                                '14572783785176608328': registry.Entry(timestamp=1104632228.3476341,
                                                                       actor=L1391),
                                '2af0a890ec67be538d2e': registry.Entry(timestamp=1190664333.9233689,
                                                                       actor=L1573),
                                '3bc09d4543e10c13c0fd': registry.Entry(timestamp=1109435162.498421,
                                                                       actor=L122),
                                '744cd5a5607fb52901e3': registry.Entry(timestamp=1190665257.4724829,
                                                                       actor=L1265),
                                'dfdddcc9276b298ffa66': registry.Entry(timestamp=1108412173.816499,
                                                                       actor=L236),
                                '3221c3e44d26b6bbd5ad': registry.Entry(timestamp=1105921540.943424,
                                                                       actor=L855),
                                'e64afe24df26d799a9ac': registry.Entry(timestamp=1104807972.488673,
                                                                       actor=L939),
                                '17543361990980566375': registry.Entry(timestamp=1104650712.6712439,
                                                                       actor=L1571),
                                'aa59537f559184f9eca2': registry.Entry(timestamp=1104797063.503005,
                                                                       actor=L1445),
                                '15235668337536127643': registry.Entry(timestamp=1104650549.6492591,
                                                                       actor=L1729),
                                '66910d75bb942953d69c': registry.Entry(timestamp=1208019245.8258109,
                                                                       actor=L1473),
                                '506e223cff60b5489e1b': registry.Entry(timestamp=1109435078.919728,
                                                                       actor=L53),
                                'bd4007d9b81ff6015fa': registry.Entry(timestamp=1109677352.059732,
                                                                      actor=L1745),
                                '66e67041b7181b22690': registry.Entry(timestamp=1104797063.3189459,
                                                                      actor=L941),
                                '9f783033e4c251e7aecd': registry.Entry(timestamp=1109435120.1054151,
                                                                       actor=L965),
                                '1823737881735097641': registry.Entry(timestamp=1104633108.6909039,
                                                                      actor=L968),
                                'd12f22d62909bfa38926': registry.Entry(timestamp=1190664334.0435531,
                                                                       actor=L994),
                                '6231133fb36d5570d27a': registry.Entry(timestamp=1109434995.1101241,
                                                                       actor=L1255),
                                '2291036927185731541': registry.Entry(timestamp=1104650712.656209,
                                                                      actor=L711),
                                '16832713526910606204': registry.Entry(timestamp=1104732473.8273611,
                                                                       actor=L1316),
                                'e5adaa9b6e0a3d911e8c': registry.Entry(timestamp=1208019245.8314581,
                                                                       actor=L1324),
                                '5ce1f20ddbfb0d7dbdc8': registry.Entry(timestamp=1109422775.132426,
                                                                       actor=L1615),
                                '10238622742572975996': registry.Entry(timestamp=1104696935.0587831,
                                                                       actor=L626),
                                'feab0d101efa1eb7800c': registry.Entry(timestamp=1105921822.377749,
                                                                       actor=L883),
                                '6368b3eb10785a7e39c3': registry.Entry(timestamp=1104797063.330265,
                                                                       actor=L1752),
                                '8635995105440979424': registry.Entry(timestamp=1104650712.6806979,
                                                                      actor=L737),
                                '9515dc91fc08cfc0dda0': registry.Entry(timestamp=1109428838.2248061,
                                                                       actor=L848),
                                '1955787528046718785': registry.Entry(timestamp=1104689968.784857,
                                                                      actor=L645),
                                '4b6ad410a34d5b6c16ee': registry.Entry(timestamp=1105921803.8393171,
                                                                       actor=L1410),
                                '5b0ee41b18f3e75167a2': registry.Entry(timestamp=1104797063.3379431,
                                                                       actor=L1565),
                                'd09a2d478bd604dc3907': registry.Entry(timestamp=1109435120.102756,
                                                                       actor=L964),
                                '4eec14b8e7620b9cbbf6': registry.Entry(timestamp=1104797063.3455911,
                                                                       actor=L569),
                                '5f250d31a4b5ac2e53cb': registry.Entry(timestamp=1109435010.016041,
                                                                       actor=L1623),
                                '9360497806179331195': registry.Entry(timestamp=1104650930.792357,
                                                                      actor=L707),
                                'd56af1fc4e478d2676e4': registry.Entry(timestamp=1109424447.451117,
                                                                       actor=L1555),
                                '17127538032127337902': registry.Entry(timestamp=1104730109.318953,
                                                                       actor=L1041),
                                'f087d80a9309247b65a': registry.Entry(timestamp=1108956695.1802731,
                                                                      actor=L1199),
                                '844713905205980550': registry.Entry(timestamp=1104730109.319428,
                                                                     actor=L1045),
                                '17611950891294426261': registry.Entry(timestamp=1104690171.623419,
                                                                       actor=L1379),
                                'f58848882bb5b9bb3ac8': registry.Entry(timestamp=1109433508.5816081,
                                                                       actor=L56),
                                '8cf176cfe796cd156975': registry.Entry(timestamp=1190665181.345289,
                                                                       actor=L471),
                                '1d080e958d08e20c362b': registry.Entry(timestamp=1109434485.9212029,
                                                                       actor=L89),
                                'f8ff73eb7cf1b9941a73': registry.Entry(timestamp=1109428388.6854019,
                                                                       actor=L170),
                                '9057425907194955737': registry.Entry(timestamp=1105488351.8877051,
                                                                      actor=L616),
                                '3518475730128674669': registry.Entry(timestamp=1104730507.83989,
                                                                      actor=L1466),
                                '4227047065147840205': registry.Entry(timestamp=1104650529.884198,
                                                                      actor=L739),
                                '12634790733065757812': registry.Entry(timestamp=1104632228.343287,
                                                                       actor=L787),
                                '12685563122316055259': registry.Entry(timestamp=1104706912.387881,
                                                                       actor=L641),
                                'c4fbf97dd8919c749ca9': registry.Entry(timestamp=1190664333.911598,
                                                                       actor=L720),
                                'fcceeb077cb614ca85f8': registry.Entry(timestamp=1105921806.0911419,
                                                                       actor=L1038),
                                'a51f96a48acf383d67b6': registry.Entry(timestamp=1108956747.618078,
                                                                       actor=L1383),
                                '437ed8478e622b78736e': registry.Entry(timestamp=1208019541.593823,
                                                                       actor=L575),
                                '3324730690425372007': registry.Entry(timestamp=1104650549.6319871,
                                                                      actor=L1542),
                                'eaad67a6f405387e7f63': registry.Entry(timestamp=1109428392.426419,
                                                                       actor=L21),
                                '1f450f46787e5df1a832': registry.Entry(timestamp=1109433892.9024999,
                                                                       actor=L66),
                                'f57378bfa8f1bda4717f': registry.Entry(timestamp=1109428871.343946,
                                                                       actor=L1621),
                                'e6e700e2d7e729e3e72': registry.Entry(timestamp=1104807950.8954489,
                                                                      actor=L903),
                                '2f63027d1e8f1c1a37fd': registry.Entry(timestamp=1109428835.8189859,
                                                                       actor=L1394),
                                '9ffceadfb339bf0a37b7': registry.Entry(timestamp=1109434995.1128759,
                                                                       actor=L1256),
                                '6c6ed31f12ce3e23a22a': registry.Entry(timestamp=1109434683.425472,
                                                                       actor=L1742),
                                '14138594607498135940': registry.Entry(timestamp=1104650760.299006,
                                                                       actor=L231),
                                '9638377965285201700': registry.Entry(timestamp=1104632228.3473179,
                                                                      actor=L1395),
                                '1aa5ec03a965669b0022': registry.Entry(timestamp=1109423781.7648139,
                                                                       actor=L1548),
                                '236d38760c6a183af6f8': registry.Entry(timestamp=1108956215.9963861,
                                                                       actor=L307),
                                '1546622807325074855': registry.Entry(timestamp=1104696117.3322141,
                                                                      actor=L661),
                                '7936621921662856627': registry.Entry(timestamp=1104650549.672792,
                                                                      actor=L1315),
                                'e87eee5c7103444d365b': registry.Entry(timestamp=1108412101.378515,
                                                                       actor=L719),
                                '941178e1441881defb2b': registry.Entry(timestamp=1108412101.4808841,
                                                                       actor=L1392),
                                '97cdf671f963709d9eb3': registry.Entry(timestamp=1108412173.8229091,
                                                                       actor=L1380),
                                '6817141969146993628': registry.Entry(timestamp=1104708982.6086359,
                                                                      actor=L1759),
                                '12545444783397887118': registry.Entry(timestamp=1104693955.28495,
                                                                       actor=L588),
                                '7a19485e947469b48f5d': registry.Entry(timestamp=1105921826.4260719,
                                                                       actor=L306),
                                '13319024784900900893': registry.Entry(timestamp=1104730507.798197,
                                                                       actor=L1504),
                                'cc5e0eda4ea20f97f227': registry.Entry(timestamp=1208019541.5957279,
                                                                       actor=L733),
                                '3313777953666434324': registry.Entry(timestamp=1104650549.6397591,
                                                                      actor=L1560),
                                '1061218531910574846': registry.Entry(timestamp=1104706912.3873279,
                                                                      actor=L642),
                                '59366674524a8992ec57': registry.Entry(timestamp=1105921808.808475,
                                                                       actor=L716),
                                '34874108ea81817dd45f': registry.Entry(timestamp=1109428828.336385,
                                                                       actor=L1503),
                                '620b2cb3deba6d946d89': registry.Entry(timestamp=1109433834.8225541,
                                                                       actor=L76),
                                '12473ee71c96cd605738': registry.Entry(timestamp=1108412101.3312759,
                                                                       actor=L1221),
                                '2496797421715521539': registry.Entry(timestamp=1104732153.4440341,
                                                                      actor=L383),
                                '4f4d746968439adc77f8': registry.Entry(timestamp=1108956726.5260489,
                                                                       actor=L1180),
                                'fc67e57428a80e5c577': registry.Entry(timestamp=1109434690.4835491,
                                                                      actor=L1544),
                                '959c6923ca073aa23ec2': registry.Entry(timestamp=1105921745.7405829,
                                                                       actor=L849),
                                '9e1868775012070da71': registry.Entry(timestamp=1109434991.6687219,
                                                                      actor=L951),
                                '479cbf4440b2fda712e3': registry.Entry(timestamp=1108956215.9968741,
                                                                       actor=L298),
                                '27642d37c9e93d88a9d3': registry.Entry(timestamp=1108412173.8300371,
                                                                       actor=L738),
                                '66d46b6a4c45495d85f': registry.Entry(timestamp=1108412101.364145,
                                                                      actor=L1579),
                                'c4491d62f5b2c77c1788': registry.Entry(timestamp=1109435027.723671,
                                                                       actor=L1272),
                                '9cab7b2aaf0861d72052': registry.Entry(timestamp=1105921513.584868,
                                                                       actor=L1468),
                                'b378f20f4218f5661db8': registry.Entry(timestamp=1109428186.7802711,
                                                                       actor=L180),
                                '38674a8406c10d8acc66': registry.Entry(timestamp=1105921513.4133351,
                                                                       actor=L850),
                                '11497005180784433127': registry.Entry(timestamp=1104730109.3140781,
                                                                       actor=L1332),
                                '11885770933734303644': registry.Entry(timestamp=1104689888.176734,
                                                                       actor=L1574),
                                '2909c2803333fa9763dd': registry.Entry(timestamp=1190665226.653671,
                                                                       actor=L1169),
                                'abd8c6c996e0bdee54ab': registry.Entry(timestamp=1105921788.513629,
                                                                       actor=L422),
                                '40318dd352f07bad2f32': registry.Entry(timestamp=1109435048.0906439,
                                                                       actor=L1025),
                                'a3707eafba7f8c29438f': registry.Entry(timestamp=1190665181.3520789,
                                                                       actor=L1314),
                                '7725879995356042119': registry.Entry(timestamp=1104633105.5330541,
                                                                      actor=L1266),
                                'c28f00da84aabe9711f8': registry.Entry(timestamp=1109428846.2577951,
                                                                       actor=L1374),
                                '8275236787514389161': registry.Entry(timestamp=1104732146.0397589,
                                                                      actor=L382),
                                '1049070116954587991': registry.Entry(timestamp=1104697494.401659,
                                                                      actor=L1179),
                                '211eb2ea127cce5956ea': registry.Entry(timestamp=1109433447.629179,
                                                                       actor=L128),
                                '6ae432c49f19b06e3dce': registry.Entry(timestamp=1109424192.8307281,
                                                                       actor=L1058),
                                '6842470814180133769': registry.Entry(timestamp=1104632241.948518,
                                                                      actor=L777),
                                '3adc62bc55fb88be1f69': registry.Entry(timestamp=1108412101.3760641,
                                                                       actor=L1313),
                                '5dc7e64e69d3a5a73189': registry.Entry(timestamp=1105921748.370198,
                                                                       actor=L458),
                                '1817218079521314969': registry.Entry(timestamp=1104632228.3319261,
                                                                      actor=L963),
                                '16897814623275256082': registry.Entry(timestamp=1104632239.2551229,
                                                                       actor=L772),
                                '986b3d704ed99c37b1e2': registry.Entry(timestamp=1208019254.894026,
                                                                       actor=L1566),
                                '7984984827063085602': registry.Entry(timestamp=1104730507.8248301,
                                                                      actor=L1736),
                                '10726820175615189179': registry.Entry(timestamp=1104650549.657733,
                                                                       actor=L1060),
                                '848b9113b67cd5bfccbc': registry.Entry(timestamp=1105921513.6032341,
                                                                       actor=L414),
                                'd368cd1b3e772c0dee3a': registry.Entry(timestamp=1109433734.2794211,
                                                                       actor=L85),
                                'eea508d94e56f68e728b': registry.Entry(timestamp=1108956215.9550979,
                                                                       actor=L1762),
                                'f675ab66721705423554': registry.Entry(timestamp=1109434712.600971,
                                                                       actor=L233),
                                '15000248107523643647': registry.Entry(timestamp=1104732488.3008361,
                                                                       actor=L1317),
                                '13176058059947371572': registry.Entry(timestamp=1104697346.2155011,
                                                                       actor=L1319),
                                '6737ab2d99858d2cb98e': registry.Entry(timestamp=1190665221.2731609,
                                                                       actor=L1279),
                                'b25d5843447a0422c30a': registry.Entry(timestamp=1108412101.3371241,
                                                                       actor=L1617),
                                '2a4f7a3dcd2f87a7532b': registry.Entry(timestamp=1105921690.9049809,
                                                                       actor=L442),
                                'e20bc13b888334ad3537': registry.Entry(timestamp=1108956448.854455,
                                                                       actor=L573),
                                '15354271914547105265': registry.Entry(timestamp=1104689747.0002921,
                                                                       actor=L1412),
                                '9829540809193203453': registry.Entry(timestamp=1104633108.691174,
                                                                      actor=L969),
                                '11244828830854864470': registry.Entry(timestamp=1104633047.078866,
                                                                       actor=L1619),
                                '9e55068b582c80b9f474': registry.Entry(timestamp=1108412101.4894359,
                                                                       actor=L1738),
                                'de5f81ed1b494d3519df': registry.Entry(timestamp=1109433597.6299551,
                                                                       actor=L61),
                                '6aa8789df5ecc4190c79': registry.Entry(timestamp=1108956850.9261429,
                                                                       actor=L1201),
                                'f8670e226436fa73128f': registry.Entry(timestamp=1109428826.413799,
                                                                       actor=L198),
                                'def59007c148e24940ad': registry.Entry(timestamp=1190664334.0511611,
                                                                       actor=L736),
                                '35269d3b8f3f78114257': registry.Entry(timestamp=1108956796.8554609,
                                                                       actor=L1209),
                                'fa59d03a167a4c1b94ff': registry.Entry(timestamp=1109434755.246258,
                                                                       actor=L92),
                                '10330519763115726681': registry.Entry(timestamp=1104689888.177563,
                                                                       actor=L1577),
                                '93a74d12b66f1bf6d440': registry.Entry(timestamp=1109677336.731226,
                                                                       actor=L131),
                                '4a3c84658bd78b1029a1': registry.Entry(timestamp=1208019245.830636,
                                                                       actor=L1262),
                                '5d52906b91dc36916500': registry.Entry(timestamp=1104807950.912137,
                                                                       actor=L1727),
                                '54573033a0f923d876e0': registry.Entry(timestamp=1109422775.108053,
                                                                       actor=L1036),
                                '8511836882149982016': registry.Entry(timestamp=1104650706.713083,
                                                                      actor=L1061),
                                '120d37656e5a1a12158e': registry.Entry(timestamp=1109428443.6542909,
                                                                       actor=L187),
                                '4667264518391135515': registry.Entry(timestamp=1104650724.1308751,
                                                                      actor=L412),
                                'e94c4dff11c20c4a0886': registry.Entry(timestamp=1104797071.7125549,
                                                                       actor=L1518),
                                '232be96254a60b1185f4': registry.Entry(timestamp=1109428842.672349,
                                                                       actor=L577),
                                '5591050765793200711': registry.Entry(timestamp=1104732505.688601,
                                                                      actor=L235),
                                '12051635174327115429': registry.Entry(timestamp=1104650712.6820021,
                                                                       actor=L1580),
                                '9fe8821ff61c3fe3b77d': registry.Entry(timestamp=1109422775.0955131,
                                                                       actor=L1545),
                                '56191cb3e8143011d87c': registry.Entry(timestamp=1190665181.347971,
                                                                       actor=L472),
                                '5274326361166066280': registry.Entry(timestamp=1104693745.0998559,
                                                                      actor=L665),
                                '13270445787827545889': registry.Entry(timestamp=1104730109.3088651,
                                                                       actor=L1561),
                                'c223f740d0189de07951': registry.Entry(timestamp=1109435170.1033919,
                                                                       actor=L1737),
                                '9ed64c1f46f388ef377e': registry.Entry(timestamp=1108412240.3527069,
                                                                       actor=L1252),
                                '1a3edd7a42ba08472afd': registry.Entry(timestamp=1108956448.852829,
                                                                       actor=L572),
                                '55786e30b2bf1b3ea69f': registry.Entry(timestamp=1109428799.6917369,
                                                                       actor=L1164),
                                '4442827039649434997': registry.Entry(timestamp=1104650930.7920511,
                                                                      actor=L1568),
                                '322fb4bc7605aa8653e2': registry.Entry(timestamp=1109435009.982374,
                                                                       actor=L1620),
                                '474b80e51e808fed1a99': registry.Entry(timestamp=1109433451.294275,
                                                                       actor=L49),
                                '12128037699416130148': registry.Entry(timestamp=1104732146.0393341,
                                                                       actor=L1399),
                                '6f3a7f7d336523b08bd4': registry.Entry(timestamp=1109422775.123138,
                                                                       actor=L1170),
                                '22eb057b0621169328c9': registry.Entry(timestamp=1108956215.9773271,
                                                                       actor=L1507),
                                '13387220976027820258': registry.Entry(timestamp=1104650712.644146,
                                                                       actor=L1749),
                                '7a89bcf8d307b258b3b4': registry.Entry(timestamp=1109435009.9851551,
                                                                       actor=L147),
                                '672462e5d7d6c8606fe3': registry.Entry(timestamp=1109434948.9922681,
                                                                       actor=L36),
                                'bb9c4f22765c549d20f1': registry.Entry(timestamp=1208019537.386277,
                                                                       actor=L518),
                                '708093d3f5efae9ceb81': registry.Entry(timestamp=1109435009.994391,
                                                                       actor=L846),
                                '67eeb2429b63101a4ec7': registry.Entry(timestamp=1108412161.574615,
                                                                       actor=L1751),
                                'ca30c87e605ba765be06': registry.Entry(timestamp=1109428804.8202569,
                                                                       actor=L1331),
                                '1679989706457713520': registry.Entry(timestamp=1104706912.3876929,
                                                                      actor=L644),
                                'e18028cacd7efe69dfbb': registry.Entry(timestamp=1190665154.678051,
                                                                       actor=L511),
                                '6402116433048299654': registry.Entry(timestamp=1104650712.6671181,
                                                                      actor=L1510),
                                '70ca891a948da6b4fd73': registry.Entry(timestamp=1109422775.1296489,
                                                                       actor=L1034),
                                '15511116157062632786': registry.Entry(timestamp=1104650712.6740661,
                                                                       actor=L1035),
                                'fff687e48591806e7d56': registry.Entry(timestamp=1109435168.3178489,
                                                                       actor=L955),
                                'b774260d0676ba628669': registry.Entry(timestamp=1104797063.3239031,
                                                                       actor=L579),
                                'b714558827a1934689eb': registry.Entry(timestamp=1109435027.72104,
                                                                       actor=L1271),
                                '16136617492328534660': registry.Entry(timestamp=1104650949.250061,
                                                                       actor=L1447),
                                'dee2d9a8289d27ac176a': registry.Entry(timestamp=1109424028.7127371,
                                                                       actor=L204),
                                '804e5b1a3b2aadf7c001': registry.Entry(timestamp=1109423781.762228,
                                                                       actor=L1547),
                                'bd70c7c47be23dba293f': registry.Entry(timestamp=1109433735.9576671,
                                                                       actor=L83),
                                '4cb50eebe02b70a0d71b': registry.Entry(timestamp=1190664334.091352,
                                                                       actor=L1567),
                                '9564f27dcab30da4c8d4': registry.Entry(timestamp=1190664334.0540831,
                                                                       actor=L1039),
                                '25c2e6f96744ae60c374': registry.Entry(timestamp=1105921513.572356,
                                                                       actor=L397),
                                'CCDF40493E712274L': registry.Entry(timestamp=1104796672.1500449,
                                                                    actor=L1658),
                                '93ea785fea4a1506079a': registry.Entry(timestamp=1108412161.5768311,
                                                                       actor=L265),
                                '10871997212631801029': registry.Entry(timestamp=1104730109.3334141,
                                                                       actor=L1563),
                                '658c0f7cf8f1c49b6a69': registry.Entry(timestamp=1208019537.388222,
                                                                       actor=L554),
                                '73d4b6bd3504795305a1': registry.Entry(timestamp=1109424445.3275061,
                                                                       actor=L207),
                                '8060076283853931247': registry.Entry(timestamp=1104650549.665045,
                                                                      actor=L1),
                                '7472656884655288975': registry.Entry(timestamp=1104689853.1316221,
                                                                      actor=L1471),
                                'fd0e0dcd73af9e72f597': registry.Entry(timestamp=1108956216.009995,
                                                                       actor=L890),
                                '17980192334006365197': registry.Entry(timestamp=1104632228.403507,
                                                                       actor=L1578),
                                '7fd28421399c0260a1a0': registry.Entry(timestamp=1109428731.5971761,
                                                                       actor=L191),
                                '4178227206424925539': registry.Entry(timestamp=1104650549.674288,
                                                                      actor=L1401),
                                '15250013233234179905': registry.Entry(timestamp=1104632228.3750589,
                                                                       actor=L967),
                                '6c85152f239871975017': registry.Entry(timestamp=1109428208.878855,
                                                                       actor=L1553),
                                '3cb26424481623ed41bc': registry.Entry(timestamp=1108956926.1981299,
                                                                       actor=L1206),
                                '1c4a4e54eec83f776e4a': registry.Entry(timestamp=1109424192.8323901,
                                                                       actor=L1059),
                                '12946925928954107809': registry.Entry(timestamp=1104730507.796433,
                                                                       actor=L717),
                                '92d4a78cea106df07c2c': registry.Entry(timestamp=1108956796.853735,
                                                                       actor=L1385),
                                '14095654525563810214': registry.Entry(timestamp=1104694007.8913209,
                                                                       actor=L587),
                                'a14d85d55467ffe04ee0': registry.Entry(timestamp=1109435018.4971809,
                                                                       actor=L1618),
                                'c25353745b522913f4c2': registry.Entry(timestamp=1109424299.653085,
                                                                       actor=L210),
                                '659985c7578a877b07e3': registry.Entry(timestamp=1109428804.8175659,
                                                                       actor=L1330),
                                '4f3f54f1d8db5a25f118': registry.Entry(timestamp=1108956216.005373,
                                                                       actor=L1557),
                                '13661059783025868973': registry.Entry(timestamp=1104633042.4138801,
                                                                       actor=L775),
                                '7aa131ceb0eae191a3ed': registry.Entry(timestamp=1108956833.1141219,
                                                                       actor=L1761),
                                '6055406963319936966': registry.Entry(timestamp=1104650753.2101431,
                                                                      actor=L1581),
                                '354f3356b414dbdf6595': registry.Entry(timestamp=1109435083.837661,
                                                                       actor=L51),
                                '10927938414203847443': registry.Entry(timestamp=1104689958.5300021,
                                                                       actor=L649),
                                '420e55efa0fb8d8f2ffd': registry.Entry(timestamp=1109428835.814178,
                                                                       actor=L175),
                                'fd6a40ab5331a449ac99': registry.Entry(timestamp=1104797063.2925529,
                                                                       actor=L1513),
                                '1359982258694374825': registry.Entry(timestamp=1104632228.379292,
                                                                      actor=L1322),
                                '10593314374053890933': registry.Entry(timestamp=1104730507.788162,
                                                                       actor=L1031),
                                'ad509debf6bb51e095c9': registry.Entry(timestamp=1108412101.357022,
                                                                       actor=L1799),
                                'b33414f37886533390d2': registry.Entry(timestamp=1108412161.582691,
                                                                       actor=L269),
                                'f5a54a967633535bf134': registry.Entry(timestamp=1109422948.6272831,
                                                                       actor=L166),
                                '10103513020179766570': registry.Entry(timestamp=1104690335.904788,
                                                                       actor=L654),
                                'c757003da8382520250d': registry.Entry(timestamp=1105921822.3753741,
                                                                       actor=L1411),
                                '261ec3b86d5f1af30a43': registry.Entry(timestamp=1109435160.16693,
                                                                       actor=L1268),
                                '14107852319538388771': registry.Entry(timestamp=1104730507.833338,
                                                                       actor=L1377),
                                '73f50a3f60d178768e5d': registry.Entry(timestamp=1104807950.8976121,
                                                                       actor=L904),
                                'ef7b8185a1e8d3a1d99e': registry.Entry(timestamp=1208019245.8276751,
                                                                       actor=L1731),
                                'f9ab36734295b51f1fb9': registry.Entry(timestamp=1109435170.1005421,
                                                                       actor=L116),
                                '3ed58789fe9a7d9623fa': registry.Entry(timestamp=1104797063.3068709,
                                                                       actor=L1622),
                                '11549355846312153998': registry.Entry(timestamp=1104632228.3814001,
                                                                       actor=L1403),
                                '3191a13927a42a0aca34': registry.Entry(timestamp=1109428764.7491829,
                                                                       actor=L20),
                                '9ca23758d3e14b14e22f': registry.Entry(timestamp=1105921548.3496211,
                                                                       actor=L990),
                                '4138178436990957034': registry.Entry(timestamp=1104732505.688319,
                                                                      actor=L234),
                                '6920636786683624616': registry.Entry(timestamp=1104690523.1329401,
                                                                      actor=L734),
                                '32b6411e86ed3305be63': registry.Entry(timestamp=1108956726.5277021,
                                                                       actor=L1181),
                                '14726587180619911525': registry.Entry(timestamp=1104633035.78582,
                                                                       actor=L783),
                                'a125bcaed7f5954b9150': registry.Entry(timestamp=1109422775.1189499,
                                                                       actor=L712),
                                '1564538181099476570': registry.Entry(timestamp=1104690401.654279,
                                                                      actor=L1732),
                                'ac567c51e8219e69ff16': registry.Entry(timestamp=1190664334.070976,
                                                                       actor=L987),
                                'f4e883b36a48f3be4880': registry.Entry(timestamp=1109422945.6852801,
                                                                       actor=L167),
                                'dfd2c79df992922d1acf': registry.Entry(timestamp=1105921540.9413459,
                                                                       actor=L1095),
                                '12182569062741163979': registry.Entry(timestamp=1104730109.3149381,
                                                                       actor=L1370),
                                'ca15ef2c3a7701c12458': registry.Entry(timestamp=1109423159.0988619,
                                                                       actor=L225),
                                '1b5a49fb0fec6944ecc4': registry.Entry(timestamp=1105921513.538332,
                                                                       actor=L574),
                                'a7bd903423cd5317bd7b': registry.Entry(timestamp=1109428831.4499919,
                                                                       actor=L1740),
                                '17801320630458131755': registry.Entry(timestamp=1104689816.700052,
                                                                       actor=L1263),
                                '2d3ff26bf3a1ccdbda01': registry.Entry(timestamp=1109428838.222214,
                                                                       actor=L847),
                                '3dda188fab7c5720065a': registry.Entry(timestamp=1208019245.8287461,
                                                                       actor=L546),
                                '13838842964897476745': registry.Entry(timestamp=1104650720.799705,
                                                                       actor=L1734),
                                'f96001099601a04981f6': registry.Entry(timestamp=1108956537.787472,
                                                                       actor=L1213),
                                '6461598025166001448': registry.Entry(timestamp=1104689796.4098401,
                                                                      actor=L609),
                                'cea976a1318c7f6a6ec': registry.Entry(timestamp=1109434693.650279,
                                                                      actor=L124),
                                '7798158345955886274': registry.Entry(timestamp=1104650549.6464159,
                                                                      actor=L1021),
                                '3cadcfebb3425343d2ae': registry.Entry(timestamp=1109434660.0012491,
                                                                       actor=L103),
                                '5b74f62f6857b7956095': registry.Entry(timestamp=1208019605.013859,
                                                                       actor=L1472),
                                '2956948422716100561': registry.Entry(timestamp=1104706912.386812,
                                                                      actor=L643),
                                '4131740470354140357': registry.Entry(timestamp=1104697377.9553559,
                                                                      actor=L669),
                                '740e543a73fba8ae453f': registry.Entry(timestamp=1109677327.1529441,
                                                                       actor=L1582),
                                '8ceb80a0f5e5a7b0bbd6': registry.Entry(timestamp=1208019554.7395229,
                                                                       actor=L1320),
                                'e568157c9501ba7cfc6a': registry.Entry(timestamp=1109428462.781116,
                                                                       actor=L1165),
                                'c700b53d7a40117bd126': registry.Entry(timestamp=1109435168.315073,
                                                                       actor=L956),
                                '2805739992860418134': registry.Entry(timestamp=1104650712.650219,
                                                                      actor=L1043),
                                'a80d84152cb05bbf1286': registry.Entry(timestamp=1109424025.394774,
                                                                       actor=L201),
                                '8549478301856461533': registry.Entry(timestamp=1104730507.77914,
                                                                      actor=L310),
                                '400632f1c4d59068aadc': registry.Entry(timestamp=1104797063.3278401,
                                                                       actor=L1390),
                                '3bcc6e02355a4489272b': registry.Entry(timestamp=1109434795.845222,
                                                                       actor=L1511),
                                '12904228506947022660': registry.Entry(timestamp=1104632228.327944,
                                                                       actor=L740),
                                'af6bc0bdd2da549d34ab': registry.Entry(timestamp=1109435027.7326839,
                                                                       actor=L1259),
                                '978002a771fdb82dea39': registry.Entry(timestamp=1109435124.705168,
                                                                       actor=L1404),
                                '8ab96d54de6dae117484': registry.Entry(timestamp=1109428846.255095,
                                                                       actor=L1373),
                                '905b734d21990d905889': registry.Entry(timestamp=1109422775.0432079,
                                                                       actor=L1371),
                                '8608183716299200486': registry.Entry(timestamp=1104632228.3480451,
                                                                      actor=L1743),
                                '7436199748876259015': registry.Entry(timestamp=1104696844.4145091,
                                                                      actor=L718),
                                '63d95a5f3af1685a4628': registry.Entry(timestamp=1104807978.8575661,
                                                                       actor=L228),
                                '69de3657b02e113b0f93': registry.Entry(timestamp=1108412173.8187251,
                                                                       actor=L237),
                                '14955675966070121265': registry.Entry(timestamp=1104650712.6410279,
                                                                       actor=L1413),
                                'f607f8a7a922d909c959': registry.Entry(timestamp=1105921825.2458611,
                                                                       actor=L1037),
                                '33f0080422fa3454881b': registry.Entry(timestamp=1208019263.446157,
                                                                       actor=L544),
                                '81ea31f2e40de4411915': registry.Entry(timestamp=1108956454.267065,
                                                                       actor=L1032),
                                'ea1042a44339a6b6299c': registry.Entry(timestamp=1108956216.0383761,
                                                                       actor=L1543),
                                '4f7773f6e389793f5cff': registry.Entry(timestamp=1109428842.6749821,
                                                                       actor=L578),
                                '77c7ce5c863dd5a05a76': registry.Entry(timestamp=1109422775.0328751,
                                                                       actor=L1583),
                                '1011012714027468268': registry.Entry(timestamp=1104650712.6589899,
                                                                      actor=L1318),
                                'c171aaf4622a67eec25f': registry.Entry(timestamp=1105921745.787854,
                                                                       actor=L460),
                                '8238bb4120ed257048c5': registry.Entry(timestamp=1208019607.900213,
                                                                       actor=L1029),
                                '13286087984584598130': registry.Entry(timestamp=1104650712.6619079,
                                                                       actor=L1753),
                                '96f0ef4cbdcdc2586bf0': registry.Entry(timestamp=1109428182.139416,
                                                                       actor=L1741),
                                '40a8e69a8169b7a993b1': registry.Entry(timestamp=1108956889.0060489,
                                                                       actor=L1509),
                                '10e10ac18640c6dd2364': registry.Entry(timestamp=1109434627.705112,
                                                                       actor=L1328),
                                '4939350837483695449': registry.Entry(timestamp=1104730109.317359,
                                                                      actor=L1726),
                                'daa4bbacf74bab652f0a': registry.Entry(timestamp=1109434477.727283,
                                                                       actor=L992),
                                '7451b642c3dd07bfa37e': registry.Entry(timestamp=1208019554.7398829,
                                                                       actor=L558),
                                'c6395c42b17dc6409a98': registry.Entry(timestamp=1108956695.1835511,
                                                                       actor=L1554),
                                'ce21e0cc674c8dff1aa1': registry.Entry(timestamp=1109428875.2832229,
                                                                       actor=L1053),
                                'f1b64b96203dc1031e47': registry.Entry(timestamp=1109433805.3580141,
                                                                       actor=L63),
                                'f2761198c8015e58297d': registry.Entry(timestamp=1109422775.0365369,
                                                                       actor=L1730),
                                '987ba6d80c536ef72fd3': registry.Entry(timestamp=1104796957.85256,
                                                                       actor=L1096),
                                '112755c6b7b0197ca6bb': registry.Entry(timestamp=1105921513.5788419,
                                                                       actor=L1264),
                                '335fd96b953d2239db53': registry.Entry(timestamp=1109433926.7197659,
                                                                       actor=L69),
                                '2c4f6289354906ecf08': registry.Entry(timestamp=1109424447.4493661,
                                                                      actor=L1556),
                                '11512313525346285370': registry.Entry(timestamp=1104730109.340476,
                                                                       actor=L1400),
                                '477d1d63d2661835065d': registry.Entry(timestamp=1105921513.564682,
                                                                       actor=L1278),
                                '14095783355500097386': registry.Entry(timestamp=1104633023.2535551,
                                                                       actor=L1168),
                                '84af1be6f390fc4f0d92': registry.Entry(timestamp=1108412234.059459,
                                                                       actor=L1220),
                                '76105c3de42692569c7f': registry.Entry(timestamp=1190665257.4738071,
                                                                       actor=L513),
                                'c97d9bb0c2aa5df61e6e': registry.Entry(timestamp=1108412101.454735,
                                                                       actor=L722),
                                'dc10179ce6eb719eddec': registry.Entry(timestamp=1105921587.3464301,
                                                                       actor=L465),
                                '132bd817a0e8acb0485e': registry.Entry(timestamp=1108956833.1580081,
                                                                       actor=L1203),
                                '40e51ffc174da6c81c4f': registry.Entry(timestamp=1108412101.37217,
                                                                       actor=L1057),
                                '5292533547202728044': registry.Entry(timestamp=1104730442.7894969,
                                                                      actor=L1625),
                                'e5fb3e230d899e6a15ec': registry.Entry(timestamp=1208019537.3884959,
                                                                       actor=L559),
                                'f84c449eddb7e174f514': registry.Entry(timestamp=1108956539.883023,
                                                                       actor=L1389),
                                '16495268673511082035': registry.Entry(timestamp=1104795314.0476921,
                                                                       actor=L309),
                                '89b4ca205464b571e41e': registry.Entry(timestamp=1109428157.5395341,
                                                                       actor=L959),
                                '8a9f1ac419253f7817c7': registry.Entry(timestamp=1105921826.4286239,
                                                                       actor=L305),
                                '9462070805789713288': registry.Entry(timestamp=1104650549.652365,
                                                                      actor=L411),
                                '15604201270503278878': registry.Entry(timestamp=1104632228.3436141,
                                                                       actor=L1396),
                                '12079799893167868995': registry.Entry(timestamp=1104693742.1302421,
                                                                       actor=L658),
                                'daf060d1d66ad487dee3': registry.Entry(timestamp=1109435117.514183,
                                                                       actor=L1756),
                                'c88c9deae9a8bad90c4': registry.Entry(timestamp=1190664334.047466,
                                                                      actor=L510),
                                '5217137786238671049': registry.Entry(timestamp=1104632241.9482341,
                                                                      actor=L1746),
                                '1f966172227f701d36a1': registry.Entry(timestamp=1109434798.857053,
                                                                       actor=L1056),
                                '7522505065968084182': registry.Entry(timestamp=1104730507.792691,
                                                                      actor=L1506),
                                '2ce2546b3a61d585544e': registry.Entry(timestamp=1108412161.584934,
                                                                       actor=L272),
                                '10579116576104148034': registry.Entry(timestamp=1104632797.6333671,
                                                                       actor=L1570),
                                'bc6686a069873608f287': registry.Entry(timestamp=1109434503.0064521,
                                                                       actor=L99),
                                'cac21146f6ccd1384dcb': registry.Entry(timestamp=1108956794.6392231,
                                                                       actor=L1398),
                                '12427553908187455670': registry.Entry(timestamp=1104730109.330364,
                                                                       actor=L1735),
                                '4edd14e178ad0c694a5f': registry.Entry(timestamp=1104807944.3474181,
                                                                       actor=L1512),
                                '1f894cedda7a5116c672': registry.Entry(timestamp=1109433555.5110941,
                                                                       actor=L26),
                                '11346868527983282560': registry.Entry(timestamp=1104632803.6578569,
                                                                       actor=L1257),
                                '5b87ae2914a9f9836ec7': registry.Entry(timestamp=1208019554.739634,
                                                                       actor=L557),
                                '7c9da28e49e64a268faa': registry.Entry(timestamp=1208019245.8292351,
                                                                       actor=L986),
                                '12280374078573952893': registry.Entry(timestamp=1104689747.0388479,
                                                                       actor=L610),
                                '5186614581370432354': registry.Entry(timestamp=1104730776.1944089,
                                                                      actor=L366),
                                'd3fa83e2175f56e2183f': registry.Entry(timestamp=1109434779.0693159,
                                                                       actor=L1505),
                                '3719337025926476596': registry.Entry(timestamp=1104650549.6292789,
                                                                      actor=L1062),
                                '7708682ba51a597e4483': registry.Entry(timestamp=1109427882.6983581,
                                                                       actor=L960),
                                '3d7fe3f0661198add7d2': registry.Entry(timestamp=1108956216.0018411,
                                                                       actor=L1323),
                                'b6d022a6aab1a9c58c67': registry.Entry(timestamp=1105921513.5993609,
                                                                       actor=L1406),
                                '7838193153830263651': registry.Entry(timestamp=1104730507.7985001,
                                                                      actor=L1446),
                                '994f72d124ba4ab3e643': registry.Entry(timestamp=1109435124.707993,
                                                                       actor=L1405),
                                '5ee3a50d3351e3b67fd4': registry.Entry(timestamp=1104807950.9019289,
                                                                       actor=L1022),
                                '10584963968992807980': registry.Entry(timestamp=1104730109.3000181,
                                                                       actor=L1626),
                                '63af8fe6397a4ec62ec8': registry.Entry(timestamp=1104807978.85042,
                                                                       actor=L944),
                                '202f42bea33bd7dcb5c7': registry.Entry(timestamp=1105921808.8114059,
                                                                       actor=L715),
                                '129f5ab2812ebd35a6f3': registry.Entry(timestamp=1108956527.0244949,
                                                                       actor=L1215),
                                '8d2fd9ab021f90ee5c23': registry.Entry(timestamp=1208019541.593894,
                                                                       actor=L549),
                                '2737335135250149149': registry.Entry(timestamp=1104650724.1311619,
                                                                      actor=L413),
                                'cf3306171571f5115689': registry.Entry(timestamp=1109435018.505995,
                                                                       actor=L889),
                                '15550032082523474268': registry.Entry(timestamp=1104650556.4493201,
                                                                       actor=L1572),
                                'a9cb48105a7013552f52': registry.Entry(timestamp=1108412234.392565,
                                                                       actor=L286),
                                '1245e3bda58496bdf7e7': registry.Entry(timestamp=1105921513.4643559,
                                                                       actor=L467),
                                '1347a00d734365bfd85e': registry.Entry(timestamp=1108956747.616488,
                                                                       actor=L1382),
                                '3491372217552124879': registry.Entry(timestamp=1104694604.2031541,
                                                                      actor=L1754),
                                '13101820419664547343': registry.Entry(timestamp=1104632307.7753921,
                                                                       actor=L1569),
                                '48c31983ab36c2b93869': registry.Entry(timestamp=1109422775.113838,
                                                                       actor=L576),
                                '2226060574216469791': registry.Entry(timestamp=1104795314.147552,
                                                                      actor=L1261),
                                '9191949582763768590': registry.Entry(timestamp=1104732153.4437671,
                                                                      actor=L1760),
                                '11009507096081710421': registry.Entry(timestamp=1104650949.2503321,
                                                                       actor=L1448),
                                'd6b5b4340e8822d2762c': registry.Entry(timestamp=1109434804.450887,
                                                                       actor=L952),
                                '11031015219216838346': registry.Entry(timestamp=1104730109.341886,
                                                                       actor=L1750),
                                'bb790ac1a0ee7ed3ea5b': registry.Entry(timestamp=1109434798.854404,
                                                                       actor=L1055),
                                '1d9f30f9466014fd9845': registry.Entry(timestamp=1208019245.8296211,
                                                                       actor=L1402),
                                'c136252aeda06b05ab25': registry.Entry(timestamp=1108412101.4477329,
                                                                       actor=L1327),
                                'd81a12a2169de556f93d': registry.Entry(timestamp=1108956488.748338,
                                                                       actor=L1023),
                                '8096643624464055522': registry.Entry(timestamp=1104633049.924382,
                                                                      actor=L781),
                                '40e992d83eee6dfcc7a5': registry.Entry(timestamp=1108412101.3672991,
                                                                       actor=L293),
                                'c16a270d21302658f53d': registry.Entry(timestamp=1108956776.0309,
                                                                       actor=L1211),
                                '35b913d9f1a9ff04226a': registry.Entry(timestamp=1109435098.7016151,
                                                                       actor=L1030),
                                '3112541654131017587': registry.Entry(timestamp=1104633023.2538221,
                                                                      actor=L822),
                                '310e5faab910f546eb10': registry.Entry(timestamp=1109434795.8531029,
                                                                       actor=L1546),
                                '33c2fbb146d136f5d402': registry.Entry(timestamp=1109428835.8112259,
                                                                       actor=L1624),
                                '14245085994013281857': registry.Entry(timestamp=1104640325.6669509,
                                                                       actor=L1254),
                                '18d8a761281277ebaf47': registry.Entry(timestamp=1208019607.90014,
                                                                       actor=L1028),
                                '16622057499147950833': registry.Entry(timestamp=1104697074.9701481,
                                                                       actor=L634),
                                '10084807298204554591': registry.Entry(timestamp=1104730507.8413301,
                                                                       actor=L1054),
                                '2553436941368336606': registry.Entry(timestamp=1104632803.6574349,
                                                                      actor=L1258),
                                '8343b425fd8ebf32117': registry.Entry(timestamp=1105921548.351846,
                                                                      actor=L991),
                                '6752b9d510ea35cf88d9': registry.Entry(timestamp=1190664334.057488,
                                                                       actor=L404),
                                '18af9ec7344533271914': registry.Entry(timestamp=1109435018.501241,
                                                                       actor=L1277),
                                '16060064330232869464': registry.Entry(timestamp=1104730109.3031399,
                                                                       actor=L1739)})
L114 = envs.Env(parent=L84)
L112 = actors.Actor(env=envs.Env(parent=L114),
                    script=L89)
L284 = actors.Actor(env=envs.Env(parent=L240),
                    script=L286)
L440 = actors.Actor(env=envs.Env(parent=L416),
                    script=L442)

L907.define(var='box',
            value=L580)

L907.define(var='makemailbox',
             value=L925)

L907.define(var='Foo',
             value=L939)

L907.define(var='mailbox',
             value=L904)

L907.define(var='maildirectory',
             value=L945)

L908.define(var='false',
             value=L581)

L908.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L908.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L908.define(var='makestamp',
             value=builtin.StampMaker())

L908.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L908.define(var='makebox',
             value=L913)

L908.define(var='true',
             value=L914)

L908.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L908.define(var='if',
             value=actors.Actor(env=L908,
                                script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0,
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             selector='true:then:else:')],
                                                     next_serial_id=1)))

L1270.define(var='node',
              value=L103)

L1270.define(var='asker',
              value=L1268)

L106.define(var='yesbox',
             value=L107)

L106.define(var='askernode',
             value=L104)

L106.define(var='question',
             value=L122)

L106.define(var='nobox',
             value=L123)

L50.define(var='playgame',
            value=L51)

L50.define(var='call',
            value=L56)

L50.define(var='makebranch',
            value=L61)

L50.define(var='makeguess',
            value=L83)

L50.define(var='root',
            value=L103)

L24.define(var='box',
            value=L48)

L24.define(var='newanimalgame',
            value=L49)

L24.define(var='makemailbox',
            value=L152)

L24.define(var='animalgame',
            value=L166)

L24.define(var='mailbox',
            value=L213)

L24.define(var='maildirectory',
            value=L220)

L24.define(var='Foo',
            value=L222)

L25.define(var='false',
            value=L26)

L25.define(var='numberguard',
            value=builtin.TypeGuard(sample_instance=0))

L25.define(var='listguard',
            value=builtin.TypeGuard(sample_instance=()))

L25.define(var='makestamp',
            value=builtin.StampMaker())

L25.define(var='booleanguard',
            value=builtin.TypeGuard(sample_instance=True))

L25.define(var='makebox',
            value=L36)

L25.define(var='true',
            value=L37)

L25.define(var='stringguard',
            value=builtin.TypeGuard(sample_instance=''))

L25.define(var='if',
            value=actors.Actor(env=L25,
                               script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                   inner_map={}),
                                                                            serial_id=0,
                                                                            parameters=['test',
                                                                                        'yes',
                                                                                        'no'],
                                                                            selector='true:then:else:')],
                                                    next_serial_id=1)))

L962.define(var='question',
             value=L960)

L209.define(var='box',
             value=L170)

L209.define(var='guess',
             value=L207)

L209.define(var='animal',
             value=L210)

L23.define(var='makequestion',
            value=L21)

L23.define(var='makeguess',
            value=L204)

L23.define(var='gamebox',
            value=L170)

L357.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L357),
                                script=L340))

L357.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=())))

L357.define(var='mailbox',
             value=L355)

L311.define(var='box',
             value=L335)

L311.define(var='makemailbox',
             value=L336)

L311.define(var='Foo',
             value=L350)

L311.define(var='maildirectory',
             value=L353)

L311.define(var='mailbox',
             value=L355)

L312.define(var='false',
             value=L313)

L312.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L312.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L312.define(var='makestamp',
             value=builtin.StampMaker())

L312.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L312.define(var='makebox',
             value=L323)

L312.define(var='true',
             value=L324)

L312.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L312.define(var='if',
             value=actors.Actor(env=L312,
                                script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0,
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             selector='true:then:else:')],
                                                     next_serial_id=1)))

L110.define(var='yesbox',
             value=builtin.Box(initial_value=L112))

L110.define(var='askernode',
             value=L108)

L110.define(var='question',
             value=L116)

L110.define(var='nobox',
             value=builtin.Box(initial_value=L118))

L774.define(var='sender',
             value=L775)

L774.define(var='inbox',
             value=L777)

L774.define(var='mailbox',
             value=L772)

L741.define(var='box',
             value=L757)

L741.define(var='makemailbox',
             value=L758)

L741.define(var='mailbox',
             value=L772)

L741.define(var='maildirectory',
             value=L779)

L741.define(var='message',
             value=L781)

L741.define(var='Foo',
             value=L785)

L741.define(var='tome',
             value=L775)

L742.define(var='true',
             value=L743)

L742.define(var='makebox',
             value=L749)

L742.define(var='false',
             value=L750)

L742.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L281.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=(L284,))))

L281.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L281),
                                script=L269))

L281.define(var='mailbox',
             value=L279)

L240.define(var='box',
             value=L264)

L240.define(var='makemailbox',
             value=L265)

L240.define(var='mailbox',
             value=L279)

L240.define(var='maildirectory',
             value=L289)

L240.define(var='message',
             value=L284)

L240.define(var='Foo',
             value=L291)

L241.define(var='false',
             value=L242)

L241.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L241.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L241.define(var='makestamp',
             value=builtin.StampMaker())

L241.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L241.define(var='makebox',
             value=L252)

L241.define(var='true',
             value=L253)

L241.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L241.define(var='if',
             value=actors.Actor(env=L241,
                                script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0,
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             selector='true:then:else:')],
                                                     next_serial_id=1)))

L416.define(var='box',
             value=L434)

L416.define(var='makemailbox',
             value=L415)

L416.define(var='mailbox',
             value=L435)

L416.define(var='makeballot',
             value=L458)

L416.define(var='maildirectory',
             value=L463)

L416.define(var='message',
             value=L440)

L416.define(var='Foo',
             value=L465)

L417.define(var='false',
             value=L398)

L417.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L417.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L417.define(var='makestamp',
             value=builtin.StampMaker())

L417.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L417.define(var='makebox',
             value=L422)

L417.define(var='true',
             value=L423)

L417.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L417.define(var='if',
             value=actors.Actor(env=L417,
                                script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0,
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             selector='true:then:else:')],
                                                     next_serial_id=1)))

L853._add_result(result=L855,
                  actor=L849)

L856._add_result(result=L858,
                  actor=L849)

L860._add_result(result=L465,
                  actor=L849)

L863._add_result(result=L434,
                  actor=L849)

L865._add_result(result=L423,
                  actor=L849)

L867._add_result(result=L398,
                  actor=L849)

L869._add_result(result=L871,
                  actor=L849)

L874._add_result(result=L463,
                  actor=L849)

L877._add_result(result=L435,
                  actor=L849)

L881._add_result(result=L883,
                  actor=L849)

L885._add_result(result='Error: Unbound: makek',
                  actor=L849)

L887._add_result(result=L458,
                  actor=L849)

L1167.define(var='question',
              value=L1165)

L519.define(var='box',
             value=L543)

L519.define(var='makemailbox',
             value=L518)

L519.define(var='Foo',
             value=L544)

L519.define(var='maildirectory',
             value=L547)

L519.define(var='mailbox',
             value=L549)

L520.define(var='false',
             value=L521)

L520.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L520.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L520.define(var='makestamp',
             value=builtin.StampMaker())

L520.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L520.define(var='makebox',
             value=L531)

L520.define(var='true',
             value=L532)

L520.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L520.define(var='if',
             value=actors.Actor(env=L520,
                                script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0,
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             selector='true:then:else:')],
                                                     next_serial_id=1)))

L120.define(var='guessernode',
             value=L118)

L120.define(var='animal',
             value=L121)

L1586._add_result(result=L1588,
                   actor=L1582)

L1589._add_result(result=L1372,
                   actor=L1582)

L1592._add_result(result=L222,
                   actor=L1582)

L1595._add_result(result=L48,
                   actor=L1582)

L1597._add_result(result=L37,
                   actor=L1582)

L1599._add_result(result=L26,
                   actor=L1582)

L1601._add_result(result=L713,
                   actor=L1582)

L1604._add_result(result=L220,
                   actor=L1582)

L1607._add_result(result=L213,
                   actor=L1582)

L1611._add_result(result=L166,
                   actor=L1582)

L168._add_result(result=L170,
                  actor=L198)

L199._add_result(result=L204,
                  actor=L198)

L205._add_result(result=L207,
                  actor=L198)

L211._add_result(result=L171,
                  actor=L198)

L1613._add_result(result=L49,
                   actor=L1582)

L129._add_result(result=L56,
                  actor=L131)

L132._add_result(result=L61,
                  actor=L131)

L134._add_result(result=L83,
                  actor=L131)

L136._add_result(result='Error: No matching method: holding:',
                  actor=L131)

L138._add_result(result=L103,
                  actor=L131)

L140._add_result(result=L142,
                  actor=L131)

L145._add_result(result=L147,
                  actor=L131)

L150._add_result(result=L51,
                  actor=L131)

L475.define(var='box',
             value=L493)

L475.define(var='makemailbox',
             value=L494)

L475.define(var='Foo',
             value=L508)

L475.define(var='maildirectory',
             value=L511)

L475.define(var='mailbox',
             value=L472)

L476.define(var='false',
             value=L477)

L476.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L476.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L476.define(var='makestamp',
             value=builtin.StampMaker())

L476.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L476.define(var='makebox',
             value=L487)

L476.define(var='true',
             value=L405)

L476.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L476.define(var='if',
             value=actors.Actor(env=L476,
                                script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0,
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             selector='true:then:else:')],
                                                     next_serial_id=1)))

L823.define(var='false',
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

L823.define(var='makebox',
             value=builtin.BoxMaker())

L823.define(var='true',
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

L823.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L1283._add_result(result=L721,
                   actor=L1279)

L1285._add_result(result=L1287,
                   actor=L1279)

L1289._add_result(result=L508,
                   actor=L1279)

L1292._add_result(result=L493,
                   actor=L1279)

L1294._add_result(result=L405,
                   actor=L1279)

L1296._add_result(result=L477,
                   actor=L1279)

L1298._add_result(result=L988,
                   actor=L1279)

L1301._add_result(result=L511,
                   actor=L1279)

L1304._add_result(result=L472,
                   actor=L1279)

L1309._add_result(result=L405,
                   actor=L1279)

L591.define(var='box',
             value=L608)

L591.define(var='htmlmodule',
             value=L609)

L591.define(var='makemailbox',
             value=L684)

L591.define(var='mailbox',
             value=L698)

L591.define(var='maildirectory',
             value=L705)

L591.define(var='pair',
             value=L413)

L591.define(var='x',
             value=L707)

L591.define(var='Foo',
             value=L709)

L592.define(var='false',
             value=L593)

L592.define(var='makestamp',
             value=L599)

L592.define(var='true',
             value=L600)

L592.define(var='makebox',
             value=L606)

L592.define(var='listguard',
             value=L607)

L4.define(var='false',
           value=L5)

L4.define(var='makestamp',
           value=L11)

L4.define(var='true',
           value=L12)

L4.define(var='makebox',
           value=L18)

L4.define(var='listguard',
           value=builtin.TypeGuard(sample_instance=()))

L1098.define(var='makemailbox',
              value=actors.Actor(env=L1098,
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

L1098.define(var='maildirectory',
              value=builtin.MailDirectory(env=envs.Env(parent=L1099)))

L1099.define(var='false',
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

L1099.define(var='numberguard',
              value=builtin.TypeGuard(sample_instance=0))

L1099.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L1099.define(var='makestamp',
              value=builtin.StampMaker())

L1099.define(var='booleanguard',
              value=builtin.TypeGuard(sample_instance=True))

L1099.define(var='makebox',
              value=builtin.BoxMaker())

L1099.define(var='true',
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

L1099.define(var='stringguard',
              value=builtin.TypeGuard(sample_instance=''))

L1099.define(var='if',
              value=actors.Actor(env=L1099,
                                 script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                     inner_map={}),
                                                                              serial_id=0,
                                                                              parameters=['test',
                                                                                          'yes',
                                                                                          'no'],
                                                                              selector='true:then:else:')],
                                                      next_serial_id=1)))

L1183.define(var='mailbox',
              value=L1199)

L1183.define(var='sender',
              value=L1181)

L1183.define(var='inbox',
              value=L1218)

L1184.define(var='box',
              value=L726)

L1184.define(var='sender',
              value=L1181)

L1184.define(var='makemailbox',
              value=L1185)

L1184.define(var='mailbox',
              value=L1199)

L1184.define(var='makeballot',
              value=L1201)

L1184.define(var='maildirectory',
              value=L891)

L1184.define(var='message',
              value=L1209)

L1184.define(var='Foo',
              value=L1213)

L893.define(var='false',
             value=L727)

L893.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L893.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L893.define(var='makestamp',
             value=builtin.StampMaker())

L893.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L893.define(var='makebox',
             value=L308)

L893.define(var='true',
             value=L299)

L893.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L893.define(var='if',
             value=actors.Actor(env=L893,
                                script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0,
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             selector='true:then:else:')],
                                                     next_serial_id=1)))

L998.define(var='box',
             value=L999)

L998.define(var='makemailbox',
             value=L1000)

L998.define(var='Foo',
             value=L996)

L998.define(var='maildirectory',
             value=L2)

L998.define(var='mailbox',
             value=L1014)

L590.define(var='htmlguard',
             value=L615)

L590.define(var='markup',
             value=L645)

L590.define(var='html',
             value=L654)

L590.define(var='stamppair',
             value=L613)

L590.define(var='htmlstamp',
             value=L614)

L590.define(var='makeattr',
             value=L665)

L590.define(var='showattr',
             value=L588)

L239.define(var='inbox',
             value=L294)

L239.define(var='sender',
             value=L296)

L239.define(var='mailbox',
             value=L237)

L1276.define(var='node',
              value=L107)

L1276.define(var='guesser',
              value=L1277)

L790._add_result(result=L792,
                  actor=L739)

L793._add_result(result=L795,
                  actor=L739)

L797._add_result(result=L785,
                  actor=L739)

L800._add_result(result=L757,
                  actor=L739)

L802._add_result(result=L743,
                  actor=L739)

L804._add_result(result=L750,
                  actor=L739)

L806._add_result(result=L808,
                  actor=L739)

L811._add_result(result=L779,
                  actor=L739)

L814._add_result(result=L772,
                  actor=L739)

L818._add_result(result=L775,
                  actor=L739)

L820._add_result(result=L822,
                  actor=L739)

L839._add_result(result=L841,
                  actor=L739)

L842._add_result(result='Error: exceptions.ZeroDivisionError: float division',
                  actor=L739)

L844._add_result(result='Error: Unbound: makestamp',
                  actor=L739)

L1336.define(var='false',
              value=L1173)

L1336.define(var='numberguard',
              value=builtin.TypeGuard(sample_instance=0))

L1336.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L1336.define(var='makestamp',
              value=builtin.StampMaker())

L1336.define(var='booleanguard',
              value=builtin.TypeGuard(sample_instance=True))

L1336.define(var='makebox',
              value=L1042)

L1336.define(var='true',
              value=L1046)

L1336.define(var='stringguard',
              value=builtin.TypeGuard(sample_instance=''))

L1336.define(var='if',
              value=actors.Actor(env=L1336,
                                 script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                     inner_map={}),
                                                                              serial_id=0,
                                                                              parameters=['test',
                                                                                          'yes',
                                                                                          'no'],
                                                                              selector='true:then:else:')],
                                                      next_serial_id=1)))

L1550.define(var='query',
              value=builtin.String(str='Does it bark?'))

L1550.define(var='question',
              value=L1548)

L1550.define(var='animal',
              value=builtin.String(str='dog'))

L1274.define(var='terminus',
              value=L1272)

L1765._add_result(result=L573,
                   actor=L1761)

L1767._add_result(result=L1508,
                   actor=L1761)

L1770._add_result(result=L1213,
                   actor=L1761)

L1773._add_result(result=L726,
                   actor=L1761)

L1775._add_result(result=L299,
                   actor=L1761)

L1777._add_result(result=L727,
                   actor=L1761)

L1779._add_result(result=L1558,
                   actor=L1761)

L1782._add_result(result=L891,
                   actor=L1761)

L1785._add_result(result=L1199,
                   actor=L1761)

L1789._add_result(result='Error: No matching method: size',
                   actor=L1761)

L1791._add_result(result=L1024,
                   actor=L1761)

L1793._add_result(result=L1181,
                   actor=L1761)

L1795._add_result(result=L1383,
                   actor=L1761)

L1797._add_result(result=L1201,
                   actor=L1761)

L144.define(var='node',
             value=L103)

L144.define(var='guesser',
             value=L142)

L126.define(var='guessernode',
             value=L124)

L126.define(var='animal',
             value=L127)

L1660.define(var='makemailbox',
              value=actors.Actor(env=L1660,
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

L1660.define(var='maildirectory',
              value=builtin.MailDirectory(env=envs.Env(parent=L1661)))

L1661.define(var='false',
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

L1661.define(var='numberguard',
              value=builtin.TypeGuard(sample_instance=0))

L1661.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L1661.define(var='makestamp',
              value=builtin.StampMaker())

L1661.define(var='booleanguard',
              value=builtin.TypeGuard(sample_instance=True))

L1661.define(var='makebox',
              value=builtin.BoxMaker())

L1661.define(var='true',
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

L1661.define(var='stringguard',
              value=builtin.TypeGuard(sample_instance=''))

L1661.define(var='if',
              value=actors.Actor(env=L1661,
                                 script=actors.Script(elements=[actors.Method(body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                     inner_map={}),
                                                                              serial_id=0,
                                                                              parameters=['test',
                                                                                          'yes',
                                                                                          'no'],
                                                                              selector='true:then:else:')],
                                                      next_serial_id=1)))

L474.define(var='inbox',
             value=L515)

L474.define(var='sender',
             value=L513)

L474.define(var='mailbox',
             value=L472)

L551.define(var='sender',
             value=L552)

L551.define(var='inbox',
             value=L557)

L551.define(var='mailbox',
             value=L549)

L1335.define(var='box',
              value=L1346)

L1335.define(var='makemailbox',
              value=L1347)

L1335.define(var='Foo',
              value=L1333)

L1335.define(var='mailbox',
              value=L1361)

L1335.define(var='maildirectory',
              value=L1368)

L1758.define(var='node',
              value=L123)

L1758.define(var='guesser',
              value=L1756)

L906.define(var='mailbox',
             value=L904)

L906.define(var='inbox',
             value=L947)

L906.define(var='sender',
             value=L949)

L177.define(var='box',
             value=L170)

L177.define(var='guess',
             value=L175)

L177.define(var='animal',
             value=L179)

L149.define(var='node',
             value=L103)

L149.define(var='asker',
             value=L147)

L1416._add_result(result=L1418,
                   actor=L1412)

L1419._add_result(result=L1044,
                   actor=L1412)

L1422._add_result(result=L709,
                   actor=L1412)

L1425._add_result(result=L608,
                   actor=L1412)

L1427._add_result(result=L600,
                   actor=L1412)

L1429._add_result(result=L593,
                   actor=L1412)

L1431._add_result(result=L1433,
                   actor=L1412)

L1436._add_result(result=L705,
                   actor=L1412)

L1439._add_result(result=L698,
                   actor=L1412)

L1443._add_result(result=L609,
                   actor=L1412)

L611._add_result(result=L613,
                  actor=L616)

L617._add_result(result=L614,
                  actor=L616)

L619._add_result(result=L615,
                  actor=L616)

L621._add_result(result=L645,
                  actor=L616)

L647._add_result(result=L654,
                  actor=L616)

L656._add_result(result=L665,
                  actor=L616)

L667._add_result(result=L588,
                  actor=L616)

L673._add_result(result=L675,
                  actor=L616)

L676._add_result(result=L678,
                  actor=L616)

L679._add_result(result=L681,
                  actor=L616)

L682._add_result(result='Error: No matching method: show',
                  actor=L616)

L1224._add_result(result=L1226,
                   actor=L1220)

L1227._add_result(result=L1229,
                   actor=L1220)

L1231._add_result(result=L291,
                   actor=L1220)

L1234._add_result(result=L264,
                   actor=L1220)

L1236._add_result(result=L253,
                   actor=L1220)

L1238._add_result(result=L242,
                   actor=L1220)

L1240._add_result(result=L723,
                   actor=L1220)

L1243._add_result(result=L289,
                   actor=L1220)

L1246._add_result(result=L279,
                   actor=L1220)

L1250._add_result(result=L1252,
                   actor=L1220)

L1629._add_result(result=L1631,
                   actor=L1625)

L1632._add_result(result=L1562,
                   actor=L1625)

L1635._add_result(result=L1333,
                   actor=L1625)

L1638._add_result(result=L1346,
                   actor=L1625)

L1640._add_result(result=L1046,
                   actor=L1625)

L1642._add_result(result=L1173,
                   actor=L1625)

L1644._add_result(result=L1646,
                   actor=L1625)

L1649._add_result(result=L1368,
                   actor=L1625)

L1652._add_result(result=L1361,
                   actor=L1625)

L1656._add_result(result=L1625,
                   actor=L1625)

L700.define(var='mailbox',
             value=L698)

L700.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L700),
                                script=L688))

L700.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=())))

L437.define(var='mailbox',
             value=L435)

L437.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=(L440,))))

L437.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L437),
                                script=L448))

L512.define(var='alice',
             value=L513)

L215.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L215),
                                script=L156))

L215.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=())))

L215.define(var='mailbox',
             value=L213)

L173.define(var='query',
             value=L174)

L173.define(var='onyes',
             value=L175)

L173.define(var='onno',
             value=L21)

L173.define(var='yesnoquestion',
             value=L171)

L1363.define(var='mailbox',
              value=L1361)

L1363.define(var='sender',
              value=actors.Actor(env=envs.Env(parent=L1363),
                                 script=L1351))

L1363.define(var='inbox',
              value=builtin.Box(initial_value=builtin.List(elements=())))

L1449.define(var='false',
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

L1449.define(var='makestamp',
              value=builtin.StampMaker())

L1449.define(var='true',
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

L1449.define(var='makebox',
              value=builtin.BoxMaker())

L1449.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L1476._add_result(result=L1387,
                   actor=L1472)

L1478._add_result(result=L1480,
                   actor=L1472)

L1482._add_result(result=L544,
                   actor=L1472)

L1485._add_result(result=L543,
                   actor=L1472)

L1487._add_result(result=L532,
                   actor=L1472)

L1489._add_result(result=L521,
                   actor=L1472)

L1491._add_result(result=L1325,
                   actor=L1472)

L1494._add_result(result=L547,
                   actor=L1472)

L1497._add_result(result=L549,
                   actor=L1472)

L1501._add_result(result=L1029,
                   actor=L1472)

L970.define(var='true',
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

L970.define(var='makebox',
             value=builtin.BoxMaker())

L970.define(var='false',
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

L970.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L1376.define(var='question',
              value=L1374)

L942._add_result(result=L229,
                  actor=L944)

L954.define(var='terminus',
             value=L952)

L364._add_result(result=L366,
                  actor=L309)

L367._add_result(result=L369,
                  actor=L309)

L371._add_result(result=L350,
                  actor=L309)

L374._add_result(result=L335,
                  actor=L309)

L376._add_result(result=L324,
                  actor=L309)

L378._add_result(result=L313,
                  actor=L309)

L380._add_result(result=L382,
                  actor=L309)

L385._add_result(result=L353,
                  actor=L309)

L388._add_result(result=L355,
                  actor=L309)

L392._add_result(result=L366,
                  actor=L309)

L394._add_result(result=L396,
                  actor=L309)

L958.define(var='node',
             value=L107)

L958.define(var='asker',
             value=L956)

L1016.define(var='inbox',
              value=builtin.Box(initial_value=builtin.List(elements=())))

L1016.define(var='sender',
              value=actors.Actor(env=envs.Env(parent=L1016),
                                 script=L1004))

L1016.define(var='mailbox',
              value=L1014)

L1065._add_result(result=L1067,
                   actor=L1061)

L1068._add_result(result=L1070,
                   actor=L1061)

L1072._add_result(result=L996,
                   actor=L1061)

L1075._add_result(result=L999,
                   actor=L1061)

L1077._add_result(result=L12,
                   actor=L1061)

L1079._add_result(result=L5,
                   actor=L1061)

L1081._add_result(result=L1083,
                   actor=L1061)

L1086._add_result(result=L2,
                   actor=L1061)

L1089._add_result(result=L1014,
                   actor=L1061)

L1093._add_result(result='Error: exceptions.TypeError: unbound method __init__() must be called with Actor instance as first argument (got Stamp instance instead)',
                   actor=L1061)

L1516._add_result(result=L1518,
                   actor=L1512)

L1519._add_result(result=L1521,
                   actor=L1512)

L1523._add_result(result=L939,
                   actor=L1512)

L1526._add_result(result=L580,
                   actor=L1512)

L1528._add_result(result=L914,
                   actor=L1512)

L1530._add_result(result=L581,
                   actor=L1512)

L1532._add_result(result=L570,
                   actor=L1512)

L1535._add_result(result=L945,
                   actor=L1512)

L1538._add_result(result=L904,
                   actor=L1512)

L114.define(var='guessernode',
             value=L112)

L114.define(var='animal',
             value=builtin.String(str='fraidycat'))

L0
root = L0
