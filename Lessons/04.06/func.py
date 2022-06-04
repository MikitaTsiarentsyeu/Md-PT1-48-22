# test()

from typing import Any


def test():
    print("this is a test")

test()

def test_sum(x, y):
    print(id(x), id(y))
    return x + y

t = test_sum(3, 4)
print(t, test_sum(5,6))

a, b = 888888888, 9999999999
print(id(a), id(b))
test_sum(a, b)
print(a, b)

a, b = [8,8,8,8,8], [9,9,9,9,9,9]
print(id(a), id(b))
test_sum(a, b)
print(a, b)

l = [1,3,6,2,2,4,6,7]
l.sort()
sorted(l)

def test_print(x:object, y:Any, s:str, e:str) -> str:
    """The function makes a new string from the x and y with separator s and end e\n
    x - any object that will be placed first\n
    y - any object that will be placed after the separator\n
    s - separator\n
    e - end of the line
    """
    return f"{x}{s}{y}{e}"

print(test_print(2,3,',','.'))
print(test_print(2,3,2.5,3.5))

def my_test_func1():
    my_test_func2()
    print("hello from my_test_func1")

def my_test_func2():
    print("hello from my_test_func2")

my_test_func1()

sign = '+'
# if sign == '+':
#     def action(x, y):
#         return x+y
# elif sign == '*':
#     def action(x, y):
#         return x*y

def action(x, y, s):
    if s == '+':
        return x+y
    elif s == '*':
        return x*y

print(type(action(2,3,'-')))

def test_return_func(x, y):
    print(f"x:{x} y:{y}")
    x += 1
    y += 1
    return x, y

a = test_return_func(2, 3)
print(a)

