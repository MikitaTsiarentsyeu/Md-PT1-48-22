# Task1

result_elements = 0

def sum_elements(lst):

    for i in lst:
        if type(i) is list:
            sum_elements(i)
        else:
            global result_elements
            result_elements += i
    return result_elements

print(sum_elements([1, 2, [2, 4, [[7, 8], 4, 6]]]))


#Task 2

def fib(i, var = 0, var_i = 1, lst_var = []):
    if i == 0:
        return lst_var
    else:
        lst_var.append(var)
    return fib(i-1,var+var_i, var)

   
print(fib(5))
#print(fib(10))