# exercises/11.3.py

# cache computed values
cache = dict()

def ack(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m-1, 1)
    # check cache
    if (m, n) in cache:
        return cache[m, n]
    else:
        # cache value, then return it
        cache[m, n] = ack(m-1, ack(m, n-1))
        return cache[m, n]

print(ack(3, 4))
print(ack(-1, 500)) # should break
print(ack(20, 50))  # RuntimeError: maximum recursion depth exceeded
