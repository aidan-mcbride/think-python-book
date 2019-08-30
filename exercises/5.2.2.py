# exercises/5.2.2.py

# fancy it up a bit
print("CHECK FERMAT")
print("--------------------------------")

print("Input a value for a: ", end="")
a = int(input())
print("Input a value for b: ", end="")
b = int(input())
print("Input a value for c: ", end="")
c = int(input())
print("Input a value for n: ", end="")
n = int(input())

def check_fermat(a, b, c, n):
    if n > 2:
        if (a**n + b**n == c**n):
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work")
    else:
        print("No, that doesn't work")

print("")
print("checking if {} + {} == {}".format(a**n, b**n, c**n))
print("...")

check_fermat(a=a, b=b, c=c, n=n)
