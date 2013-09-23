from swampy.TurtleWorld import *

#Samantha Kumarasena
#Software Design
#9/22/13

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

#function call
polygon(bob, 50, 10)
