# 11: Dictionaries

A **dictionary** is a *mapping* of **keys** to **values** in **key-value pairs**.

To create an empty dictionary:

```python
new_dict = dict()
new_dict = {}
new_dict	# {}
```

To add key-value pairs to a dictionary, or to re-assign existing key-value pairs, use square brackets like when re-assigning values in a list:

```python
dog = dict()
print(dog)		# {}
dog['name'] = "mr. beans"
print(dog)		# {'name': 'mr. beans'}

# get value of key:
dog['name']		# 'mr. beans'
```

To check for the presence of *keys* within a dictionary, use the `in` operator:

```python
dog = dict(name='mr. beans', age=7)
'name' in dog		# True
'owner' in dog		# False
```

To check for the presence of *values*, you can use the `values()` method, and then use the `in` operator on the return value:

```python
dog_vals = dog.values()
'mr. beans' in dog_vals	# True
'spot' in dog_vals		# False
```

Dictionaries have a useful method called `get` that takes a `key` and a `default value` - if the key appears in the dictionary, the value of that key is returned, otherwise the default value is returned.

```python
# useful function:
# displays frequency that items appear in a dictionary

def histogram(string):
    d = dict()
    for char in string:
        d[char] = d.get(char, 0) + 1
    return d
```

Dictionary *keys* can be traversed in a `for` loop:

```python
h = histogram('parrot')
for key in h:
    # print key, value
    print(key, h[key])
```

**Lookup:** find the *value* of a given *key*.

```python
v = d[k]
```

**Reverse Lookup:** find the *key* for a given *value*.

```python
def reverse_lookup(d, val):
    """returns FIRST key with given value"""
    for k in d:
        if d[k] == val:
            return k
        # if none found
        raise LookupError()
```

* Where-as a dictionary can only have one instance of a key name, Multiple keys can have equivalent values.
* Reverse lookups are slower than forward lookups

### Raising Exceptions

**Raise statement(`raise`)** will cause an exception to occur, which will print a traceback and an error message.

* You can pass a detailed error message as an optional argument to a raise statement:

  ```python
  >>> raise LookupError('value does not exist in dictionary')
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  LookupError: value does not exist in dictionary
  ```

## `11.6` Memos

**Memos** store previously-computed values for some function so that on future calls of that function it will run faster.

Example: The recursive Fibonacci function which becomes exponentially slower the greater the value of `n` is:

```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1:
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

Can be memoized:

```python
# track previously computed values
known ={0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    # compute new value
    rv = fibonacci(n-1) + fibonacci(n-2)
    # add to known values
    known[n] = rv
    return rv
```

## `11.7` Global Variables

variables created outside the scope of a function are called **global variables** and can be used from within any function. Global variables are persisted from one function call to the next.

Global variables can only be reassigned from within a function if they are first declared as global variables:

```python
g = False

def set_g():
    global g	# declare g as a global variable
    g = True
```

If a global variable is not declared in a function, that function will instead create a **local variable** with the same name.

Global variables with ***mutable*** values can be *modified* from within a function without being declared as globals, but they still can't be reassigned. *(e.g. you can add/remove/change elements of a global list)*

## `11.8` Debugging

Tips for debugging programs with large datasets:

1. **Reduce the size of your input data**
2. **Check summaries and types** instead of, say, printing the entire actual dataset to the console.
3. **Write tests** such as sanity tests or consistency checks
4. **Format the output**

Time spent scaffolding your project pays dividends in reduced time spent debugging.

---

## `11.10` Exercises

### `Exercise 11.1`

> Write a function that reads the words in `words.txt` and stores them as keys in a dictionary. It doesn't matter what the values are. Then you can use the `in` operator as a fast way to check whether a string is in a dictionary.

```python
# exercises/11.1.py

fin = open('exercises/words.txt')

words = dict()

def words_to_dict(word_list):
    """
    takes a list of words
    creates a dictionary with each word as a key
    with a value of 0
    """
    for word in word_list:
        word = word.strip()
        words[word] = 0

words_to_dict(fin)

```

### `Exercise 11.2`

>Read the documentation of the dictionary method [`setdefault`](https://docs.python.org/3.7/library/stdtypes.html#dict.setdefault) and use it to write a more concise version of `invert_dict`

```python
# exercises/11.2.py

def invert_dict(d):
    """
    takes some dictionary d
    inverts each key-value pair such that the old
    value is the new key and the old key is the new value
    returns the inverted dictionary
    """

    inverse = dict()
    for key in d:
        inverse.setdefault(d[key], []).append(key)
    return inverse

```

### `Exercise 11.3`

> Memoize the Ackerman function from `exercise 6.2`

```python
# exercises/11.3.py

# cache computed values
cache = dict()

def ack(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m-1, 1)
    # check cache
    if (m, n) in cache:
        return cache[m, n]
    else:
        # cache value, then return it
        cache[m, n] = ack(m-1, ack(m, n-1))
        return cache[m, n]

```

### `Exercise 11.4`

> If you did exercise 10.7 you already have a function named `has_duplicates` that takes a list as a parameter and returns `True` if there is any object that appears more than once in the list.
>
> Use a dictionary to write a faster, simpler version of `has_duplicates`

```python
# exercises/11.4.py

def has_duplicates(t):
    """
    takes a list
    returns True if any elements are repeated
    """
    d = dict()
    for word in t:
        if word in d:
            return True
        d[word] = True
    return False

```

