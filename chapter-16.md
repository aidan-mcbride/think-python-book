# 16: Classes and functions

**Pure functions** have no side-effects - they don't modify any of the objects passed to them, and they have no effect other than returning a value.

**Modifiers** are functions that change the object(s) they receive as arguments.

* Modifier functions often have a return value of `None`

You should, as a general rule, try to always use pure functions over modifiers.

[**Functional programming**](https://en.wikipedia.org/wiki/Functional_programming) - A style of programming that prefers *pure functions**(There's a lot more to functional programming, but this is the essence of it)*.

**Invariants** are conditions that should always be true.

* e.g. a time should always be comprised of positive integers - it can't be -3.5 o'clock.

* Testing for invariants within your code helps to reduce bugs.

* You can use an **`assert` statement** to do this, which raises an exception if  a given statement does not evaluate to `True`

  

---

## *Exercises*

>Write a function called `print_time` that takes a Time object and prints it in the form `hour:minute:second`.

```python
def print_time(time):
    """
    takes a Time object,
    prints a formatted string
    """
    print("{:02d}:{:02d}:{:02d}".format(time.hour, time.minute, time.second))
```

> Write a boolean function called `is_after` that takes two Time objects, `t1` and `t2`, and returns `True` if `t1` follows `t2` chronologically and `False` otherwise. Challenge: don't use an `if` statement.

```python
def is_after(t1, t2):
    """
    takes two Time objects
    returns `True` if `t1` is later than `t2`
    """
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)
```

> Write a correct version of increment that doesn't contain any loops

```python
def time_to_seconds(time):
    """
    takes a Time object
    returns that time converted to seconds
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def seconds_to_time(seconds):
    """
    takes an integer representing a time in seconds
    returns an instance of Time
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def increment(t1, seconds):
    seconds += time_to_seconds(t1)
    return seconds_to_time(seconds)
```

> Write a pure version of `increment` that creates and returns a new Time object rather than modifying the parameter

```python
# see above - it already does that.
```

### `Exercise 16.1`

> Write a function called `mul_time` that takes a Time object and a number and returns a new Time object that contains the product of the original Time and the number.
>
> Then use `mul_time` to write a function that takes a Time object that represents the finishing time in a race, and a number that represents the distance, and returns a Time object that represents the average pace(time per mile)

```python
# exercises/16.1.py

class Time:
    # ...
def print_time(time):
    # ...
def time_to_seconds(time):
    # ...
def seconds_to_time(seconds):
    # ...
def mult_time(t1, factor):
    """
    takes a Time instance and a number as factor
    returns a new Time instance that is the original
    multiplied by the giveb number
    """
    seconds = time_to_seconds(t1)
    return seconds_to_time(int(seconds * factor))

def race_time(finishing_time, miles):
    """
    finishing_time: Time instance
    miles: integer

    returns pace in time per mile: Time instance
    """
    return mult_time(finishing_time, 1 / miles)

if __name__ == "__main__":
    race = Time()
    race.hour = 1
    race.minute = 0
    race.second = 0

    pace = race_time(race, 4)
    print_time(race)
    print_time(pace)

```

### `Exercise 16.2`

1. > Use the `datetime` module to write a program that gets the current date and prints the day of the week.

   ```python
   def day_of_week():
       """
       returns the current day
       """
       days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
       today = datetime.date.today()
       return days[datetime.date.weekday(today)]
   ```

2. > Write a program that takes a birthday as input and prints the user's age and the number of days, hours, minutes, and seconds until their next birthday.

   ```python
   # exercises/16.2.py
   
   import datetime
   import copy
   
   today = datetime.datetime.now()
   
   def day_of_week():
       # ...
   
   def current_age(birthdate):
       """
       takes a birthdate as Datetime object
       returns an integer of the current age of that person.
       """
       global today
       delta = today - birthdate
       return delta.days // 365
   
   def delta_to_time(timedelta):
       """
       takes a Timedelta object
       returns a Tuple of the hours, minutes, and seconds
       """
       ts = timedelta.total_seconds() - timedelta.days * 86400
       hours, rem = divmod(ts, 3600)
       minutes, seconds = divmod(rem, 60)
       return (int(hours), int(minutes), int(seconds))
   
   def time_to_next_birthday(birthdate):
       """
       takes a birthdate as Datetime object
       returns a Timedelta object of the time between today and the next birthday
       """
       global today
       next_birthday = birthdate.replace(year=today.year)
       if today > next_birthday:
           next_birthday = next_birthday.replace(year=next_birthday.year+1)
       delta = next_birthday - today
       print()
       return delta
   
   def user_birthday():
       """
       prompts user for birthday info
       prints current age
       prints time to next birthday
       """
       print("Input your birthday:")
       print("Year:", end=" ")
       year = int(input())
       print("Month:", end=" ")
       month = int(input())
       print("Day:", end=" ")
       day = int(input())
       print('---')
       birthday = datetime.datetime(year, month, day)
       print("Current Age: {} Years Old".format(current_age(birthday)))
       print() # empty line
       next = time_to_next_birthday(birthday)
       days = next.days
       hours, minutes, seconds = delta_to_time(next)
       print("Time to next birthday:")
       print("{} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, seconds))
   
   
   
   if __name__ == "__main__":
       print("Today is {}".format(day_of_week()))
       print('---')
   
       user_birthday()
       print('---')
   
   ```

3. > For two people born on different days, there is a day when one is twice as old as the other. That's their Double Day. Write a program that takes two birth dates and computes their Double Day.

   ```python
   # exercises/16.2.py
   
   # ...
   
   def double_day(bd1, bd2):
       """
       Takes two birthday Datetime objects
       returns the 'double day' - where one birthday is double the other
       """
       # figure out which birthday comes first
       date1 = min(bd1, bd2)
       date2 = max(bd1, bd2)
       double_day = date2 + (date2 - date1)
       return double_day
   
   # ...
   
   ```