"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""
import copy
import math
from swampy.Lumpy import Lumpy

class Point(object):
    """Represents a point in 2-D space."""


def print_point(p):
    """Print a Point object in human-readable format."""
    print '(%g, %g)' % (p.x, p.y)

def distance_between_points(p1, p2):
    #dist = math.sqrt(math.pow(p1.x-p2.x,2) + math.pow(p1.y-p2.y,2))
    dist = math.hypot(p1.x-p2.x, p1.y-p2.y)
    return dist

class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle."""
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dx, dy):
    """Modify the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dx
    rect.height += dy

def move_rectangle1(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

def move_rectangle2(rect, dx, dy):
    res = copy.deepcopy(rect)
    move_rectangle1(res, dx, dy)
    #res.corner.x = rect.corner.x + dx
    #res.corner.y = rect.corner.y + dy
    return res


def main():
    
    p1 = Point()
    p2 = Point()
    p1.x = 0
    p1.y = 0
    p2.x = 3
    p2.y = 4.5
    print distance_between_points(p1, p2)
    
    lumpy = Lumpy()
    lumpy.make_reference()

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0

    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print 'move'
    box2 = move_rectangle2(box, 50, 100)
    print box2.corner.x
    print box2.corner.y

    lumpy.object_diagram()


if __name__ == '__main__':
    main()
