# The sum of the numbers in the list
F = [1, 2, [2, 4, [[7, 8], 4, 6]]]

def get_sum(lst):
    n = 0
    for i in lst:
        if type(i) == list:
            n = n + get_sum(i)
        else:
            n = n + i
    return n

print(get_sum(F))


# Fibonacci numbers
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input("Please enter a Fibonacci numbers:\n "))
fib_list = []
for i in range(n):
    fib_list.append(fib(i))
print(",".join([str(i) for i in fib_list]))
