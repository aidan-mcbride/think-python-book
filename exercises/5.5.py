import turtle

my_turtle = turtle.Turtle()

def draw(t, length, n):
    """
    My guess:
    draws a tree-like branching structure
    """
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

draw(my_turtle, 50, 5)
