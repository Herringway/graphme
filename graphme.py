#!/usr/bin/python2

import operator
def graphme(numgroups, losestates, groupweights, verify = lambda v,w,x,y,z: True, maxval = 40, victoryverify = lambda a: len(a) == len(list(filter(None, a))), numbermoving = 2):
	"""Programmer-friendly interface to the graph searching algorithm"""
	assert numgroups == len(groupweights)
	return graphmeup([False]*numgroups, losestates, groupweights, verify, maxval, victoryverify, numbermoving)

def graphmeup(state, losestates, groupweights, verify, maxval, victoryverify, numbermoving):
	"""Searches for and returns a solution required to move all items across the river."""
	backtracks = 0
	searchedstates = 0
	pathqueue = []
	pathqueue.append((0, [state]))
	while pathqueue:
		(totalweight, path) = pathqueue.pop(0)
		node = path[-1] #the current state will be at the tail
		if victoryverify(node) and totalweight <= maxval:
			return (totalweight, path, backtracks, searchedstates)
		for (permutation, weight) in permute(verify, list(node), groupweights, numbermoving):
			if (permutation in path or
			 totalweight > maxval or
			 permutation in losestates or
			 invertgroup(list(permutation)) in losestates):
				backtracks = backtracks + 1
				continue
			newpath = list(path)
			newpath.append(list(permutation))
			pathqueue.append((totalweight+weight, newpath))
			searchedstates = searchedstates + 1

def invertgroup(group):
	"""Flip all the values in the specified group and return it"""
	return map(operator.not_, group)
def permute(verify, state, weights, changes = 2):
	"""Generates possible next states for river crossing problems"""
	for i in range(len(state)):
		statecopy = list(state)
		statecopy[i] = not(state[i])
		for j in range(i+1, len(state)):
			statecopy[j] = not(state[j])
			if changes == 3:
				for k in range(j+1, len(state)):
					statecopy[k] = not(state[k])
					if verify(state, statecopy, i, j, k):
						yield (statecopy, max(weights[i], weights[j]))
					statecopy[k] = state[k]
			if verify(state, statecopy, i, j, i):
				yield (statecopy, max(weights[i], weights[j]))
			statecopy[j] = state[j]
		if verify(state, statecopy, i, i, i):
			yield (statecopy, weights[i])
		statecopy[i] = state[i]

def prettyprint(solution):
	if solution == None:
		print("No solution found\n--------------------------------")
		return
	(weight, path, backtracks, searchedstates) = solution
	print("Path taken: %s\nCost: %s\nPath length: %s\nBacktrack count: %s\nStates searched: %s\n--------------------------------" % (path, weight, len(path), backtracks, searchedstates))
def main():
	prettyprint(graphme(4, [
		[True, True, False, False],
		[False, True, True, False],
		[True, True, True, False]], [1,1,1,1], verify = lambda x, y, w, z, v: (x[-1] != y[-1]) and (y[w] == y[z] == y[-1]), victoryverify = lambda x: x[0] and x[1] and x[2]))
	prettyprint(graphme(6, [
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
		[False, True, True, False, False, True]], [1,1,1,1,1,1]))
	prettyprint(graphme(5, [], [1,2,5,8,1], maxval = 15, verify = lambda x, y, w, z, v: (x[-1] != y[-1]) and (y[v] == y[w] == y[z] == y[-1]) and ((w != z) or (w != v) or (z != v)), numbermoving=3))

if __name__ == "__main__":
    main()