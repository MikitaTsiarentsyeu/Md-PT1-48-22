
def lst_sum(l):
    total = 0
    for element in l:
        if (type(element) == type([])):
            total = total + lst_sum(element)
        else:
            total = total + element
    return total
print(lst_sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fib(n):
    if n<1:
        return[]
    if n == 1:
        return [0]
    if n == 2:
        return  [0, 1]
    else:
        lst = fib(n-1)
        lst.append(lst[n-3] + lst[n-2])
        return lst
print(fib(5))
print(fib(10))
