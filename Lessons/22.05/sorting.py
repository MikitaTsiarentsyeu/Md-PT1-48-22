# l = [2,4,1,7,-45,0,3,5,7,7,4,5]

# print(sorted(l))
# print(l)

# l.sort()
# print(l)

l = [12,11,10,9,8,7,6,5,4,3,2,1]
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

l = [12,11,10,9,8,7,6,5,4,3,2,1]
# l = [2,4,1,7,-45,0,3,5,7,7,4,5]
counter = 0
print(l)
for i in range(len(l)):
    m = i
    for j in range(i, len(l)):
        if l[j] < l[m]:
            m = j
    # if m == i:
    #     continue
    l[i], l[m] = l[m], l[i]
    counter += 1

print(l)
print(counter)

