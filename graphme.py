#!/usr/bin/python2

import operator
def graphme(numgroups, losestates, groupweights):
	print("%s, %s, %s" % (numgroups, losestates, groupweights))
def invertgroup(group):
	return map(operator.not_, group)

graphme(4, [
	[True, True, False, False],
	[False, True, True, False],
	[True, True, True, False]], [1,1,1,1])
graphme(6, [
	[True, True, True, False, False, False],
	[True, True, True, True,  False, False],
	[True, True, True, True,  True,  False],
	[True, True, True, False, True,  False],
	[True, True, True, False, False, True],
	[True, True, True, False, True,  True],
	[True, True, False, True, False, False],
	[True, True, False, False, True, False],
	[True, True, False, False, False, True],
	[True, False, True, True, False, False],
	[True, False, True, False, True, False],
	[True, False, True, False, False, True],
	[False, True, True, True, False, False],
	[False, True, True, False, True, False],
	[False, True, True, False, False, True]], [1,1,1,1,1,1])
graphme(4, [], [1,2,5,8])