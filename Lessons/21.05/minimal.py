l = [2,4,1,7,-45,0,3,5,7,7,4,5]

# min(l)
m = l[0]
for i in l:
    if i < m:
        m = i

m = 0
i = 0
while i < len(l):
    if l[m] > l[i]:
        m = i
    i += 1

print(m)