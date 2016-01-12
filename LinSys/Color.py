# returns the hex value according to a "progress" percentage
# pattern goes as follows:
#    black, red, yellow, green, cyan, blue, magenta, white
def getValueByPercent(p_overall):

	xff = shiftLeft(1)-1
	xff00 = shiftLeft(xff)
	xff0000 = shiftLeft(xff00)

	val = 0
	base = 0

	# x000000 -> xFF0000
	# black -> red
	if p_overall < (1/7):
		p_partial = getPartialProgress(p_overall, 0);
		val = getStageValue(p_partial)
		val = shiftLeft(val)
		val = shiftLeft(val)

	# xFF0000 -> xFFFF00
	# red -> yellow
	elif p_overall < (2/7):
		base = xff0000
		p_partial = getPartialProgress(p_overall, 1)
		val = getStageValue(p_partial)
		val = shiftLeft(val)

	# xFFFF00 -> x00FF00
	# yellow -> green
	elif p_overall < (3/7):
		base = xff00
		p_partial = getPartialProgress(p_overall, 2)
		val = getStageValue(1-p_partial)
		val = shiftLeft(val)
		val = shiftLeft(val)

	# x00FF00 -> x00FFFF
	# green -> cyan
	elif p_overall < (4/7):
		base = xff00
		p_partial = getPartialProgress(p_overall, 3)
		val = getStageValue(p_partial)

	# x00FFFF -> x0000FF
	# cyan -> blue
	elif p_overall < (5/7):
		base = xff
		p_partial = getPartialProgress(p_overall, 4)
		val = getStageValue(1-p_partial)
		val = shiftLeft(val)

	# x0000FF -> xFF00FF
	# blue -> magenta
	elif p_overall < (6/7):
		base = xff
		p_partial = getPartialProgress(p_overall, 5)
		val = getStageValue(p_partial)
		val = shiftLeft(val)
		val = shiftLeft(val)

	# xFF00FF -> xFFFFFF
	# magenta -> white
	else:
		base = xff0000 + xff
		p_partial = getPartialProgress(p_overall, 6)
		val = getStageValue(p_partial)
		val = shiftLeft(val)

	return hexColorOf(base + val)


# returns a hex representation of x
# output is a string in the format /#\d{6}/
def getHexString(x):
	try:
		int(x, 16)
		while len(x) < 6:
			x = "0" + x
		return "#" + x
	except ValueError as e:
		return x.replace('_', ' ')

def hexColorOf(x):
	x = int(x)
	x = hex(x)
	return getHexString(x.split('x')[1])

# scale from 0-255 given a percentage
def getStageValue(perc):
	return int(255*perc)

# given an overall progress percentage and a stage, determine the relative progress through that stage
def getPartialProgress(perc, stage):
	return 7*perc - stage

# shifts a hex number two left
# i.e. xFF -> xFF00
def shiftLeft(x):
	return x*256

def white():
	return "#000000"

def default():
	return "#F0F0F0"