# exercises/5.3.1.py

def is_triangle(a, b, c):
    check_a = bool(a <= b + c)
    check_b = bool(b <= a + c)
    check_c = bool(c <= a + b)

    if check_a and check_b and check_c:
        print("Yes")
    else:
        print("No")

is_triangle(3, 4, 5)
is_triangle(100, 1, 2)
is_triangle(2, 3, 5)
is_triangle(2, 3, 6)
