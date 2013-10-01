from swampy.TurtleWorld import *

length = 50
def curve(t, n):
    if n == 0:
        fd(t, length)
    else:
        rt(t, 90)
        curve(t, n-1)
        lt(t, 90)
        curve(t, n-1)
        lt(t, 90)
        curve(t, n-1)
        rt(t, 90)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1
curve(bob, 3)
