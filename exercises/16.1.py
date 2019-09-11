# exercises/16.1.py

class Time:
    """
    Represents a tme of day

    attributes: hour, minute, second
    """

def print_time(time):
    """
    takes a Time object,
    prints a formatted string
    """
    print("{:02d}:{:02d}:{:02d}".format(time.hour, time.minute, time.second))


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
