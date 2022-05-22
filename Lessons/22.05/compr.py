import math

l = [12,11,10,9,8,7,6,5,4,3,2,1]
s = {1,2,3,4}
d = {"one":1, "two":2, "three":3}

print([x*10 for x in s])

print({str(x) for x in l})
print([x for x in d])
print([x for x in d.items()])
print([f"{k}:{v}" for k, v in d.items()])

print([x for x in range(10)])
# print(list(range(10)))
# l = []
# for x in range(10):
#     l.append(x)
# print(l)

print([math.sin(math.pi*x**3) for x in range(20)])

print([x**2 for x in range(15) if x%2 == 0])

print([x**2 for x in range(15) if x%2 == 0 if x == 2 or x == 4])
print([x**2 for x in range(15) if x%2 == 0 and (x == 2 or x == 4)])

print([f"{x}-{y}" for x in range(10) for y in range(10)])
# for x in range(10):
#     for y in range(10):
#         print(f"{x}-{y}")

l = [[1,2,3], [4,5,6], [7,8,9]]
print([y for x in l for y in x])

print({x:str(x) for x in range(10)})

print({x:x**3 for x in range(10)})

print({y:x for x in range(1,4) for y in d.keys()}) # not optimal
test_dict = {}
for x in range(1,4):
    for y in d.keys():
        test_dict[y]=x
        print("operation happened")
