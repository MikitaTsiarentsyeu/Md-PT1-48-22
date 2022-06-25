'''
Write recirsion function for sum counting.
[1, 2, [2, 4, [[7, 8], 4, 6]]], Sum of elements - 34
'''
a = [1, 2, [2, 4, [[7, 8], 4, 6]]]

def unpuck_sum(a):
    summa = 0
    for i in a:
        if type(i) != list:
            summa += i
        else:
            summa = summa + unpuck_sum(i)
    return summa
print(unpuck_sum(a))
