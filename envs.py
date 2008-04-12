class Env:

    # XXX it's bad form to pass in the locals as a parameter because
    # the caller might hold on to that mutable dict.
    def __init__(self, parent, locals=None):
	if locals is None:
	    locals = {}
	self.parent = parent
	self.locals = locals

    def uneval(self, context, label):
	buildme = context.uncall('envs.Env', parent=self.parent)
	defns = [context.uncall('define', 
				var=key, 
				value=self.locals[key])
		 for key in self.locals]
	return context.unsequence(buildme, label, defns)
    
    def get(self, var):
	if var in self.locals:
	    return self.locals[var]
	if self.parent is None:
	    return None
	return self.parent.get(var)

    def must_get(self, var):
	value = self.get(var)
	if value is None:
	    raise 'Unbound', var
	return value

    # XXX mutable environments are more of a problem than a help,
    # as we scale up.  Will have to refactor this out eventually.
    def define(self, var, value):
	self.locals[var] = value

    def sprout(self):
	return Env(self, {})


# XXX yucko
global_env = Env(None)
