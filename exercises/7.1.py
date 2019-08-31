# exercises/7.1.py

import math

def mysqrt(a):
    x = a/2
    while True:
        y = (x + a/x) / 2
        if y == x:
            return y
        x = y

def test_square_root():
    # header row
    print("a", end="\t")
    print("mysqrt(a)", end="\t")
    print("math.sqrt(a)", end="\t")
    print("diff")
    # divider row
    print("-", end="\t")
    print("---------", end="\t")
    print("------------", end="\t")
    print("----")
    # results rows
    for i in range(9):
        # range is 0 index:
        # convert to 1-index floating point
        a = float(i+1)
        print(a, end="\t")
        print(mysqrt(a), end="\t")
        print(math.sqrt(a), end="\t")
        print(math.fabs(mysqrt(a) - math.sqrt(a)))

test_square_root()
