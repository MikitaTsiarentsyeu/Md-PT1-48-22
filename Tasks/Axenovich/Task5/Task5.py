def sum_list(l:list) -> int:
    """Function return sum list consist of number and lists"""

    res = 0
    if str(l).isdigit():
        return res + l
    elif l == []:
        return 0
    res += sum_list(l.pop(0)) + sum_list(l)
    return res

print(sum_list([1, 2, [2, 4, [[7, 8], 4, 6]]]))

def fibonacci(n) -> str:
    """Function return string with Fibonacci number sequence to your number"""

    def fib_of_n(n:int):
        if n <= 1:
            return n
        else:
            return fib_of_n(n-1) + fib_of_n(n-2)
    return ', '.join([str(fib_of_n(i)) for i in range(n)])


print(fibonacci(5))
print(fibonacci(10))