# [1,2,3,4,5,5,6] - list

t = (1,2,3,4,5,6)
print(type(t), t)

t = ()
print(len(t))

# t = (1)
t = (1,)
print(type(t), t)

t = (1,2,3,4,5)+(6,7,8,9)
print(t)

n = 5
t = (0,)*n
print(t)

t = (1,2,3,4,5,6,7,8,9)
print(t[0], t[3])
# t[11] error

print(t[2:7:2])
print(t[6:0:-1])
print(t[::-1])
print(t[-1])

# t[0] = 56 error
# t.append(45) error

if 55 in t:
    print(t.index(55))

del t
# print(t) error

t = (1, "test", [1,2,3,4,5])
print(t[2])
t[2].append(6)
print(t)

d = {}
print(type(d))

d = {"one":1, 2:"tw0", 3.0: 3, (4,):"four"}
print(d)

print(d["one"], d[(4,)])
d[5] = 5
print(d)

d[5] = 5.0
print(d)

d = {"one":1, 2:"tw0", 3.0: 3, (4,):"four", "one":1.0}
print(d)

print("one" in d)
print("0ne" in d)

print("tw0" in d.values())
# print(d.values()[0])
print(list(d.values())[0])

print(d.keys())
print(d.items())
print(('one', 1.0) in d.items())

print(len(d))
# print(d["0ne"]) error
# d[[0]] = 0 error

print(d.get("one"))
print(d.get("0ne"))
print(d.get("0ne", "nothing was found"))

print(d.pop("one"))
print(d)

print(d.popitem())
print(d)
print(d.popitem())
print(d)

d["test"] = "test"
print(d)

print(d.popitem())
print(d)
print(d.popitem())
print(d)

print({"test":2}["test"])

d.clear()
print(d)

d = {"test":2}
del d["test"]
print(d)

del d

d = {2:[1,2,3,4,5]}