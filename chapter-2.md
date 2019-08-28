# 2: Variables, expressions, and statements

**variable** - a name that refers to a *value*.

* An **assignment statement** creates a new variable and gives it a value.

* ```python
  x = 24
  x		# 24
  ```

* A **state diagram** is a way of notating a variable with paper-and-pencil by drawing a line from the variable name to its value:

  * ```
    x -> 24
    ```

* Variable names cannot begin with numbers, contain illegal characters, or use reserved Python **keywords**.

  * ```python
    1cat = 'meow'
    """
      File "<stdin>", line 1
        1cat = 'meow'
           ^
    SyntaxError: invalid syntax
    """
    
    class = 'think python'
    """
      File "<stdin>", line 1
        class = 'think python'
              ^
    SyntaxError: invalid syntax
    """
    ```

**Expression** - a combination of one or more *values*, *variables*, or *operators*.

* When an expression is typed into the prompt, the interpreter **evaluates** it to compute the *value* of the expression.

**Statement** - any unit of code that has an effect - e.g. creating a variable or displaying a value.

* From [wikipedia](https://en.wikipedia.org/wiki/Statement_(computer_science)): A statement is a unit of code that expresses *some action* to be carried out.
* When a statement is typed into the prompt, the interpreter **executes** it.

## `2.4` Script Mode

**Interactive mode** - running python code by inputting it directly into the prompt.

**Script mode** - running python code from a script

**Script** - a program stored in a file.

## `2.5` Order of Operations

Python follows the normal mathematical convention for order of operations(PEMDAS).

## `2.6` String Operations

You cannot perform mathematical operations with strings.

The **`+`** operator performs **string concatenation** - it joins two strings into a single value.

The **`*`** operator performs repetition:

```python
'cat'*3		# catcatcat
```

* One of the values in the *expression* must be a *string*, and the other  an *integer*.

## `2.7` Comments

Comment lines begin with the `#` character and are not executed by the program. Comments can also be placed after code on the same line, and anything from the `#` sign to the end of the line will be ignored by the program.

```python
x = 10	# this is a comment.
```

## `2.8` Debugging

Three main categories of errors:

1. **Syntax Error** - There is a problem with the structure of your code.
2. **Runtime Error** - Error that occurs when the program is run that prevents the program from being parsed; also known as ***exceptions***.
3. **Semantic Error** - Your program will run, but it won't do what you expect it to do. These won't raise an error message because - from the computer's perspective - there wasn't actually an error.

---

## *`2.10` Exercises*

### `Exercise 2.1`

> Repeating my advice from the previous chapter, whenever you learn a new feature,you should try it out in interactive mode and make errors on purpose to see what goes wrong.

1. > We've seen that `n = 42` is legal. What about `42 = n`?

   ```python
   42 = n
   """
     File "<stdin>", line 1
   SyntaxError: can't assign to literal
   """
   ```

2. > How about `x = y = 1`?

   ```python
   x = y = 1	# no output
   x			# 1
   y			# 1
   ```

3. > In some languages every statement ends with a semi-colon, `;`. What happens if you put a semi-colon at the end of a Python statement?

   ```python
   x = 4;	# no output
   x		# 4
   ```

4. > What if you put a period at the end of a statement?

   ```python
   a = 6.	# no output
   a		# 6.0
   ```

5. > In math notation you can multiply x and y like this: `xy`. What happens if you try that in Python?

   ```python
   x = 4	# no output
   y = 2	# no output
   xy
   """
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'xy' is not defined
   """
   ```

### `Exercise 2.2`

> Practice using the Python interpreter as a calculator:

1. > The volume of a sphere with radius r is (4/3)πr^3. What is the volume of a sphere with radius 5?

   ```python
   pi = 3.14159
   r = 5
   v = (4/3)*pi*r**3
   v		# 523.5983333333332
   ```

2. > Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

   ```python
   x = 60
   unit_cost = 24.95 * 0.6
   total_shipping = 3 + (0.75 * x)
   total_cost = (unit_cost * x) + total_shipping
   total_cost		# 946.1999999999999
   ```

3. > If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

   ```python
   # calculate time spent running in seconds
   # run starts and ends with 1 mile @ 8:15/mile
   # total 2 miles @ 8:15/mile
   time_1_seconds = ((8 * 60) + 15) * 2
   # middle of run is 3 miles @ 7:12 per mile
   time_2_seconds = ((7 * 60) + 12) * 3
   total_seconds = time_1_seconds + time_2_seconds
   # convert time spent running to minutes, seconds
   minutes = total_seconds // 60
   seconds = total_seconds % 60
   print(str(minutes) + ', ' + str(seconds))
   
   # calculate return time
   hour = 7
   # 8 minutes remaining in previous hour
   minute = minutes - (60 - 52)
   
   # print return time
   print(str(hour) + ":" + str(minute))
   ```

   