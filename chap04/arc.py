from swampy.TurtleWorld import *
from math import pi

#Samantha Kumarasena
#Software Design
#9/22/13

#Creates a arc of radius r using turtles (Swampy)
#t = turtle object
#r = radius of arc
#angle = angle of arc

def arc(t, r, angle):
    #makes sure angle is a float
    angle = float(angle)
    
    circumference = 2*pi*r                  #circumference of circle
    segment = circumference*(angle/360)     #length of segment
    n = int(segment/3) + 1                  #n depends on segment length -- from ch. 4.3

    #angle and length required for arc
    ang = angle/n
    length = segment/n

    for i in range(n):
        fd(t, length)
        lt(t, ang)


#creates world, turtle object
world = TurtleWorld()
bob = Turtle()

#decreases turtle delay in movement -- otherwise this would take a while!
bob.delay = 0.01

#function call
arc(bob, 50, 110)
