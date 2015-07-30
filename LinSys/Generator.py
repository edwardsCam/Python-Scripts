import Rule
import re
import collections

def getReplacements(s):
	prod = Rule.getProductions()
	ret = {}
	for p in prod:
		sym = p[0]
		rep = p[1]
		hits = [m.start() for m in re.finditer(sym, s)]
		for i in hits:
			intersect = False
			hitrange = (i, i+len(sym)-1)
			for k in ret:
				iset = set(range(hitrange[0], hitrange[1]+1))
				kset = set(range(k[0], k[1]+1))
				if iset & kset:
					intersect = True
					break
			if not intersect:
				ret[hitrange] = rep
	return ret

def ordered(r):
	return collections.OrderedDict(sorted(r.items(), reverse=True))

def replace(s, r):
	for symb in r:
		repl = r[symb]
		rlen = len(repl)
		i = symb[0]
		j = symb[1]
		diff = j-i
		s = s[:i] + repl + s[j+1:]
	return s

def convert(s, n):
	if (n == 0):
		return s
	else:
		s = replace(s, ordered(getReplacements(s)))
		return convert(s, n-1)
