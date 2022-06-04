def mult(a, b):
    if b < 0:
        b = -b
        a = -a
    res = 0
    for i in range(b):
        res += a
    return res

print(mult(2,3))
print(mult(3,2))
print(mult(0,3))
print(mult(2,0))
print(mult(-2,3))
print(mult(2,-3))
print(mult(-2,-3))
