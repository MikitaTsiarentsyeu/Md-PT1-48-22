def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a 
        a, b = b, a + b
print(list(fib(10))) 
print(list(fib(5)))