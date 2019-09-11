import turtle
import math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def get_circumference(r):
    return math.pi * r * 2


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    angle = 360 / n
    # for i in range(n):
    #     t.fd(length)
    #     t.lt(angle)
    polyline(t=t, n=n, length=length, angle=angle)

# def circle(t, r):
#     circumference = math.pi * r * 2
#     n = int(math.fabs(circumference) / 3) + 3
#     length = circumference / n
#     polygon(t=t, length=length, n=n)

def circle(t, r):
    arc(t=t, r=r, angle=360)

def arc(t, r, angle):
    arc_length = get_circumference(r) * angle / 360
    n = int(math.fabs(arc_length) / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t=t, n=n, length=step_length, angle=step_angle)

if __name__ == "__main__":
    # create turtle
    my_turtle = turtle.Turtle()

    square(my_turtle, 50)
    square(my_turtle, -200)
    square(my_turtle, 63.75)
    square(my_turtle, -50)

    polygon(my_turtle, 50, 5)
    polygon(my_turtle, -200, 3)
    polygon(my_turtle, 63.75, 6)
    polygon(my_turtle, -50, 8)

    circle(my_turtle, 200)
    circle(my_turtle, -100)

    arc(my_turtle, 30, 90)
    arc(my_turtle, -40, 180)
    arc(my_turtle, 50, -270)
    arc(my_turtle, -60, -360)
