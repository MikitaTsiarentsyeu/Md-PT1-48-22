l = [1,2,3,4,5,6]

def iterate(l, i=0):
    if i == len(l):
        return
    print(l[i])
    return iterate(l, i+1)

iterate(l)

l = [1,2,3,4,5,6,7,8]

x = 3

m = (len(l)-1)//2
if l[m] == x:
    print(f"we found it - {m}")
if l[m] > x:
    m = (0+m)//2
    if l[m] == x:
        print(f"we found it - {m}")
    if l[m] < x:
        m = (m+1+m+1)//2
        if l[m] == x:
            print(f"we found it - {m}")

def search(l, x, low=None, high=None):
    if high is None and low is None:
        low = 0
        high = len(l)-1
    if low > high:
        return -1

    m = (low+high)//2
    if l[m] == x:
        return m
    elif l[m] > x:
        return search(l, x, low, m-1)
    else:
        return search(l, x, m+1, high)

print(search(l, 2))