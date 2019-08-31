# 6: Fruitful Functions

## `6.1` Return values

**`return`** statements exit the current function with a specified value.

* Code placed after a return statement will not run; the book calls it *dead code*.

```python
# exercise from end of section

def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1
```

## `6.2` Incremental development

**Incremental development:** the process of adding and testing only a small amount of code at a time, with the goal of reducing time spent debugging.

* [See: Test-Driven Development](https://en.wikipedia.org/wiki/Test-driven_development)

```python
# exercise from end of section:
## write a function called `hypotenuse` that
## returns the length of the hypotenuse of a right
## triangle given the lengths of the other two legs
## as arguments.
## record each stage of the development proces.


# define parameters
def hypotenuse(a, b):
    print(a)
    print(b)
    
# create variables
def hypotenuse(a, b):
    a_square = a**2
    b_square = b**2

    print(a)
    print(a_square)
    print(b)
    print(b_square)

hypotenuse(3, 5)
    
# calculate and return hypotenuse
import math

def hypotenuse(a, b):
    a_square = a**2
    b_square = b**2

    hypotenuse = math.sqrt(a_square + b_square)
    return hypotenuse

print(hypotenuse(3, 5))
```

## `6.4` Boolean Functions

Functions can *return* boolean values.

These types of functions are useful for checking conditions

```python
def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False
    
print(is_between(2, 3, 5))	# True
print(is_between(7, 4, 6))	# False
```

## `6.8` Checking Types

Runtime errors can occur when the argument passed to a function is of the incorrect type.

You can check the type of a variable using `isinstance`, which is useful for validating arguments within a function.

```python
def is_int(n):
    if not isinstance(n, int):
        return False
    return True
    
```

The book calls this the **guardian** pattern, where-by checks are placed at the beginning of a function to protect later code from  values that would break it.

---

## *`6.11` Exercises*

### `Exercise 6.1`

> Draw a stack  diagram for the following program.

*Skipped*

### `Exercise 6.2`

> Write a function named `ack` that evaluates the Ackermann function. Use your function to evaluate `ack(3, 4)`, which should be 125. What happens for larger values of `m` and `n`?

```python
# exercises/6.2.py

def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))

print(ack(3, 4))
print(ack(-1, 500)) # should break
print(ack(20, 50))  # RuntimeError: maximum recursion depth exceeded

```

### `Exercise 6.3`

> A palindrome is a word that is spelled the same backward and forward, like "noon" and "redivider". Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.
>
> The following are functions that take a string argument and return the first, last, and middle letters:
>
> ```python
> def first(word):
>     return word[0]
> 
> def last(word):
>     return word[-1]
> 
> def middle(word):
>     return word[1:-1]
> ```

1. > Type these functions into a file named `palindrome.py` and test them out. What happens if you call `middle` with a string with only two letters? One letter? What about the empty string, which is written `''` and contains no letters?

   ```python
   # exercises/palindrome.py
   
   def first(word):
       return word[0]
   
   def last(word):
       return word[-1]
   
   def middle(word):
       return word[1:-1]
   
   
   # tests
   print(first('cat')) # c
   print(first('x'))   # x
   print(first(''))    # IndexError: string index out of range
   
   print(last('cat'))  # t
   print(last('x'))    # x
   print(last(''))     # IndexError: string index out of range
   
   print(middle('cat'))    # a
   print(middle('xy'))     # ''
   print(middle('x'))      # ''
   print(middle(''))       # ''
   
   ```

2. > Write a function called `is_palindrome` that takes a string argument and returns `True` if it is a palindrome and `False` otherwise. Remember that you can use the built-in function `len` to check the length of a string.

   ```python
   # exercises/6.3.2.py
   
   def first(word):
       return word[0]
   
   def last(word):
       return word[-1]
   
   def middle(word):
       return word[1:-1]
   
   def is_palindrome(word):
       # a one-letter word is a palindrome
       if len(word) <= 1:
           return True
       if first(word) != last(word):
           return False
       return is_palindrome(middle(word))
   
   print(is_palindrome('racecar'))
   print(is_palindrome('goldfish'))
   print(is_palindrome('abcdba'))
   print(is_palindrome('redivider'))
   
   ```

### `Exercise 6.4`

> A number, `a` is a power of `b` if it is divisible by `b` and `a/b` is a power of `b`. Write a function called `is_power` that takes parameters `a` and `b` and returns `True` if `a` is a power of `b`. Note: you will have to think about a base case.

```python
# exercises/6.4.py

def is_power(a, b):
    """
    return True if a is a power of b
    otherwise return false
    """
    if a % b == 0:
        # a^1 == a
        if a == b:
            return True
        else:
            return is_power(a/b, b)
    return False

print(is_power(64, 2))
print(is_power(1000, 10))
print(is_power(1001, 10))

```

