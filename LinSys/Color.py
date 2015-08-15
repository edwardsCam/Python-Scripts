

def get(s):
	try:
		int(s, 16)
		while len(s) < 6:
			s = "0" + s
		return "#" + s
	except ValueError as e:
		return s.replace('_', ' ')

def getByPercent(p):
	return get(hex(int(16777215 * p)).split('x')[1])

def white():
	return "#000000"

def default():
	return "#F0F0F0"