#1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
#Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34

def sum_element(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total + sum_element(element)
        else:
            total = total + element
    return total
print(f"Сумма элементов равна: {sum_element([1, 2, [2, 4, [[7, 8], 4, 6]]])}")


#2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи.
#Примеры вызова: 
#fib(5) -> 0,1,1,2,3
#fib(10) -> 0,1,1,2,3,5,8,13,21,34

def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    x = fib(n-1)
    x.append(x[-1] + x[-2])
    return x
print(f"Числа Фибоначчи: {fib(5)}")
print(f"Числа Фибоначчи: {fib(10)}")