def sum(l):
    total = 0
    for i in l:
        if not isinstance(i, list):
            total = total + i
        else:
            total = total + sum(i)
    return total

print(sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fib(n, first=0, second=1, list=[0]):
    if n <= 1:
        return list
    else:
        list.append(first+second)
        return fib(n-1,first+second, first, list)

print(fib(10))