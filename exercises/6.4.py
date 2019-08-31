# exercises/6.4.py

def is_power(a, b):
    """
    return True if a is a power of b
    otherwise return false
    """
    if a % b == 0:
        # a^1 == a
        if a == b:
            return True
        else:
            return is_power(a/b, b)
    return False

print(is_power(64, 2))
print(is_power(1000, 10))
print(is_power(1001, 10))
