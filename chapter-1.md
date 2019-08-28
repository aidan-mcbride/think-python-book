# 1: The way of the Program

* **program** - sequence of instructions on how to do a computation.
  * take input
  * output something
  * do calculation
  * conditionals
  * loops

```bash
## Launch python 3.x interpreter in terminal
python3

## Launch python 2.x interpreter
python
```

## `1.3, 1.4` First Program

```python
# Print 'Hello, World!' in interpreter
print('Hello, World!')

# Arithmetic operations
+ - * / // **	# operators
## Addition
40 + 2		# 42
## Subtraction
43 - 1		# 42
## Multiplication
6 * 7		# 42
## Division(float)
84 / 2		# 42.0
## Division(int)
84 // 2		# 42
## Exponentiation
6**2 + 6	# 42
```

## `1.5` Values and Types

* [**Value**](https://en.wikipedia.org/wiki/Value_(computer_science)) - the representation of some entity in a program.

  * Values are of different **types**:

    * types: categories of values

  * ```python
    type(2)		# <class 'int'>
    type(42.0)	# <class 'float'>
    type('Hello, World!')	# <class 'str'>
    
    type('2')	# <class 'str'>
    type('42')	# <class 'str'>
    ```

## `1.6` Formal and Natural Languages

* **Natural Languages** - spoken languages, such as English or Italian; Evolved naturally rather than being designed.
* **Formal Languages** - languages designed by people for a specific purpose, such as math, music, or **programming** languages.
  * Strict syntax rules for the structure of statements.
    * **tokens** - elements of a language - e.g. words, numbers, music notes.
    * **structure** - how tokens are combined - e.g. phrases, equations.

---

## *`1.9` Exercises*

### `Exercise 1.1`

> It  is  a  good  idea  to  read  this  book  in  front  of  a  computer  so  you  can  try  out  the examples as you go.Whenever you are experimenting with a new feature, you should try to make mistakes. For example,in the “Hello, world!” program, what happens if you leave out one of the quotation marks? What if you leave out both? What if you spell `print` wrong?This kind of experiment helps you remember what you read; it also helps when you are programming,because you get to know what the error messages mean.  It is better to make mistakes now and on purpose than later and accidentally.

1. > In a print statement, what happens if you leave out one of the parentheses, or both?

   ```python
   print('Hello, world!'		# ...
   ```

2. > If you are trying to print a string, what happens if you leave out one of the quotation marks,or both?

   ```python
   print(Hello, world!)
   """
     File "<stdin>", line 1
       print(Hello, world!)
                         ^
   SyntaxError: invalid syntax
   """
   
   print('Hello, world!)
   """
     File "<stdin>", line 1
       print('Hello, world!)
                           ^
   SyntaxError: EOL while scanning string literal
   """
   ```

3. > You can use a minus sign to make a negative number like`-2`. What happens if you put a plus sign before a number? What about `2++2`?

   ```python
   +2		# 2
   2++2	# 4
   2+-2	# 0
   +2-+2	# 0
   ```

### `Exercise 1.2`

> Start the Python interpreter and use it as a calculator.

1. > How many seconds are there in 42 minutes 42 seconds?

   ```python
   42*60 + 42		# 2562
   # double-check order of operations
   42*60			# 2520
   2520 + 42		# 2562
   ```

2. > How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

   ```python
   10 * 1.61		# 16.1
   ```

3. > If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?

   ```python
   # Average pace
   ## seconds per mile
   2562 / 10		# 256.2
   ## minutes & seconds per mile
   ## (gonna bust out some advanced knowledge)
   seconds = 256.2 % 60
   m = 256.2 - seconds
   minutes = m / 60
   print ("{}, {}".format(minutes, seconds))
   # 4.0, 16.19999999999999
   # or, 4 minutes 16.2 seconds per mile
   
   # check work:
   4 * 60		# 240
   240 + 16.2	# 256.2
   256.2 * 10	# 2562
   # all checks out
   ```

   