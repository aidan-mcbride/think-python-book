# 8: Strings

## `8.1` A string is a sequence

A string is a sequence of characters, each of which can be accessed by index.

```python
my_string = 'gooby'
my_string[0]	# 'g'
my_string[2]	# 'o'
```

Negative indices count from the end of the string

```python
my_string[-1]	# 'y'
```

## `8.3` Traversal with a `for` loop

**traversal** - iterating over some sequence.

```python
# exercise:
## reverse a string using a `while` loop,
## print one letter per line

print("input string:", end=" ")
string = str(input())

def reverse_string(string):
    index = 1
    while (index <= len(string)):
        char = string[index * -1]
        print(char)
        index = index + 1

reverse_string(string)

```

## `8.4` String Slices

**slice** - segment of a string.

```python
s = 'Monty Python'
# select a slice with slice[n:m]
# where n is the start index
# and m is the end index
s[0:5]		# 'Monty`
s[:5]		# 'Monty'
s[6:]		# 'Python'
s[:]		# 'Monty Python'
```

## `8.5` Strings are immutable

**Immutable** - can't be changed.

```python
string = 'gooby'
string[0] = 'b'
# TypeError: 'str' object does not support item assignment
```

## `8.6` Searching

example of **search** pattern:

```python
def find(word, letter, start_index=0):
    """
   	returns index of first instance of given letter
   	within given word
   	takes optional start index
   	returns -1 if letter not found
    """
    index = start_index
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
```

## `8.7` Looping and Counting

Example of **counter** pattern:

```python
def count(word, letter):
    """
    returns count of how many times a given letter
    appears in a given word
    """
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    return count
```

## `8.8` String Methods

Strings can be manipulated with **[string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)**

A call of a method is called an *invocation*.

```python
# `find` method returns first index where a given substring appears in a string.
string = 'gooby'
string.find('o')		# 1
string.find('y')		# 4
```

## `8.9` The `in` operator

The **`in`** operator takes two strings and returns `true` if the fist string appears as a *substring* in the second string.

## `8.10` String Comparison

**`==`** operator compares two strings

**`<`** and **`>`** operators can be used to sort alphabetically:

```python
string = 'Apples'
string2 = 'Carrots'
string > string2		# False
string < string2		# True
```

---

## *Exercises*

### `Exercise 8.2`

> There is a string method called `count` that is similar to the function in section 8.7. Read the documentation of this method and write an invocation that counts the number of `'a'`s in `'banana'`

```python
string = 'banana'
string.count('a')
```

### `Exercise 8.3`

> ...
>
> Write a one-line version of `is_palindrome` from Exercise 6.3

```python
def is_palindrome(string):
    return string == string[::-1]
```

### `Exercise 8.5`

> Caesar Cypher
>
> ...
>
> Write a function called `rotate_word` that takes a string and an integer as parameters, and returns a new string that contains the letters from the original string rotated by the given amount.

```python
# exercises/8.5.py

def rotate_letter(letter, amount):
    if letter.isupper():
        start_code = ord('A')
    elif letter.islower():
        start_code = ord('a')
    else:
        # if 'letter' is not a letter, don't rotate
        return letter

    # rotate letter *within* range of alphabet
    letter_code = ord(letter) - start_code
    # '%' will return operand if under 26
    # or operand - 26 if over 26
    new_letter_code = (letter_code + amount) % 26 + start_code
    return chr(new_letter_code)

def rotate_word(word, amount=0):
    rv = ''
    for letter in word:
        rv = rv + rotate_letter(letter, amount)
    return rv

# tests from solution in book
print(rotate_word('cheer!', 7))
print(rotate_word('melon', -10))
print(rotate_word('Sleep', 9))

```

