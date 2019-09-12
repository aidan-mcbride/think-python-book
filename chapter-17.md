# 17: Classes and Methods

**Object-oriented programming** - A programming paradigm in which data and the operations that manipulate this data are organized into *classes* and *methods*.

**Methods** are functions that are associated with a particular class.

The **subject** of the *method* - the object the method is invoked  on - is the first parameter of the method, and is named **`self`** by convention.

```python
class Time:
    """Represents the time of day."""
    def print_time(self):
        """prints formatted time"""
        print("{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second))
    def time_to_int(self):
        """converts time to seconds as int"""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
# create instance of Time:
start_time = Time()

# call method:
start_time.print_time()
```

The **`__init__`** method is a special method that is invoked when an object is instantiated; One use for this is to set (default) values for attributes:

```python
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
```

```python
class Point:
    """represents a point in 2D space"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
```

The **`__str__`** method returns a string representation of an object. When you `print()` an object, python invokes the `__str__` method.

```python
class Point:
    #...
    def __str__(self):
        return "{}, {}".format(self.x, self.y)
```

[***<u>See here for more special methods</u>***](https://docs.python.org/3/reference/datamodel.html#specialnames)

## `17.8` Type-based dispatch

You can use the built-in function `isinstance(value, class)` to check if a given value is an instance of a given class.

**Type-based dispatch** is when you invoke a different method depending on the *type* of the argument:

```python
class Time:
    # ...
    # operator overloading for '+' operator
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        elif isinstance(other, int):
            return self.increment(other)
    # ...

```

**polymorphic** functions work with multiple *types*.

## `17.10` Debugging

While it is legal to add attributes to an object at any point, this can cause problems if you have two instances of the same Class with different attributes. To avoid this problem, you should initialize all of an object's attributes in the `__init__` method.

To check if an object has a given attribute, use `hasattr()`

**The function `vars(instance)` prints a dictionary of each of an object's attributes mapped to its value:**

```python
coords = Point(x=3, y=7)
vars(coords)
# returns:
# {'x': 3, 'y': 7}
```

The function `getattr(obj, attr)` takes an object and an attribute name and returns the attribute's value.



---

## *Exercises*

### `Exercise 17.1`

> Download the code from this chapter. Change the attributes of `Time` to be a single integer representing seconds since midnight. Then modify the methods (and the function `int_to_time`) to work with the new implementation.

```python
# see file:
# exercises/17.1.py
```

### `Exercise 17.2`

> Write a definition for a class named `Kangaroo` with the following methods:
>
> 1. An `__init__` method that initializes an attribute named `pouch_contents` to an empty list.
> 2. A method named `put_in_pouch` that takes an object of any type and adds it to `pouch_contents`
> 3. A `__str__` that returns a string representation of the Kangaroo object and the contents of the pouch.

```python
# exercises/17.2.py

class Kangaroo:
    def __init__(self, contents=list()):
        self.pouch_contents = contents

    def put_in_pouch(self, obj):
        """appends given obj to pouch_contents"""
        self.pouch_contents.append(obj)

    def __str__(self):
        s = "Kangaroo - pouch contents:"
        for obj in self.pouch_contents:
            s += object.__str__(obj)
        return s
    
```

> Test your code by creating two Kangaroo objects, assigning them to variables named `kanga` and `roo`, and then adding `roo` to the contents of `kanga`'s pouch.

```python
if __name__ == "__main__":
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch(roo)

    print(kanga)
    print(roo)

```

> Download [file], it contains a solution to the previous problem with one big, nasty bug. Find and fix the bug.

Default values for `__init__` methods get evaluated when the function is defined, not on each instantiation. Because of this, both kangaroos reference the *same list* for their pouch contents.

To fix this, set the default value for `pouch_contents` to None; Within the function itself, create a list if needed.

```diff
 class Kangaroo:
-    def __init__(self, contents=list()):
+    def __init__(self, contents=None):
+		 if contents == None:
+			 contents = list()
		 self.pouch_contents = contents

```

