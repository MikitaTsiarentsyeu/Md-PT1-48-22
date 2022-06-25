# 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34

def sum(nested_list):
    summ = 0
    for number in nested_list:
        if not isinstance(number, list):
            summ = summ + number
        else:
            summ = summ + sum(number)
    return summ

print(sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))

# 2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34

def fib(numbers_values, first_value=0,second_value=1,list_fibonacci=[]):
    if numbers_values == 0:
        return list_fibonacci
    else:
        list_fibonacci.append(first_value)
        return fib(numbers_values-1,first_value+second_value, first_value, list_fibonacci)
        
print(fib(10)) 