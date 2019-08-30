# 5: Conditionals and Recursion

## `5.1` Floor division and modulus

The **floor division** operator - `//` - will divide two numbers and round down to the nearest integer.

The **modulus** operator - `%` - will divide two numbers and *return* the *remainder*.

## `5.2` Boolean Expressions

**Boolean expression** - either true or false.

**`==`** operator compares two values and returns `True` if they are equal, `False` otherwise.

```python
# relational operators
x == y		# equal
x != y		# not equal
x > y		# greater than
x < y
x >= y		# greater than or equal to
x <= y
```

## `5.3` Logical Operators

* **`and`** returns `True` if both conditions are true
* **`or`** returns `True` if either condition is true
* **`not`** returns `True` if condition is false.

## `5.4` Conditional Execution

```python
# if statement is a conditional statement
if x == 3:				# condition
    print('x is 3')		
    # pass				# pass statement does nothing
```

## `5.5` Alternative Execution

```python
if hotdog:
    print('hotdog')
else:
    print('not hotdog')
```

## `5.6` Chained Conditionals

```python
# if more than two possibilities, use 'elif'

if x > 0:
    print('pos')
elif x < 0:
    print('neg')
else:
    print('equals zero')
```

## `5.7` Nested Conditionals

```python
# conditionals can be nested within other conditionals

if x == 0:
    print('equals zero')
else:
    if x < 0:
        print('neg')
    else:
        print('pos')
```

You should avoid nested conditionals if you can, since they become difficult to read.

Logical operators can sometimes be used to simplify nested conditionals by checking multiple conditions at once.

## `5.8` Recursion

A function can call itself *recursively*:

```python
def countdown(t):
    """
    given an integer,
    will countdown from that integer to zero.
    """
    if t <= 0:
        return	# return statement exits the function
    else:
        print(t)
        countdown(t-1)
```

***[See here for more information on recursive functions](https://youtu.be/MTCYhbfSAuA?t=275).***

## `5.10` Infinite Recursion

If a recursive function does not have a base case, it may recursively call itself until it crashes.

## `5.11` Keyboard Input

```python
def get_input():
    """
    get user input via prompt
    and print it
    """
	user_input = input()
	print(user_input)
```

---

## *`5.14` Exercises*

### `Exercise 5.1`

> Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.

```python
# exercises/5.1.py

import time

total_seconds = time.time()

s_in_min = 60
s_in_hour = s_in_min * 60
s_in_day = s_in_hour * 24

days = total_seconds // s_in_day
seconds_remaining = total_seconds % s_in_day

hours = seconds_remaining // s_in_hour
seconds_remaining = seconds_remaining % s_in_hour

minutes = seconds_remaining // s_in_min
seconds = seconds_remaining % s_in_min

print('days since epoch: {}'.format(days))
print('hours: {}'.format(hours))
print('minutes: {}'.format(minutes))
print('seconds: {}'.format(seconds))

```

### `Exercise 5.2`

> Fermat's Last Theorem says that there are no positive integers a, b, and c such that a<sup>n</sup> + b<sup>n</sup> = c<sup>n</sup> for any values of n greater than 2.

1. > Write a function named `check_fermat` that takes four parameters - `a`, `b`, `c`, and `n` - and checks to see if Fermat's theorem holds. If n is greater than 2 and a<sup>n</sup> + b<sup>n</sup> = c<sup>n</sup> the program should print, "Holy smokes, Fermat was wrong!" Otherwise, the program should print, "No, that doesn't work".

   ```python
   # exercises/5.2.1.py
   
   def check_fermat(a, b, c, n):
       if n > 2:
           if (a**n + b**n == c**n):
               print("Holy smokes, Fermat was wrong!")
           else:
               print("No, that doesn't work")
       else:
           print("No, that doesn't work")
   
   
   check_fermat(1, 2, 3, 4)
   
   ```

2. > Write a function that prompts the user to input values for `a`, `b`, `c`, and `n`, converts them to integers, and uses `check_fermat` to check whether they violate Fermat's theorem.

   ```python
   # exercises/5.2.2.py
   
   # fancy it up a bit
   print("CHECK FERMAT")
   print("--------------------------------")
   
   print("Input a value for a: ", end="")
   a = int(input())
   print("Input a value for b: ", end="")
   b = int(input())
   print("Input a value for c: ", end="")
   c = int(input())
   print("Input a value for n: ", end="")
   n = int(input())
   
   def check_fermat(a, b, c, n):
       if n > 2:
           if (a**n + b**n == c**n):
               print("Holy smokes, Fermat was wrong!")
           else:
               print("No, that doesn't work")
       else:
           print("No, that doesn't work")
   
   print("")
   print("checking if {} + {} == {}".format(a**n, b**n, c**n))
   print("...")
   
   check_fermat(a=a, b=b, c=c, n=n)
   
   ```

### `Exercise 5.3`

> If you are given three sticks, you may or may not be able to arrange them into a triangle. For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not be able to get the short sticks to meet in the middle. For any three lengths, there is a simple test to see if it is possible to form a triangle:
>
> > If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they form what is called a "degenerate" triangle.)
>
> > Check that *recursive* block quote ( ͡° ͜ʖ ͡°)

