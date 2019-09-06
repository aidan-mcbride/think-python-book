# case-study-3/13.5.py

import random

# from 11.2
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def choose_from_hist(hist):
    """
    takes a histogram
    returns a randomly selected key
    with probability based on value
    """
    p = list()
    for key, value in hist.items():
        for i in range(value):
            p.append(key)
    return random.choice(p)

t = ['a', 'a', 'b']
hist = histogram(t)

print(choose_from_hist(hist))
