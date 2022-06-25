def sum_elements(l):
    sum = 0
    for i in l:
        if type(i) is list:
            sum += sum_elements(i)
        else:
            sum += i
    return sum

print(sum_elements([1, 2, [2, 4, [[7, 8], 4, 6]]]))



def fib(n, first=0, second=1, work_list=[0]):
    if n <= 1:
        return work_list
    else:
        work_list.append(first+second)
        return fib(n-1,first+second, first, work_list)

print(fib(10))