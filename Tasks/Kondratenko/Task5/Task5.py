def recursion_sum_list(lst: list):
    total = 0
    for i in lst:
        if type(i) is list:
            total += recursion_sum_list(i)
        else:
            total += i
    return total


# implementation through a loop (more for myself)
def fibo_from_cycle(n):
    lst = [0, 1]
    if n == 0:
        return 0
    for i in range(n - 2):
        lst.append(lst[i] + lst[i + 1])
    return lst


def fibo(n):
    if n in fibo_line:
        return fibo_line[n]
    fibo_line[n] = fibo(n - 1) + fibo(n - 2)

    return fibo_line[n]


# Task5/1
print(f"The sum of all elements of the list - {recursion_sum_list([1, 2, [2, 4, [[7, 8], 4, 6]]])}")
print()
# Task5/2 - implementation through a loop
print(*fibo_from_cycle(5), sep=",")
print(*fibo_from_cycle(10), sep=",")
print()
# Task5/2 - implementation through a recursion
fibo_line = {1: 0, 2: 1}  # Two start elements of the fibo line
fibo(5)
print(*fibo_line.values(), sep=",")
fibo(10)
print(*fibo_line.values(), sep=",")
