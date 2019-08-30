# exercises/5.6.2.py

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

def snowflake(t, length):
    for i in range(3):
        koch(t=t, length=length)
        t.rt(120)

my_turtle = turtle.Turtle()

snowflake(t=my_turtle, length=60)
