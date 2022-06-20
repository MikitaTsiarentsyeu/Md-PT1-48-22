'''
Write recurcion fucntion for counting the n first Fibonacci`s numbers.
Examples:
fib(5) -> 0,1,1,2,3
fib(10) -> 0,1,1,2,3,5,8,13,21,34
'''

def fib_sum(n):
        if n==1:
            return 0
        if n == 2:
            return 1
        return fib_sum(n-1) + fib_sum(n-2)
 
def listing(n):
    fibo = []   
    for i in range(1, n+1): 
        fibo.append(fib_sum(i))
    return fibo  

print(listing(10))

#Not my variant, but looks very cool.
def fib(n):
    if n == 2:
        return [0,1]
    x = fib(n-1)
    x.append(x[-1] + x[-2])
    return x

print(fib(5))
