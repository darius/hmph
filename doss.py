# XXX at some point, get this to detect cycles and complain that you
# need to break them with side-effect calls.

# Also it's kind of ugly to have to pass label to uneval.

def serialize(object, file):
    depiction = Context().depict(object)
    depiction.refcount += 1     # ensure it goes in the defs table
    defs = Defs()
    walked = defs.walk_until_quiescent(depiction)
    out = Output(file)
    print_imports(out)
    out.pprint(defs)
    defs.pp_effects(out)
    out.pprint(walked)
    out.emit('root = ')
    depiction.pp(out)
    out.newline()

def print_imports(out):         # XXX should compute them automatically
    out.emit('import actors\n')
    out.emit('import builtin\n')
    out.emit('import envs\n')
    out.emit('import registry\n')
    out.newline()


class Context:                # XXX what's a better name than context?

    def __init__(self):
        self.to_label = {}
        self.next_label = 0

    def depict(self, object):
        if is_simple_data(object):
            return object
        if type(object) == type(()):
            return tuple([self.depict(elt) for elt in object])
        # N.B. we don't preserve identity of lists and dicts
        # (XXX make sure this is ok)
        # (maybe better for uneval to simply avoid lists and dicts)
        if type(object) == type([]):
            return [self.depict(elt) for elt in object]
        if type(object) == type({}):
            result = {}
            for key in object:
                result[self.depict(key)] = self.depict(object[key])
            return result
        if object in self.to_label:
            label = self.to_label[object]
            label.refcount += 1
            return label
        label = self._next_label()
        self.to_label[object] = label
        label.referent = object.uneval(self, label)
        return label

    def _next_label(self):
        result = Label(self.next_label)
        self.next_label += 1
        return result

    def uncall(self, function_name, **arguments):
        return Uncall(function_name, **self.depict(arguments))

    def unsequence(self, uncall, label, method_uncalls):
        return Unsequence(uncall, label, method_uncalls)


simple_data_types = map(type, [0, 0.0, 0L, '', True, None])

def is_simple_data(object):
    return type(object) in simple_data_types

class Defs:

    def __init__(self):
        self.defined = {}
        self.vars = []
        self.vals = []
        self.effects = []

    def ensure_defined(self, label):
        if label not in self.defined:
            self.defined[label] = True
            value = self.walk(label.referent)
            self.vars.append(label)
            self.vals.append(value)

    def register_effects(self, effects):
        self.effects.append(effects)

    def walk_until_quiescent(self, depiction):
        result = self.walk(depiction)
        i = 0
        while i < len(self.effects):
            self.effects[i].walk_effects(self)
            i += 1
        return result

    # Return depiction topologically sorted, with linear refs inlined
    def walk(self, depiction):
        if is_simple_data(depiction):
            return depiction
        if type(depiction) == type(()):
            return tuple(map(self.walk, depiction))
        if type(depiction) == type([]):
            return map(self.walk, depiction)
        if type(depiction) == type({}):
            result = {}
            for key in depiction:
                result[self.walk(key)] = self.walk(depiction[key])
            return result
        # XXX depiction.walk should have a different name
        return depiction.walk(self)

    def pp(self, out):
        for label, defn in zip(self.vars, self.vals):
            out.pp(label)
            out.emit(' = ')
            out.pprint(defn)

    def pp_effects(self, out):
        for effects in self.effects:
            effects.pp_effects(out)


class Label:

    def __init__(self, n):
        self.n = n
        self.refcount = 1

    def walk(self, defs):
        if 1 == self.refcount:
            return defs.walk(self.referent)
        defs.ensure_defined(self)
        return self

    def pp(self, out):
        out.emit('L%s' % self.n)

class Uncall:

    def __init__(self, constructor, **args):
        self.constructor = constructor
        self.arguments = args
        
    def walk(self, defs):
        return Uncall(defs.walk(self.constructor), 
                      **defs.walk(self.arguments))

    def pp(self, out):
        out.emit(self.constructor)
        out.pp_dict(self.arguments, out.emit, '(', ')', '=')

class Unsequence:

    def __init__(self, uncall, label, method_uncalls):
        self.uncall = uncall
        self.label = label
        self.method_uncalls = method_uncalls
        label.refcount += len(method_uncalls)

    def walk(self, defs):
        defs.register_effects(self)
        return defs.walk(self.uncall)

    def walk_effects(self, defs):
        for i in range(len(self.method_uncalls)):
            self.method_uncalls[i] = defs.walk(self.method_uncalls[i])

    def pp(self, out):
        self.uncall.pp(out)

    def pp_effects(self, out):
        for method_uncall in self.method_uncalls:
            self.label.pp(out)
            out.emit('.')
            out.pprint(method_uncall)
            out.emit('\n')


class Output:
    
    def __init__(self, stream):
        self.stream = stream
        self.column = 0
        self.margin = 0

    def pprint(self, object):
        self.pp(object)
        self.newline()

    def pp(self, object):
        if is_simple_data(object):
            self.emit(repr(object))
        elif type(object) == type(()):
            self.pp_list(object, '(', ')', tween=True)
        elif type(object) == type([]):
            self.pp_list(object, '[', ']')
        elif type(object) == type({}):
            self.pp_dict(object, self.pp, '{', '}', ': ')
        else:
            object.pp(self)

    def pp_list(self, elements, open, close, tween=False):
        self.pp_collection(elements, self.pp, open, close, tween)

    def pp_dict(self, dict, pp_key, open, close, bind, tween=False):
        def pp_pair(key):
            pp_key(key)
            self.emit(bind)
            self.pp(dict[key])
        self.pp_collection(dict, pp_pair, open, close, tween)

    def pp_collection(self, collection, pp_element, open, close, tween=False):
        self.emit(open)
        old_margin = self.margin
        self.margin = self.column
        i = 0
        for key in collection:
            self.tab()
            pp_element(key)
            i += 1
            if i < len(collection):
                self.emit(',')
                self.newline()
        self.margin = old_margin
        if tween and len(collection) == 1: # tuples need a trailing ","
            self.emit(',')
        self.emit(close)

    def newline(self):
        self.stream.write('\n')
        self.column = 0

    def emit(self, string):
        self.stream.write(string)
        self.column += len(string)

    def tab(self):
        while self.column < self.margin:
            self.emit(' ')
