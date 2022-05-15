l = [[1,2,3], [4,5,6], [7,8,9]]
print(l)
print(l[0][0], l[0][1], l[0][2])
print(l[1][0], l[1][1], l[1][2])
print(l[2][0], l[2][1], l[2][2])

t = (l, "test")
t[0][0][0] = 1.0
print(t)
print(l)

d = {t:1}
print(d)