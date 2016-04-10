def mods(module):
	""" Extension of vars(). Lists attributes, values and functions separately. 
	To be improved to include exceptions, builtins etc"""

	v=vars(module)
	details = {
		'attributes':{},
		'functions':{},
		'exceptions':{},
		'builtins': {},
		'misc':{},
		'attributes':{},
	}
	for k,v in v.iteritems():
		if hasattr(v, '__call__'):
			details["functions"][k] = v
		elif type(v) is type:
			details["exceptions"][k] = v
		elif k == "__builtins__":
			details["builtins"] = v
		elif k.startswith("_"):
			details["misc"][k] = v
		elif type(v) is str:
			details["attributes"][k] = v


	print "\n-----Attributes------"
	for k, v in details["attributes"].iteritems():
		print k, '--', v

	print "\n-----Functions------"
	for k, v in details["functions"].iteritems():
		print k + "()"

