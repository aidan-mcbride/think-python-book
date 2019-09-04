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


d = dict(a=1,b=2,c=3,z=1)

print(d)
print(invert_dict(d))
