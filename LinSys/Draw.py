from math import cos, sin, radians

def set(p, l=1.0, a=0.0):
	global curr
	global line
	global angle
	curr = p
	line = l
	angle = a

def length(l):
	global line
	line = float(l)

def turn(a):
	global angle
	angle = (angle + float(a)) % 360

def move(n):
	n = float(n)
	global curr
	global line
	global angle
	old = curr
	dx = cos(radians(angle)) * line * n
	dy = sin(radians(angle)) * line * n
	curr = (old[0]+dx, old[1]+dy)
	return (old, curr)
