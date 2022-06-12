from ast import arg


def func_test_two_args(x, y):
    print(f"x arg value - {x}\ny arg value - {y}")

func_test_two_args(2,4)
func_test_two_args(4,2)

def evaluate(arg1, arg2, arg3):
    return arg1+arg2*arg3
    
print(evaluate(2,3,4))
print(evaluate(arg1=3,arg2=2,arg3=4))
print(evaluate(arg3=3,arg1=3,arg2=2))
# print(evaluate(2,arg1=3,arg2=2)) error

def evaluate(arg1, arg2, arg3=0, arg4=6, arg5=5):
    print(arg1, arg2, arg3, arg4, arg5)
    return arg1+arg2*arg3

print(evaluate(2,3))
print(evaluate(2,3,4))
print(evaluate(arg2=2,arg1=3))

def make_pizza(ingridients, time=10, griding=True):
    for i in ingridients:
        print(f"adding {i}")
    if griding:
        print("griding cheese")
    print(f"baking for a {time} minutes")

make_pizza(["peperonni"])

print(1,2,3,4,5,6,7,8, sep=',', end='.\n')
print(1,2,3,4,5,6,7,8)

def sum(*args):
    print(args)
    res = 0
    for i in args:
        res += i
    return res

print(sum(1,2,3,4,5,6,7,8,9,10))
l = [1,2,3,4,5]
print(sum(*l))
# print(sum(l)) error

def evaluate(*args, sign='+'):
    print(args)
    print(sign)

evaluate(1,2,3,4,5,6,7,8,9,10)

def my_print(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end)

my_print(1,2,3,4,4,5, sep=',')

my_print(*"test str")

def my_print(args, sep=' ', end='\n'):
     print(*args, sep=sep, end=end)

my_print([1,2,3,4,5])

def sum(**kwargs):
    print(kwargs)
    res = 0
    for i in kwargs.values():
        res += i
    return res

d = {"one":1, "two": 2, "three":3}
print(sum(**d))

sum(one=1, two=2, three=3)

# def make_pizza(**kwargs): not very good concept
#     for i in kwargs["ingridients"]:
#         print(f"adding {i}")
#     if kwargs["griding"]:
#         print("griding cheese")
#     print(f"baking for a {kwargs['time']} minutes")
# make_pizza(ingridients=["peperonni"], time=10, griding=True)

def my_print(x=0, y=0, *args, test_arg:str="test value", **kwargs):
    print(*args, sep=kwargs['sep'], end=kwargs['end'])

my_print(1,2,3,4,5,6,7,8, sep=';', end='!')