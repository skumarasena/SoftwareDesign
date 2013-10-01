from swampy.TurtleWorld import *

#given turtle and length of koch curve, draws koch curve
def koch(t, length):
	"""Draws koch curve using TurtleWorld.

		t: Turtle object

		length: integer length of koch curve
	"""
    if length < 3:
        fd(t, length)
    else:
        koch(t, length/3)
        lt(t, 60)
        koch(t, length/3)
        rt(t, 120)
        koch(t, length/3)
        lt(t, 60)
        koch(t, length/3)
    
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1
koch(bob, 60)
