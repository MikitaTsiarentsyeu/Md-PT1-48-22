# while True:
#     print("to infinity and beyond!")
#     print("!!!")


from itertools import count


x = 0

while x < 10:
    print(x)
    x += 1
else:
    print("hello from else")

print("the end")

l = [1,2,3,4,5,6,7,8,9,10]

for elem in l:
    print(f"the current value of iteration is {elem}")
    print(f"the square value of iteration is {elem**2}")

i = 0
while i < len(l):
    print(f"the current value of iteration is {l[i]}")
    print(f"the square value of iteration is {l[i]}")
    i += 1

i = 0
while i < len(l)-1:
    print(l[i]+l[i+1])
    i += 1

for elem in set("test string"):
    print(elem)

for elem in tuple(l):
    print(elem)

print("the end")

d = {"one": 1, "two": 2, "three": 3}
for i in d:
    print(i, d[i])

for i in d.items():
    print(i)

for k, v in d.items():
    print(k, v)

for i in d.values():
    print(i)

# for i in range(500000000, 100000000000, 2):
#     print(i)

for i in range(len(l)):
    print(l[i])

flag = True
for i in range(10):
    print(flag)
    flag = not flag

l = ["one", "two", "three"]
for i, e in enumerate(l):
    print(i, e)
    print(l[i])

s = set(l)
for i, e in enumerate(s):
    print(i, e)

d = {}
for i, e in enumerate(s):
    d[i] = e

print(d)

for i in range(5):
    print(i)

print(f"the value of i is {i}")

for i in range(5):
    print(i)
    i = 0
    print(i)

for i in range(5):
    for j in range(5):
        for k in range(5):
            print(f"i j k {i} {j} {k}")

l = [[1,2,3], [4,5,6], [7,8,9]]
for i in range(len(l)):
    print(f"{l[i]}:")
    for j in range(len(l[i])):
        print(l[i][j])

for i in l:
    for j in i:
        print(j)

print("---------")

l = [1,2,3,4,5,6,7,8,9]
for i, e in enumerate(l):
    print(e)
    l[i] = -e
    print(l.pop())
print(l)

# l = [0]
# for i in l:
#     l.append(0)
#     print(l)      infinity interation

for i in range(10):
    if i == 3:
        continue
    if i == 4:
        pass
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
else:
    print("hello from else")

l = [32,3456,2344,-3456,23456,34,6789]
for i in l:
    if i < 0:
        continue
    print(i**0.5)

counter = 0
while True:
    if counter > 9:
        break
    print(f"test value number {counter}")
    counter += 1

counter = 0
while counter <= 9:
    print(f"test value number {counter}")
    counter += 1

l = ['0', '4', '2', '7', '4', '55', '32', '23', '77', '567', '789']
counter = 0
while True:
    if len(l[counter]) > 1:
        break
    print(l[counter])
    counter += 1

counter = 0
for i in l:
    if len(i) < 2:
        continue
    if len(i) == 2:
        counter += 1
        print(i)
    if len(i) > 2:
        break

l = sorted(l)
print(l)
counter = 0
for i in l:
    if len(i) != 2:
        continue
    if len(i) == 2:
        counter += 1
        print(i)