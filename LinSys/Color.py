# returns the hex value according to a "progress" percentage
# pattern goes as follows:
#    black, blue, cyan, green, yellow, red, magenta, white
def getValueByPercent(p_overall):

	# x0 - xFF
	# black - blue
	if p_overall < (1/7):
		p_partial = getPartialProgress(p_overall, 0);
		val = getStageValue(p_partial)
		return hexColorOf(val)

	# xFF - xFFFF
	# blue - cyan
	if p_overall < (2/7):
		p_partial = getPartialProgress(p_overall, 1)
		val = getStageValue(p_partial)
		val = shiftLeft(val)
		return hexColorOf(val + 255)

	# xFFFF - xFF00
	# cyan - green
	if p_overall < (3/7):
		p_partial = getPartialProgress(p_overall, 2)
		val = getStageValue(p_partial)
		return hexColorOf(65535 - val)

	# xFF00 - xFFFF00
	# green - yellow
	if p_overall < (4/7):
		p_partial = getPartialProgress(p_overall, 3)
		val = getStageValue(p_partial)
		val = shiftLeft(shiftLeft(val))
		return hexColorOf(val + 65280)

	# xFFFF00 - xFF0000
	# yellow - red
	if p_overall < (5/7):
		p_partial = getPartialProgress(p_overall, 4)
		val = getStageValue(p_partial)
		val = shiftLeft(val)
		return hexColorOf(16776960 - val)

	# xFF0000 - xFF00FF
	# red - magenta
	if p_overall < (6/7):
		p_partial = getPartialProgress(p_overall, 5)
		val = getStageValue(p_partial)
		return hexColorOf(16711680 + val)

	# xFF00FF - xFFFFFF
	# magenta - white
	p_partial = getPartialProgress(p_overall, 6)
	val = getStageValue(p_partial)
	val = shiftLeft(val)
	val += 255
	return hexColorOf(16711680 + val)

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