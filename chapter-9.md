# 9: Case study: word play

## `9.2`

Files can be opened and read using `open('filename')`

`fin` is a common name for variables containing `f`ile `in`put.

## *Exercises*

### `Exercise 9.1`

```python
fin = open('words.txt')

for word in fin:
    if len(word.strip()) > 20:
        print(word)

```

Remaining exercises are explained in the following sections, and the files are in `/case-study-2`

## `9.3` Search

All case study exercises can be solved with the `search` pattern from the prior section:

```python
# Exercise 9.2

def has_no_e(word):
    """
    takes a word as a string
    returns True if the word does not contain the letter 'e'
    """
    for letter in word:
        if letter == 'e':
            return False
    return True

print(has_no_e('racecar'))
print(has_no_e('dynamo'))

```

```python
# Exercise 9.3

# a generalized version of `has_no_e()`

def avoids(word, forbidden):
    """
    takes a word as a string and a string of forbidden letters
    returns True if the word does not contain any forbidden letter
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True

```

```python
# Exercise 9.4

# same as 9.3, but reverse `in` condition to `not in`

fin = open('case-study-2/words.txt')

def uses_only(word, letters):
    """
    takes a word as a string and a string of letters
    returns True if the word contains only given letters
    """
    for letter in word:
        if letter not in letters:
            return False
    return True

```

```python
# Exercise 9.5

# same as 9.4, but the search parameters are reversed:

fin = open('case-study-2/words.txt')

def uses_only(word, letters):
    """
    takes a word as a string and a string of letters
    returns True if the word contains only given letters
    """
    for letter in word:
        if letter not in letters:
            return False
    return True


print(uses_only('racecar', 'race'))
print(uses_only('dynamo', 'yg'))

```

## `9.4` Looping with Indices

```python
# Exercise 9.6

def is_abecedarian(word):
    """
    takes a word as a string
    returns True if letters in a word are in alphabetical order
    """
    # track previous letter, start with first letter
    previous_letter = word[0]
    for letter in word:
        # compare previous letter to current letter
        if letter < previous_letter:
            return False
        previous_letter = letter
    return True
```

## `9.5` Debugging

When testing, try to consider all cases - even **special cases** such as an empty string, or data of the wrong type.