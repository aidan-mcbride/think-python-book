# 15: Classes and Objects

**Class** - a programmer-defined *type*.

**Object** - an *instance* of a *class*.

* Creating a new object is called *instantiation*.

* **Attributes** are named elements of an instance and are assigned to an instance with *dot notation*. Attributes are accessed the same way:

  ```python
  class Point:
      """represents a point in 2-d space"""
      pass
  
  instance = Point()	# instantiate class as 'instance'
  instance.x = 6
  instance.y = 10
  print(instance.x)	# prints 6
  ```

* Objects and their attributes are mutable.

* Objects can be copied using the [**`copy`**](https://docs.python.org/3.7/library/copy.html) module:

  ```python
  p1 = Point()
  p1.x = 4
  p1.y = 12
  
  import copy
  p2 = copy.copy(p1)
  
  p1 is p2	# false
  ```

* A **shallow copy** will copy an object and any references in it, but not any ***embedded objects*** - objects as attributes.

* A **deep copy** copies an object and any objects it refers to.

* `isinstance()` can be used to check whether an *object* is an instance of a *class*.

* `hasattr(obj, attr)` can be used to check if a given `object` has a given `attribute`.

---

## *Exercises*

>As an exercise, write a function called `distance_between` that takes two Points as arguments and returns the distance between them.

```python
import math

class Point:
    """
    represents a point in 2D space
    """

def distance_between(point1, point2):
    """
    computes the distance between two points
    each with an x and y attribute
    """
    x_dist = math.fabs(point1.x - point2.x)
    y_dist = math.fabs(point1.y - point2.y)

    return(math.sqrt(x_dist**2 + y_dist**2))

```

> As an exercise, write a function named `move_rectangle` that takes a Rectangle and two numbers named `dx` and `dy`. It should change the location of the rectangle by adding `dx` to the `x` coordinate of `corner` and adding `dy` to the `y` coordinate of `corner`.

```python
def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
```

> As an exercise, write a version of `move_rectangle` that creates and returns a new Rectangle instead of modifying the old one.

```python
import copy

def move_rectangle(rect, dx, dy):
    new_rect = copy.deepcopy(rect)
    new_rect.corner.x += dx
    new_rect.corner.y += dy
    return new_rect
```

### `Exercise 15.1`

> Write a definition for a class named `Circle` with attributes `center` and `radius`, where `center` is a `Point` object and radius is a number.
>
> Instantiate a `Circle` object that represents a circle with its center at (150, 100) and a radius of 75.
>
> Write a function named `point_in_circle` that takes a `Circle` and a `Point` and returns `True` if the `Point` lies in or on the boundary of the circle.
>
> Write a function named `rect_in_circle` that takes a `Circle` and a `Rectangle` and returns `True` if any of the corners of the `Rectangle` fall inside the circle.

```python
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

```

### `Exercise 15.2`

> Write a function called `draw_rect` that takes a Turtle object and a Rectangle and uses the Turtle to draw the Rectangle.
>
> Write a function called `draw_circle` that takes a Turtle and a Circle and draws the Circle.

```python

```

