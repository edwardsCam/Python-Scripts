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
	angle = (angle + a) % 360

def step(n):
	global curr
	global line
	global angle
	dx = cos(radians(angle)) * line * n
	dy = sin(radians(angle)) * line * n
	return (curr[0]+dx, curr[1]+dy)

def move(n):
	global curr
	old = curr
	curr = step(n)
	return (old, curr)

def skip(n):
	global curr
	curr = step(n)

def back(n):
	global curr
	curr = step(n * -1)
