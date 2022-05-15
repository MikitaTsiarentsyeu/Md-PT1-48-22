s = {1,2,3,4,5,6}
print(type(s), s)

s = {1, "test", (3,3,3)}
print(s)

# s = {1, "test", [3,3,3]} error

s = {1, 1, "test", "test", (3,3,3), (3,3,3), (3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3), (3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3)}
print(s)

s = {}
print(type(s), s)

s = set()
print(type(s), s)

# s[0] error

s.add(45)
print(s)
s.update([1,2,3,4,5])
print(s)
s.update("test")
print(s)

s.discard(45)
print(s)
s.discard(45)
print(s)
s.discard(45)
print(s)

# if 45 in s:
# s.remove(45)

print(len(s))

print(s.pop())
print(s)
print(s.pop())
print(s)

s.clear()
print(s)

del s

l = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
l = list(set(l))
print(l)

l = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5] + list("aaabbbcccdddeeefffuuu")
print(l)
s = set(l)
print(s)
l = list(s)
print(l)

s = "test string"
s = set(s)
print(s)
s = list(s)
s = "".join(s)
print(s)

x = [1,3,2]
y = [1,2,3]
print(x == y)
print(set(x) == set(y))

x = {1,2,3,4,5}
y = {3,4,5,6,7}

print(x.intersection(y))
print(x.union(y))

print(set("test").intersection(set("set")))
print(set("test").union(set("set")))

print(set("test value").intersection(set("set")))
print(set("test value").union(set("set")))

