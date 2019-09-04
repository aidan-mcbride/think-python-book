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
