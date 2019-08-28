# 3: Functions

**Function** - a named sequence of *statements* that performs a computation.

* [Also known as a ***subroutine***; defined as a packaged unit of instructions to perform a specific task.](https://en.wikipedia.org/wiki/Subroutine)
* **Defined** by specifying a *name* and a sequence of *statements*.
* Can be **called** later in the program.

## `3.1` Function Calls

Example of calling the function `type()`:

```python
type(42)	# <class 'int'>
```

Functions can take **arguments**, which are given inside the parentheses.

Functions **return** a result, known as a **return value**.

```python
# examples of functions that convert types

int('32')		# 32

int('Hello')
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'Hello'
"""

## int() will always round down.
int(3.999)		# 3

## float() converts integers and strings of numbers
## to floating-point numbers:
float(46)		# 46.0
float('45.67')	# 45.67

## str() converts an argument to a string:
str(32)		# '32'
str('86.5')	# '86.5'
```

## `3.2` Math Functions

[**Module**](https://docs.python.org/3/tutorial/modules.html) - a file that contains a collection of related functions. The file name is the module name with the suffix `.py` appended. An example of a module is the [**math module**](https://docs.python.org/3/library/math.html).

To use a module, you must first import it:

```python
import math

## input the module name to get more info about it:
math		# <module 'math' (built-in)>
```

Then you can access the functions in the library using **dot notation**:

```python
## format: module.function

round_up = math.ceil(3.5)
print(round_up)				# 4

abs_val = math.fabs(-5)
print(abs_val)				# 5.0

radians = 0.7
height = math.sin(radians)
print(height)				# 0.644217687237691
```

## `3.3` Composition

Expressions and statements can be *composed* of other expressions or statements. A function can, for example, take another function as an argument:

```python
x = math.exp(math.log(x+1))
```

## `3.4` Adding Functions

**Function Definition** - specifies the name of a new function and the sequence of statements that fun when that function is called.

In Python, a function is **defined** using the keyword **`def`**, and the function name is followed by a set of parentheses specifying any **parameters** for the function.

The first line of the function - with `def` and the name - is the function **header**. A function header in Python must end with a **`:`**.

The rest of the function is the **body** - which, in Python, must be indented *4 spaces* and can contain an arbitrary number of statements.

Defining a function creates a **function object**, which has the `type` of `function`.

```python
def add_two_numbers(a, b):
    return a + b

type(add_two_numbers)		# <class 'function'>
```

Defined functions are called the same way as any other function:

```python
add_two_numbers(2, 3)		# returns 5
```

A function can be *composed* of other defined functions:

```python
def add_three_numbers(a, b, c):
    return add_two_numbers(a, b) + c

add_three_numbers(2, 3, 4)		# returns 9
```

## `3.5` Definitions and uses

A function cannot be called before it is defined; however, the order functions are defined in doesn't matter, so long as the function call is last:

```python
## This will run, even though print_lyrics() is defined
## after it is stated in the definition of
## repeat_lyrics(), since neither function is
## actually called until the last line.

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

repeat_lyrics()

```

## `3.6` Flow of Execution

**flow of execution** - the order statements are run in within a program.

* Execution begins at the first line of the program.
* Statements are run one by one in order from top to bottom.
* Function definitions do not alter the execution flow, but statements *within* functions are not run until the function is called.

## `3.7` Parameters and Arguments

**Parameters** - the variable(s) in a function declaration

**Arguments** - the actual value of this variable that gets passed to the function when the function is called.

[*(See this StackOverflow answer)*](https://stackoverflow.com/questions/156767/whats-the-difference-between-an-argument-and-a-parameter)

## `3.8` Variables and Parameters are local

Variables created inside a function are **locally scoped** - they only exist inside that function.

```python
def add_two_numbers(a, b):
    num_sum = a + b
    return num_sum

## if you try to print a variable inside a function,
## you get an exception
## since 'num_sum' does not exist in this scope.
print(num_sum)
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'num_sum' is not defined
"""

## fun fact: 'sum' is a built-in function
## that accepts an array of integers.
## Thus, my variable could not be named 'sum',
## as I learned the relatively hard way.
```

## `3.10` Fruitful Functions and Void Functions

**'Fruitful functions'** - functions that return a value.

```python
x = math.cos(radians)
```

* In a Python script this *return value* should be assigned to a variable for use in the program.

**Void functions** - perform some action, but do not return a value.

* Void functions return `None`.

## `3.11` Why Functions?

1. Grouping statements into named functions makes your program more organized, and thus easier to read and debug.
2. Functions eliminate repeated code by abstracting it into a function, thus making your code terser.
3. Well-designed functions can be debugged independently of the rest of the program.
4. Functions can be re-used, making your job as a programmer a bit easier.

---

## `3.14` *Exercises*

### `Exercise 3.1`

> Write a function named `right_justify` that takes a string named `s` as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

```python
def right_justify(s):
    print(' ' * (70-len(s)) + s)

```

### `Exercise 3.2`

```bash
# TO RUN:
python3 exercises/3.2.py
```



> A function object is a value you can assign to a variable or pass as an argument. For example, `do_twice` is a function that takes a function object as an argument and calls it twice:
>
> ```python
> def do_twice(f):
>     f()
>     f()
> ```
>
> Here's a example that uses `do_twice` to call a function named `print_spam` twice.
>
> ```python
> def print_spam():
>     print('spam')
>     
> do_twice(print_spam)
> ```

1. > Type this example into a script and test it.

   ```python
   ## output:
   spam
   spam
   ```

2. > Modify `do_twice` so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.

   ```python
   def do_twice(f, val):
       f(val)
       f(val)
   ```

3. > Copy the definition of `print_twice` form earlier in this chapter to your script.

4. > Use the modified version of `do_twice` to call `print_twice` twice, passing `spam` as an argument.

   ```python
   def do_twice(f, val):
       f(val)
       f(val)
   
   def print_twice(bruce):
       print(bruce)
       print(bruce)
   
   do_twice(print_twice, 'spam')
   ```

5. > Define a new function called `do_four` that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.

   ```python
   def do_twice(func, arg):
       func(arg)
       func(arg)
   
   def print_twice(bruce):
       print(bruce)
       print(bruce)
   
   def do_four(func, arg):
       """
       run a function four times with the given argument
       """
       do_twice(func, arg)
       do_twice(func, arg)
   
   do_twice(print_twice, 'spam')
   
   do_four(print_twice, 'spam')
   
   ```

### `Exercise 3.3`

> Note: this exercises should be done using only the statements and other features we have learned so far.

1. > Write a function that draws a grid like the following:
   >
   > [See book]

   ```python
   """
   exercises/3.3.1.py
   """
   
   def print_cell_border():
       print('+ ', end='')
       print('- '*4, end='')
   
   def print_cell_space():
       print('| ', end='')
       print('  '*4, end='')
   
   def print_grid():
       # top border
       print_cell_border()
       print_cell_border()
       print('+')
       # top row space
       print_cell_space()
       print_cell_space()
       print('|')
       print_cell_space()
       print_cell_space()
       print('|')
       print_cell_space()
       print_cell_space()
       print('|')
       print_cell_space()
       print_cell_space()
       print('|')
       # middle border
       print_cell_border()
       print_cell_border()
       print('+')
       # bottom row space
       print_cell_space()
       print_cell_space()
       print('|')
       print_cell_space()
       print_cell_space()
       print('|')
       print_cell_space()
       print_cell_space()
       print('|')
       print_cell_space()
       print_cell_space()
       print('|')
       # bottom border
       print_cell_border()
       print_cell_border()
       print('+')
   
   print_grid()
   ```

2. > Write a function that draws a similar grid with four rows and four columns

   ```python
   """
   exercises/3.3.2.py
   
   I think this could be refactored further,
   but it was tedious enough to do this much
   and this satisfies the requirements.
   """
   
   def do_twice(f):
       f()
       f()
   
   def do_four(f):
       do_twice(f)
       do_twice(f)
   
   def print_horiz_border_section():
       """
       Print one cell's border w/ left intersect
       """
       print('+ ', end='')
       print('- '*4, end='')
   
   def print_cell_space_section():
       """
       print one unit tall of cell space
       A cell is four of these tall
       """
       print('| ', end='')
       print('  '*4, end='')
   
   def print_horiz_border():
       """
       print four cells wide of border
       """
       do_four(print_horiz_border_section)
       print('+')
   
   def print_cell_space():
       """
       Print four cells of white space, then a right border
       """
       do_four(print_cell_space_section)
       print('|')
   
   def print_row():
       """
       Print a top border,
       then print four-tall of cell space
       """
       print_horiz_border()
       do_four(print_cell_space)
   
   def print_grid():
       """
       Print four rows, then print a bottom border
       """
       do_four(print_row)
       print_horiz_border()
   
   # actual final function call
   print_grid()
   
   ```

   