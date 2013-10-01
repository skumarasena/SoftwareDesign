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


def gen_snowflake(t, length, n):
	"""Draws a snowflake with n koch curves using Turtleworld.
	
		t: Turtle object
	
		length: integer length of single koch curve
	
		n: integer number of koch curves
	"""
    angle = (180 * (n-2))/float(n)
    for i in range(n):
        koch(t, length/3)
        rt(t, 180 - int(angle))
    wait_for_user()


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.005
gen_snowflake(bob, 200, 4)






