from swampy.TurtleWorld import *

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
    

def snowflake(t, length):
	"""Draws snowflake out of koch curves using Turtleworld.
	
		t: Turtle object
	
		length: integer length of single koch curve
	"""
    for i in range(3):
        koch(t, length)
        rt(t, 120)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
snowflake(bob, 60)
