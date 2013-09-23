from swampy.TurtleWorld import *

def square(t, length):    
    for i in range(4):
        fd(t, length)
        lt(t)


world = TurtleWorld()
bob = Turtle()
square(bob, 150)
