import math, turtle

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def petal(t, curve):
    n = 10  # looks pretty smooth, doesn't need math
    length = 100    # fixed size for petals
    polyline(t=t, n=n, length=length / n, angle=curve / n)
    t.lt(180 - (curve))
    polyline(t=t, n=n, length=length / n, angle=curve / n)
    t.lt(180 - (curve))

def flower(t, petals, curve, offset=0):
    t.lt(offset)
    for i in range(petals):
        petal(t=t, curve=curve)
        # rotate for next petal
        t.lt(360 / petals)

# instantiate turtle
my_turtle = turtle.Turtle()


# testing
## draw test flower
flower(t=my_turtle, petals=7, curve=45, offset=15)

## reset position, change color to red
my_turtle.pencolor("red")
my_turtle.pu()
my_turtle.setpos(0,0)
my_turtle.seth(0)
my_turtle.pd()

## draw second test flower
flower(t=my_turtle, petals=10, curve=100)

## reset position, change color to cyan
my_turtle.pencolor("cyan")
my_turtle.pu()
my_turtle.setpos(0,0)
my_turtle.seth(0)
my_turtle.pd()

## draw third test flower
flower(t=my_turtle, petals=20, curve=10)
