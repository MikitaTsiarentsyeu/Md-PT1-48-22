
def sum(nested_list):
    summ = 0
    for number in nested_list:
        if not isinstance(number, list):
            summ = summ + number
        else:
            summ = summ + sum(number)
    return summ

print(sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fib(numbers_values, first_value=0,second_value=1,list_fibonacci=[]):
    if numbers_values == 0:
        return list_fibonacci
    else:
        list_fibonacci.append(first_value)
        return fib(numbers_values-1,first_value+second_value, first_value, list_fibonacci)
        
print(fib(10)) 


