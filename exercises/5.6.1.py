# exercises/5.6.1.py

import turtle

def koch(t, length):
    if length >= 3:
        koch(t, length/3)
        t.lt(60)
        koch(t, length/3)
        t.rt(120)
        koch(t, length/3)
        t.lt(60)
        koch(t, length/3)
    else:
        t.fd(length)

my_turtle = turtle.Turtle()

koch(t=my_turtle, length=120*4)
