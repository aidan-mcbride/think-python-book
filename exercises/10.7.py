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

print(has_duplicates([1, 2, 3, 4, 5]))
print(has_duplicates([1, 2, 3, 3, 5]))
