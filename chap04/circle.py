
from swampy.TurtleWorld import *
from math import pi


#Samantha Kumarasena
#Software Design
#9/22/13

#Creates a circle of radius r using polygon (defined below) and turtles (Swampy)
#by ensuring that length * number of sides = circumference of circle
#t = turtle object
#r = radius of circle

def circle(t, r):
 
    circumference = 2*pi*r             #calculate circumference
    n = int(circumference/3) + 1       #n depends on circumference; see chapter 4.3
    
    #calculate length that will result in a circle of radius r
    length = circumference/n

    polygon(t, length, n)

#Creates a new polygon draws an n-sided polygon using turtles (Swampy)
#t = turtle object
#length = side length of polygon drawn by turtle
#n = number of sides in polygon

def polygon(t, length, n):
    #calculating angle for polygon with number of sides n
    ang = 360.0/n            #floating point division
    
    #draw each side with length 'length' and angle 'ang'
    for i in range(n):
        fd(t, length)
        lt(t, ang)


#creates world, turtle object
world = TurtleWorld()
bob = Turtle()

#decreases turtle delay in movement -- otherwise this would take a while!
bob.delay = 0.01

#function call
circle(bob, 50)
