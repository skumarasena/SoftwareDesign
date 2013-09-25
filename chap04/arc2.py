
from swampy.TurtleWorld import *
from math import pi


#Samantha Kumarasena
#Software Design
#9/22/13

#Creates a circle of radius r using polygon (defined below) and turtles (Swampy)
#by ensuring that length * number of sides = circumference of circle
#Now with refactoring!
#t = turtle object
#r = radius of circle
def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    angle = float(angle)
    circumference = 2*pi*r
    segment = circumference*(angle/360)
    
    n = int(segment/3)+1
    
    ang = angle/n
    length = segment/n
    
    polyline(t, n, length, ang)

world = TurtleWorld()
bob = Turtle()

bob.delay = 0.01

arc(bob, 50, 110)
