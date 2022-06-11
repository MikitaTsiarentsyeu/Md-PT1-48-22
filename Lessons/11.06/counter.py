def counter(n):
    def inner():
        nonlocal n
        n += 1
        return n
    return inner

f = counter(100)
h = counter(1)
print(f())
print(h())
print(f())
print(h())
print(f())
print(h())