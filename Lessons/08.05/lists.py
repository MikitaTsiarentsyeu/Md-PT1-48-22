l = []
print(type(l))

l = [1,2,3,4,5]
print(l)

l = [1, 'test', [[[[[[[]]]]]]]]
print(l)

l = list("test")
print(l)

print([1,2,3]+[4,5,6]+["test"])
print([0]*10)

print(not not [1])
print(len([1,2,3,4]))

l = [1,2,3,4,5,6,7,8,9,10]
print(l[5])
print(l[-1])
print(l[0:6])
print(l[0:6:2])
print(l[6:0:-2])
print(l[::-2])

l.append("11")
print(l)

l.extend([12.0, 13.0])
print(l)

l.insert(0, 'zero')
print(l)

print(l.pop())
print(l.pop())
print(l.pop())
print(l)

print(l.pop(0))
print(l)

l.extend([11,11,11])
l.remove(11)
l.remove(11)
l.remove(11)
print(l)

del l[0]
print(l)

del l[0:4]
print(l)

l.clear()
print(l)

del l
print(l)