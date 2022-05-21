l = [2,4,1,7,-45,0,3,5,7,7,4,5]

# print(sorted(l))
# print(l)

# l.sort()
# print(l)

print(l)

counter = 0
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            counter += 1
            print(l)

print(l)
print(counter)