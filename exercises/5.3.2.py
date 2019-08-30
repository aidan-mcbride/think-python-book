# exercises/5.3.2.py

print("side a: ", end="")
side_a = int(input())
print("side b: ", end="")
side_b = int(input())
print("side c: ", end="")
side_c = int(input())

def is_triangle(a, b, c):
    check_a = bool(a <= b + c)
    check_b = bool(b <= a + c)
    check_c = bool(c <= a + b)

    if check_a and check_b and check_c:
        print("Yes")
    else:
        print("No")

is_triangle(a=side_a, b=side_b, c=side_c)
