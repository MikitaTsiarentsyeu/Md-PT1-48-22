from functools import reduce

l = [1,2,3,4,5,6]

def iterate(l, f, i=0):
    if i == len(l):
        return
    f(l[i])
    return iterate(l, f, i+1)

iterate(l, print)

def print_sq(num):
    print(num*num)

iterate(l, print_sq)

# print_sq = lambda num: print(num*num)
iterate(l, lambda num: print(-num*num + 5))

sum = lambda x, y=0: x+y
# def sum(x, y=0): the same as
#     return x+y

test_str = "Abc Aac aaa ttt kkk"
print(sorted(test_str.split()))
print(sorted([x.lower() for x in test_str.split()]))
print(sorted(test_str.split(), key=lambda x: x.lower()))
#{"aac":"Aac", "abc":"Abc"}

d = {"one":1, "two":2, "three":3}
print(sorted(d))
print(sorted(d.items(), key=lambda kv: kv[0]))
print(sorted(d.items(), key=lambda kv: kv[1]))

l = [("one",1), ("two",2), ("three",3)]
print(sorted(l, key=lambda v: v[0]))
print(sorted(l, key=lambda v: v[1]))

def sum(x, y):
    return x+y
print(type(sum))
print(type(lambda x, y: x+y))

print((lambda x: lambda x: lambda x: lambda x: x)(3)(3)(3)(3)) # bad approach

print((lambda x: x*x)(10))

def outer(n):
    return lambda x: x**n

cube = outer(3)
print([cube(x) for x in range(10)])

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
map_obj = map(lambda x: x*x, l)
print(map_obj)

# for i in map(lambda x: x*x, range(100000000000000000000000)):
#     print(i)

# list(map(lambda x: x*x, range(100000000000000000000000))) will take too much time

print(list(map_obj))
print(list(map_obj))

for i in map_obj:
    print(i)

def to_chr(num):
    return chr(num+50)

print(list(map(to_chr, l)))

print(list(map(lambda num: chr(num+60), l)))

print(list(filter(lambda x: x > 4, l)))
print(list(filter(lambda x: 0, l)))
print(list(filter(lambda x: True, l)))

print(list(filter(lambda x: x // 10, l)))

print(list(map(lambda num: chr(num+60), filter(lambda x: x // 10, l))))

print(reduce(lambda x, y: x+y, [1,2,3,4,5]))
print(reduce(lambda x, y: x*y, [1,2,3,4,5]))
print(reduce(lambda x, y: x if x>y else y, [1,2,3,4,5]))

print(reduce(lambda x, y: f"{x}-{y}", [1,2,3,4,5]))
"1-2"
"1-2-3"
"1-2-3-4"
"1-2-3-4-5"


['1', '11', '12', '22', '2', '13', '30', '33'] 