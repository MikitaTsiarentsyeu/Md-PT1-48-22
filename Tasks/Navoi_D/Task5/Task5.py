# recursive function for sum of all elements in list
def sum_list(lst):
    n = 0
    for i in lst:
        if (type(i) == list):
            n = n + sum_list(i)
        else:
            n = n + i
    return n
print(sum_list([1, 2, [2, 4, [[7, 8], 4, 6]]]))

# recursive function for n-th first fibonacci numbers
def fib(n):
    global x
    if n <=2:
        x = [0,1]
        return x
    x = fib(n-1)
    x.append(sum(x[:-3:-1])) 
    return  x

fib(10)
print(",".join(map(str,x)))

