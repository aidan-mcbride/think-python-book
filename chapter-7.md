# 7: Iteration

## `7.2` Updating variables

```python
# update the value of a variable based on its
# previous value
x = 2
x = x * 2
print(x)	# 4

y = y * 2
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
"""
```

## `7.3` The `while` statement

**`while`** iterate *while* some condition is true.

```python
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('ding')
```

## `7.4` `break`

The `break` statement can be used to terminate a `while` loop.

## `7.6` Algorithms

**Algorithm** - a *mechanical* general process for solving a type of problem.

---

## *`7.9` Exercises*

### `Exercise 7.1`

> Copy the loop from section 7.5 and encapsulate it in a function called `mysqrt` that takes `a` as a parameter, chooses a reasonable value of `x`, and returns an estimate of the square root of `a`.
>
> To test it, write a function named `test_square_root` that prints a table like [example]

```python
# exercises/7.1.py

import math

def mysqrt(a):
    x = a/2
    while True:
        y = (x + a/x) / 2
        if y == x:
            return y
        x = y

def test_square_root():
    # header row
    print("a", end="\t")
    print("mysqrt(a)", end="\t")
    print("math.sqrt(a)", end="\t")
    print("diff")
    # divider row
    print("-", end="\t")
    print("---------", end="\t")
    print("------------", end="\t")
    print("----")
    # results rows
    for i in range(9):
        # range is 0 index:
        # convert to 1-index floating point
        a = float(i+1)
        print(a, end="\t")
        print(mysqrt(a), end="\t")
        print(math.sqrt(a), end="\t")
        print(math.fabs(mysqrt(a) - math.sqrt(a)))

test_square_root()

```

### `Exercise 7.2`

>Write a function called `eval_loop` that iteratively prompts the user, takes the resulting input, and evaluates it using `eval`, and prints the result.
>
>It should continue until the user enters `'done'`, and then return the value of the last expression it evaluated.

```python
# exercises/7.2.py

def eval_loop():
    eval_return = None
    while True:
        print("Enter a statement to be evaluated:", end=" ")
        user_input = str(input())
        if user_input == 'done':
            return eval_return
        eval_return = eval(user_input)
        print(eval_return)

print(eval_loop())

```
