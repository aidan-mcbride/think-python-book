# 4: Case Study: Interface Design

## `4.1` The turtle module

Python has a module named [`turtle`](https://docs.python.org/3.7/library/turtle.html), which allows you to create primitive graphics.

You can import the turtle module with `import turtle`.

*The `mypolygon.py` file referenced in this chapter is in `exercises/mypolygon.py`.*

the `turtle` module has a function called `Turtle`, which creates a Turtle *object*.

**Method** - a *function* associated with an *object*. A method is called using dot notation on the object to which it is associated:

```python
# call fd method on my_turtle obj.
my_turtle.fd(100)
```

## `4.2` Simple Repitition

```python
## This:
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)

## can be rewritten using a for loop:
for i in range(4):
    bob.fd(100)
    bob.lt(90)
```

---

## *`4.3` Exercises*

*See `exercises/mypolygon.py`*

---

## `4.4` Encapsulation

```python
# 4.3.1 - square function
import turtle

my_turtle = turtle.Turtle()

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
        
square(my_turtle)
```

[**Encapsulation**](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)) - bundling together related pieces of code into a named function.

By creating named functions we make out code easier to read and re-use.

*Note: I don't think the book's definition is 100% correct; it doesn't match with other definitions from i.e. Wikipedia or StackOverflow. I think what is being referred to here is more like **abstraction**.*

## `4.5` Generalization

```python
# 4.3.2 - square function w/ length param

import turtle

my_turtle = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
        
square(my_turtle, 50)
square(my_turtle, 200)
square(my_turtle, 63.75)
square(my_turtle, -50)
```

**Generalization** - making a function more general-purpose by adding parameters to the function definition.

```python
# 4.3.3 - polygon function
import turtle

def polygon(t, length, n):
    t = turtle.Turtle()
    angle = 360 // n

    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(my_turtle, 50, 5)
polygon(my_turtle, 200, 3)
## keyword arguments:
polygon(t=my_turtle, length=63.75, n=6)
polygon(t=my_turtle, length=-50, n=8)
```

When passing *arguments* to a function, you can specify which *parameter* the argument is for; These style of arguments are **keyword arguments**.

## `4.6` Interface Design

```python
# 4.3.4 - circle function

import math, turtle

my_turtle = turtle.Turtle()

def circle(t, r):
    circumference = math.pi * r * 2
    n = (circumference // 3) + 3	# from book
    length = circumference / n
    polygon(t, length, n)
        
circle(my_turtle, 200)
circle(t=my_turtle, r=-100)
```

**Function Interface** - summary of how the function is  used:

* Parameters
* What the function does
* Return value

## `4.7` Refactoring

We cannot re-use `polygon()` to create `arc()` the same way we did with `circle()`. Instead, we will create a general function named `polyline()`, then **refactor** `polygon()` to use `polyline()`.

```python
# polyline function
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
```

```python
# refactored polygon function
def polygon(t, length, n):
    angle = 360 / n
    polyline(t=t, n=n, length=length, angle=angle)
```

```python
# refactored circle function
def circle(t, r):
    arc(t=t, r=r, angle=360)
```

```python
# arc function
def arc(t, r, angle):
    arc_length = get_circumference(r) * angle / 360
    n = int(math.fabs(arc_length) / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t=t, n=n, length=step_length, angle=step_angle)
```

**Refactoring** - the process of rearranging a program to improve its *interfaces* and facilitate code re-use.

* Often involves *abstracting* repeated statements into functions.

> If we had planned ahead, we might have written `polyline` first and avoided refactoring, but **often you don't know enough at the beginning of a project to design all the interfaces.**

## `4.8` A development plan

**Development plan** - a process for writing programs. The process used in this case study is *"encapsulation and generalization"*:

1. Write a small program with no function definitions.
2. Once program works, identify pieces of it to encapsulate and name.
3. Generalize the function by adding appropriate parameters to its interface.
4. Repeat steps 1 through 3 until you have encapsulated as many functions as you can. In this phase, copy and paste code to avoid retyping or creating bugs.
5. Look for opportunities to *refactor*.

## `4.9` Docstring

A **docstring** is a string at the beginning of a function that explains the interface. Docstrings are enclosed in triple-quotes:

```python
'''
This is a docstring
'''
"""
This is also a docstring
"""
```

A well-designed interface should be simple to explain: if it is hard to write a docstring, your function or interface should be refactored.

## `4.10` Debugging

**preconditions** - conditions that a function expects to be true before it runs - e.g. our polygon functions have the *precondition* that a turtle object exists.

* **postconditions** are things that should be true *after* the function has run - i.e. the effects of the function.

Preconditions are the responsibility of function's caller. If the caller fails to meet the preconditions, the bug is in the caller, not the function.

If all preconditions are met and there is still a bug, it is with the function itself.

---

## *`4.12` Exercises*

*Skipping `4.1` - I don't care about stack diagrams - I'm not even certain that they are a common thing outside of this book.*

### `Exercise 4.2`

> Write an appropriately general set of functions that can draw shapes as in figure 4.1.

```python
# exercises/4.2.py

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
```

### `Excercise 4.3 - 4.5`

*I'm also skipping these, because the last one was very tedious and these next ones look even more tedious - especially the one where you draw all the letters. I also don't plan to ever use the turtle module again, so becoming intimately familiar with it is a waste of time.*