1. > Write a function named `is_triangle` that takes three integers as arguments, and that prints either "Yes" or "No", depending on whether you can or cannot form a triangle from sticks with the given lengths.

   ```python
   # exercises/5.3.1.py
   
   def is_triangle(a, b, c):
       check_a = bool(a <= b + c)
       check_b = bool(b <= a + c)
       check_c = bool(c <= a + b)
   
       if check_a and check_b and check_c:
           print("Yes")
       else:
           print("No")
   
   is_triangle(3, 4, 5)
   is_triangle(100, 1, 2)
   is_triangle(2, 3, 5)
   is_triangle(2, 3, 6)
   
   ```

2. > Write a function that prompts the user to input three stick lengths, converts them to integers, and uses `is_triangle` to check whether sticks with the given lengths can form a triangle.

   ```python
   # exercises/5.3.2.py
   
   print("side a: ", end="")
   side_a = int(input())
   print("side b: ", end="")
   side_b = int(input())
   print("side c: ", end="")
   side_c = int(input())
   
   def is_triangle(a, b, c):
       check_a = bool(a <= b + c)
       check_b = bool(b <= a + c)
       check_c = bool(c <= a + b)
   
       if check_a and check_b and check_c:
           print("Yes")
       else:
           print("No")
   
   is_triangle(a=side_a, b=side_b, c=side_c)
   
   ```

### `Exercise 5.4`

*Skipped because stack diagrams are dumb*

1. > What would happen if you called this function like this: `recurse(-1, 0)`?

   You would get a stack overflow, since `n` is already negative.

2. > Write a docstring that explains everything someone would need to know in order to use this function (and nothing else.)

   ```python
   # not using any formal docstring style
   # because those haven't been taught thus far.
   
   """
   prints n+(s*n)
   arguments: n:int, s:int
   """
   ```

### `Exercise 5.5`

> Read the following function and see if you can figure out what it does. Then run it and see if you got it right.

```python
# exercises/5.5.py

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

```

### `Exercise 5.6`

> The Koch curve is a fractal that looks something like Figure 5.2. To draw a Koch curve with length x, all you have to do is
>
> 1. Draw a Koch curve with length x/3
> 2. Turn left 60 degrees
> 3. Draw a Koch curve with length x/3
> 4. Turn right 120 degrees
> 5. Draw a Koch curve with length x/3
> 6. Turn left 60 degrees
> 7. Draw a Koch curve with length x/3
>
> The exception is if x is less than 3: in that case, you can just draw a straight line with length x.

1. > Write a function called `koch` that takes a turtle and a length as parameters, and that uses the turtle to draw a Koch curve with the given length.

   ```python
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
   
   ```

2. > Write a function called `snowflake` that draws three Koch curves to make the outline of a snowflake

   ```python
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
   
   ```

3. > The Koch curve can be generalized in several ways. See [link] for examples and implement your favorite.

   ```python
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
   
   ```

   