# exercises/15.2.py

import copy, math, turtle

from mypolygon import arc, polyline

class Point:
    # ...
    pass

class Rectangle:
    # ...
    pass

class Circle:
    # ...
    pass

def position_turtle(x, y, turtle):
    """
    takes an instance of Turtle and an x and y coordinate
    places the given turtle at that position
    """
    turtle.pu()
    turtle.setpos(x=x, y=y)
    turtle.pd()

def draw_circle(circle, turtle):
    """
    takes an instance of Circle and an instance of Turtle
    draws given Circle using given Turtle
    """
    # start drawing from bottom edge
    position_turtle(turtle=turtle, x=circle.center.x, y=circle.center.y - circle.radius)
    arc(t=turtle, r=circle.radius, angle=360)

def draw_rect(rectangle, turtle):
    """
    takes an instance of Rectangle and an instance of Turtle
    draws given Rectangle using given Turtle
    """
    position_turtle(turtle=turtle, x=rectangle.origin.x, y=rectangle.origin.y)
    for i in range(2):
        polyline(t=turtle, n=1, length=rectangle.width, angle=90)
        polyline(t=turtle, n=1, length=rectangle.height, angle=90)

if __name__ == '__main__':
    t = turtle.Turtle()

    circle = Circle()
    circle.center = Point()
    circle.center.x = 200
    circle.center.y = 100
    circle.radius = 50

    rectangle = Rectangle()
    rectangle.origin = Point()
    rectangle.origin.x = -50
    rectangle.origin.y = -50
    rectangle.width = 100
    rectangle.height = 150

    draw_circle(circle=circle, turtle=t)

    draw_rect(rectangle=rectangle, turtle=t)
