# 10: Lists

A **list** is a sequence of *values*, known as **elements** or **items**. List items can be of any *type*.

Lists can be created by enclosing its elements in **`[]`** :

```python
integers = [1, 2, 5]
strings = ['one', 'two', 'five']
```

Lists can contain a mix of types:

```python
mix = [1, 2.0, 'five']
mix[0]		# 1
mix[1]		# 2.0
```

Lists can contain other lists:

```python
battleship = [['G', 4], ['A', 6]]
battleship[0]		# ['G', 4]
battleship[0][0]	# 'G'
```

Empty lists can be declared with an empty set of square brackets:

```python
empty_list = []
```

Elements of a list can be accessed by index, same as string characters.

Unlike Strings, lists are ***mutable*** -  the elements of a list can be changed:

```python
integers = [1,2,3]
print(integers[2])		# 3
integers[2] = 5
print(integers[2])		# 5
```

Lists can be *traversed* with a `for` loop:

```python
integers = [1, 2, 5]
for integer in integers:
    print(integer * 10)
    
# 10
# 20
# 50
```

A list can be iteratively updated using a combination of `len()` and `range()`:

```python
integers = [1, 2, 5]
for i in range(len(integers)):
    integers[i] *= 10
    
integers	# [10, 20, 50]
```

List operations are the same as string operations

* **`+`** concatenates lists:

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)		# [1, 2, 3, 4, 5, 6]
```

* **`*`** repeats a given list, but as one list:

```python
['X'] * 4		# ['X', 'X', 'X', 'X']
```

## [`10.6` List methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

```python
list = list()	# alternate way to create an empty list
list.append()	# add a new element to end of list
list.pop(index)	# remove element from list at index
list.extend()	# add all elements of a list to another
list.sort()		# sort elements of a list

sum(list)		# returns the sum of all list elements

# create a list where each element is a word in a string.
string = str('red blue')
string.split()	# ['red', 'blue']
```

* **Accumulator** - a variable used to total some elements
* **Reduce** - an operation that reduces several values into one value.
* **Map** - applies some function to each element in a sequence.
* **Filter** - return a subset of a list

Most list operations are some form of *map*, *reduce*, or *filter* operation.

## `10.10` Objects and Values

```python
a = 'apples'
b = 'apples'

# to check if `a` and `b` refer to the same object
# or are two different objects with the same value:
a is b		# True

a = [1, 2, 3]
b = [1, 2, 3]
a is b		# False
```

In the second example, `a` and `b` are **equivalent** but not **identical**.

An **object** *has* a **value**.

## `10.11` Aliasing

```python
a = [1, 2, 5]
b = a
b is a		# True
```

**Reference** - a *variable* associated with an *object*. In the above example, both `a` and `b` are references to the same object.

An object with more than one reference is **aliased**.

An aliased object is *mutable* by either name:

```python
f = [1, 2, 2]
g = f		# g is an alias for f
g[2] = 5	# will also change f
print(f)	# [1, 2, 5]
```

## `10.12` List Arguments

Know when you are modifying a list vs. creating a new list

*Slicing* creates a new list:

```python
a = [1, 2, 3]
b = a[:]		# create slice of entire list
b[0] = 6
b	# [6, 2, 3]
a	# [1, 2, 3]	# Unchanged
```

## `10.13` Debugging

1. Many list methods have a return value of `None`:

    ```python
    list = list.sort()
    list	# None
    ```

2. There are many ways to do the same thing when it comes to lists:

  ```python
   list.append(x)
   list = list + [x]
   list += [x]
  ```

   For easier debugging, pick one way and stick with it.

3. Make copies of lists to avoid *aliasing*

  ```python
  list = [5, 3, 100]
  copy = list[:]
  copy.sort()
  list	# [5, 3, 100]
  copy	# [3, 5, 100]
  ```

---

## *`10.15` Exercises*

### `Exercise 10.1`

> Write a function called `nested_sum` that takes a list of lists of integers and adds up the elements from all of the nested lists, e.g.
>
> ```python
> t = [[1, 2], [3], [4, 5, 6]]
> nested_sum(t)	# 21
> ```

```python
# exercises/10.1.py

# imagine how clean this would be if `sum` and `list` weren't reserved keywords

def nested_sum(int_list):
    """
    takes a list of lists of integers
    returns the sum of all integers in all lists
    """
    total = 0
    for sub_list in int_list:
        total += sum(sub_list)
    return total

```

### `Exercise 10.2`

> Write a function called `cumsum` that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i+1 elements from the original list, e.g.
>
> ```python
> t = [1, 2, 3]
> cumsum(t)	# [1, 3, 6]
> ```

```python
# exercise/10.2.py

def cumsum(int_list):
    """
    takes a list of integers
    returns a list of integers that is the cumulative sum of the previous integers
    """
    new_list = []
    cum_sum = 0
    for num in int_list:
        cum_sum += num
        new_list.append(cum_sum)
    return new_list

```

### `Exercise 10.3`

> Write a function called `middle` that takes a list and returns a new list that contains all but the first and last elements, e.g.
>
> ```python
> t = [1, 2, 3, 4]
> middle(t)	# [2, 3]
> ```

```python
# exercises/10.3.py

def middle(t):
    """
    takes a list
    returns that list sans first and last element
    """
    return t[1:-1]

```

### `Exercise 10.4`

> Write a function called `chop` that takes a list, modifies it by removing the first and last elements, and returns `None`, e.g.
>
> ```python
> t = [1, 2, 3, 4]
> chop(t)		# None
> t			# [2, 3]
> ```

```python
# exercises/10.4.py

def chop(t):
    """
    takes a list
    removes the first and last element of that list
    returns None
    """
    t.pop(0)
    t.pop(len(t)-1)

```

### `Exercise 10.5`

> Write a function called `is_sorted` that takes a list as a parameter and returns `True` if the list is sorted in ascending order and `False` otherwise, e.g.
>
> ```python
> is_sorted([1,2,2])		# True
> is_sorted(['b', 'a'])	# False
> ```

```python
# exercises/10.5.py

def is_sorted(t):
    """
    takes a list
    returns True if list is sorted in ascending order
    """
    s = t[:]    # create copy
    s.sort()    # sort copy
    return t == s   # compare original to sorted copy

```

### `Exercise 10.6`

> Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called `is_anagram` that takes two strings and returns True if they are anagrams.

```python
# exercises/10.6.py

def is_anagram(s1, s2):
    """
    takes two strings
    returns True if s1 is an anagram of s2
    """
    s1 = list(s1.replace(' ', ''))
    s2 = list(s2.replace(' ', ''))
    s1.sort()
    s2.sort()
    return s1 == s2

```

### `Exercise 10.7`

> Write a function called `has_duplicates` that takes a list and returns `True` if there are any elements that appear more than once. It should not modify the original list.

```python
# exercises/10.7.py

def has_duplicates(t):
    """
    takes a list
    returns True if any elements are repeated
    """
    for i in t:
        if t.count(i) > 1:
            return True
    return False

```

