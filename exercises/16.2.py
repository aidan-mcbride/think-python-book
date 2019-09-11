# exercises/16.2.py

import datetime
import copy

today = datetime.datetime.now()

def day_of_week():
    """
    returns the current day
    """
    global today
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[datetime.date.weekday(today)]

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

if __name__ == "__main__":
    print("Today is {}".format(day_of_week()))
    print('---')

    # user_birthday()
    # print('---')

    bd1 = datetime.datetime(1985, 5, 15)
    bd2 = datetime.datetime(1993, 11, 24)
    print(double_day(bd1, bd2))
    print((double_day(bd1, bd2) - bd1).days / (double_day(bd1, bd2) - bd2).days)
    print('---')
