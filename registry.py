import random
import time


# XXX should be server instance variables
at_id = {}
id_of_actor = {}

swiss_range = 2L**80

def get_uri(actor):
    return '/id/%s' % get_id(actor)    

def id_is_defined(hid):
    print 'checking', hid
    return hid in at_id

def get_id(actor):
    # XXX should respect sameness of selfless objects
    if actor not in id_of_actor:
        while True:
            new_id = random.randint(0, swiss_range)
            hid = hex(new_id)[2:-1].lower()
            if hid not in at_id: 
                break
        print 'adding', hid
        at_id[hid] = Entry(actor)
        id_of_actor[actor] = hid
    return id_of_actor[actor]

def get_actor(hid):
    if hid not in at_id:
        raise 'No such actor', hid
    return at_id[hid].actor

def access_id(hid):
    at_id[hid].access()

class Entry:

    def __init__(self, actor, timestamp=None):
        if timestamp is None:
            timestamp = time.time()
        self.actor = actor
        self.timestamp = timestamp
    
    def uneval(self, context, label):
        return context.uncall('registry.Entry', 
                              actor=self.actor,
                              timestamp=self.timestamp)

    def access(self):
        self.timestamp = time.time()


editor_of_actor = {}

def get_editor(actor):
    from actors import ActorEditor # XXX circular module dependency
    if actor.__class__ == ActorEditor:
        return actor
    if actor not in editor_of_actor:
        editor_of_actor[actor] = ActorEditor(actor, actor.may_edit())
    return editor_of_actor[actor]
    

accounts = []

def add_account(hid):
    accounts.append(hid)


class HmphSystem:

    def __init__(self, at_id, editor_of_actor, accounts):
        self.at_id = at_id
        self.editor_of_actor = editor_of_actor
        self.accounts = accounts

    def uneval(self, context, label):
        return context.uncall('registry.HmphSystem',
                              at_id=self.at_id, 
                              editor_of_actor=self.editor_of_actor,
                              accounts=self.accounts)
        

def get_system():
    return HmphSystem(at_id, editor_of_actor, accounts)

def load_system():
    import snapshot
    try: 
        hmph = snapshot.root
    except AttributeError:
        return                  # XXX should reset the system here
    global at_id, id_of_actor, editor_of_actor, accounts
    at_id = hmph.at_id
    id_of_actor = invert_at_id(at_id)
    editor_of_actor = hmph.editor_of_actor
    accounts = hmph.accounts

def invert_at_id(table):
    result = {}
    for key in table:
        result[table[key].actor] = key
    return result
