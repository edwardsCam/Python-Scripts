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

def replaceMulti(s, r):
	for symb in r:
		repl = r[symb]
		rlen = len(repl)
		i = symb[0]
		j = symb[1]
		diff = j-i
		s = s[:i] + repl + s[j+1:]
	return s

def replaceSingle(s):
	prod = Rule.getProductions()
	idx = 0
	a = list(s)
	for c in a:
		for p in prod:
			if c == p[0]:
				a[idx] = p[1]
		idx += 1
	return "".join(a)

def convert(s, n, multi=False):
	if (n == 0):
		return s
	if multi:
		r = ordered(getReplacements(s))
		s = replaceMulti(s, r)
	else:
		s = replaceSingle(s)
	return convert(s, n-1, multi)
