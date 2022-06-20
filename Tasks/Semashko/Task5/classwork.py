# Clouser
def counter(n):
    def inner():
        nonlocal n
        n += 1
        return n
    return inner

a = counter(1529)
b = counter(333)
print(a())
print(a())
print(a())

print(b())
print(b())
print(b())

# Recurcion  sum = 1+2+3+4+5+6
n = 123456
def rec(n):
    if n // 10 == 0:
        return n
    return rec(n // 10) + n % 10
print(rec(n))

n = 123456
def rec(n):
    n = str(n)
    if len(n) == 0:
        return 0
    return int(n[-1]) + rec(n[0:-1])

print(rec(n))