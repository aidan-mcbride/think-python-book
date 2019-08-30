# exercises/5.2.1.py

def check_fermat(a, b, c, n):
    if n > 2:
        if (a**n + b**n == c**n):
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work")
    else:
        print("No, that doesn't work")


check_fermat(1, 2, 3, 4)
