#1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
#Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34


def sum_of_elem(x_list):
    sum=0
    for i in x_list:
        if isinstance(i, list):
            sum +=sum_of_elem(i)
        else:
            sum += i 
    return sum
print(sum_of_elem([1, 2, [2, 4, [[7, 8], 4, 6]]]))

#2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи.
#Примеры вызова: 
#fib(5) -> 0,1,1,2,3
#fib(10) -> 0,1,1,2,3,5,8,13,21,34

def fibonaci(n):
    if n ==1:
        return [0]
    if n ==2:
        return [0,1]
    l=fibonaci(n-1)    
    l.append(l[-1]+l[-2])
    return l
print(fibonaci(10))
