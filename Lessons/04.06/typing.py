def times(a, b):
    return a*b

print(times(2, 3))
print(times([2], 3))
print(times('[2]', 3))

def times_int(a:int, b:int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a*b

print(times_int('2', 3))

def eq(coll1, coll2):
    if len(coll1) != len(coll2):
        return False
    for i in coll1:
        if i not in coll2:
            return False
    # for i in coll2:
    #     if i not in coll1:
    #         return False
    return True

print(eq([1,2,3], (1,2,3)))
print(eq("123", ('1','2','3')))

def sum(a, b):
    return a+b

def sum(a, b, c):
    return a+b+c

# sum(2,3) error
sum(2,3,4)


def print(x):
    return x

print(4)
print("print is no longer here")