# exercises/10.5.py

def is_sorted(t):
    """
    takes a list
    returns True if list is sorted in ascending order
    """
    s = t[:]    # create copy
    s.sort()    # sort copy
    return t == s   # compare original to sorted copy

print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))
