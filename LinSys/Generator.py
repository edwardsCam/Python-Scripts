import Rule
from re import finditer

def replace(s):
	prod = Rule.getProductions()
	idx = 0
	a = list(s)
	for c in a:
		for p in prod:
			if c == p[0]:
				a[idx] = p[1]
				break
		idx += 1
	return "".join(a)

def convert(s, n):
	if (n == 0):
		return s
	s = replace(s)
	return convert(s, n-1)
