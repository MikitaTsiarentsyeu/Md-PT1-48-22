while True: 
    n=input('Enter the number of Fibonacci numbers you are looking for ')
    if n.isdigit():
        if int(n) > 0:
            n=int(n)
            break
        else:
            print('Value must be over 0. Try again!')
    else:
        print("Input Error!!Please, enter a numeric value!")
def fib(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    if n >= 2:
        fib_1 = fib(n-1)
        fib_1.append(fib_1[-1] + fib_1[-2])
        return fib_1
print(fib(n))

l=[1, 2, [2, 4, [[7, 8], 4, 6]]]
def sum_element(l):
    if type(l) is int:
        return l
    else:
        sum = 0
        for i in l:
            sum += sum_element(i)               
        return sum
print(f'The sum of the elements is', sum_element(l))
