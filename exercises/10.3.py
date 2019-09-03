# exercises/10.3.py

def middle(t):
    """
    takes a list
    returns that list sans first and last element
    """
    return t[1:-1]

t = [1,2,3,4]
print(middle(t))
