# exercises/10.4.py

def chop(t):
    """
    takes a list
    removes the first and last element of that list
    returns None
    """
    t.pop(0)
    t.pop(len(t)-1)

t = [1,2,3,4]
print(chop(t))
print(t)
