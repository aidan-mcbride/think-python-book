# exercises/15.1.py

import copy, math

class Point:
    """
    represents a point in 2D space

    Attributes:
        x: x coordinate
        y: y coordinate
    """

class Rectangle:
    """
    represents a 2D rectangle

    Attributes:
        origin: Point
        width: integer
        height: integer
    """

class Circle:
    """
    represents a 2D circle

    Attributes:
        center: Point
        radius: integer
    """

def distance_between_points(p1, p2):
    """
    takes two instances of Point
    returns the distance between the two Points' coordinates
    """
    x_dist = math.fabs(p1.x - p2.x)
    y_dist = math.fabs(p1.y - p2.y)
    return math.sqrt(x_dist**2 + y_dist**2)

def point_in_circle(circle, point):
    """
    takes an instance of a Circle and an instance of a Point
    returns True if the coordinates of the Point are within the Circle.
    """
    # the border of a circle is all points whose
    # distance from the center is equal to the radius of the circle.
    # any point whose distance from the center is
    # less than the radius is within the circle.
    dist = distance_between_points(p1=circle.center, p2=point)
    return dist <= circle.radius

def rect_in_circle(circle, rect):
    """
    takes an instance of Circle and an instance of Rectangle
    returns True if the given rectangle is entirely within the given circle.
    """
    # start in bottom left,
    # rotate clockwise, checking that each corner is in the circle.
    corner = copy.copy(rect.origin)
    if not point_in_circle(circle, point=corner):
        return False
    corner.x += rect.width
    if not point_in_circle(circle, point=corner):
        return False
    corner.y += rect.height
    if not point_in_circle(circle, point=corner):
        return False
    corner.x -= rect.width
    if not point_in_circle(circle, point=corner):
        return False
    return True

def rect_circle_overlap(circle, rect):
    """
    takes an instance of Circle and an instance of Rectangle
    returns True if any of the corners of the rectangle are within the circle.
    """
    # inverse of previous function
    corner = copy.copy(rect.origin)
    if point_in_circle(circle, point=corner):
        return True
    corner.x += rect.width
    if point_in_circle(circle, point=corner):
        return True
    corner.y += rect.height
    if point_in_circle(circle, point=corner):
        return True
    corner.x -= rect.width
    if point_in_circle(circle, point=corner):
        return True
    return False

if __name__=="__main__":
    circle = Circle()
    circle.center = Point()
    circle.center.x = 150
    circle.center.y = 100
    circle.radius = 75

    rectangle = Rectangle()
    rectangle.origin = Point()
    rectangle.origin.x = 140
    rectangle.origin.y = 90
    rectangle.width = 20
    rectangle.height = 20

    print(rect_circle_overlap(rect=rectangle, circle=circle))
