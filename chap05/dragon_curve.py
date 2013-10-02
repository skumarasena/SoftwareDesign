from swampy.TurtleWorld import *

length = 5
def dragon_curve(t, n):
    """Creates a dragon curve using two mutually recursive functions.

    t: Turtle object

    n: integer, order or "level" of curve

    """
    def x_func(t, n):
        if n == 0:
            return
        else:
            x_func(t, n-1)
            rt(t, 90)
            y_func(t, n-1)
            fd(t, length)

    def y_func(t, n):
        if n == 0:
            return
        else:
            fd(t, length)
            x_func(t, n-1)
            lt(t, 90)
            y_func(t, n-1)
    
    fd(t, length)
    x_func(t, n)



world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
dragon_curve(bob, 10)
