# exercises/6.2.py

def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))

print(ack(3, 4))
print(ack(-1, 500)) # should break
print(ack(20, 50))  # RuntimeError: maximum recursion depth exceeded
