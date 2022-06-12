def level1():
    print("start of level1")
    level2()
    print("end of level1")

def level2():
    print("start of level2")
    level3()
    print("end of level2")

def level3():
    print("start of level3")
    level4()
    print("end of level3")

def level4():
    print("start of level4")
    print("end of level4")

level1()

def level(n=1):
    if n > 4:
        return
    print(f"start of level{n}")
    level(n+1)
    print(f"end of level{n}")

level()

def print_n_times(text, n):
    while True:
        if n == 0:
            break
        print(text)
        n -= 1

def print_n_times(text, n):
    if n == 0:
        return
    print(text)
    print_n_times(text, n-1)

print_n_times("I'm going!", 10)

# 5! = 1*2*3*4*5 = 5*4!= 5*4*3! = 5*4*3*2!

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(5))

n = 123456

1+2+3+4+5+6

def sum_of_nums(num):
    if num // 10 == 0:
        return num
    return sum_of_nums(num // 10) + num%10

sum_of_nums(123456)

def sum(n):
    n = str(n)
    if len(n) == 0:
        return 0
    return int(n[-1]) + sum(n[:-1])

n = 123456
print(sum(n))