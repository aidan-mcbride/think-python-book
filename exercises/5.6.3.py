# exercises/5.6.3.py

# implementation of the Cesàro fractal variant

import turtle

def koch(t, length, angle):
    if length >= 3:
        koch(t=t, length=length/3, angle=angle)
        t.lt(angle)
        koch(t=t, length=length/3, angle=angle)
        t.rt(angle*2)
        koch(t=t, length=length/3, angle=angle)
        t.lt(angle)
        koch(t=t, length=length/3, angle=angle)
    else:
        t.fd(length)

def snowflake(t, length, angle):
    for i in range(3):
        koch(t=t, length=length, angle=angle)
        t.rt(120)

my_turtle = turtle.Turtle()

snowflake(t=my_turtle, length=240, angle=85)
