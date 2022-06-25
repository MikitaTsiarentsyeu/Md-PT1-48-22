#Task 1
def check_str(string):

    upper_count = 0
    lower_count = 0
    lst = []
    for i in string:
        if i.isalpha():
            lst.append(i)
    try:
        if len(lst) == 0:
            10/0
        for i in lst:
            if i.isupper():
                upper_count += 1
            else:
                lower_count += 1
    except ZeroDivisionError:
        result = 'empty string entered'
    else:
        result = f'{upper_count} upper case, {lower_count} lower case'
    return result
print(check_str('The quick Brown Fox'))

#Task 2
def is_prime(n):
    result = 0
    if 0 < n < 4:
        result = True
    elif n > 0:
        for i in range( 2,n-1):
            if n % i == 0:
                result = False
                break
            else:
                result = True
    else:
        result = 'enter a value greater than 0'
    return result 
print(is_prime(787))      
print(is_prime(777))

#Task 3
def get_ranges(lst):
    result = f"{lst[0]}"
    count = 1
    for i in range(len(lst)):
        if count > len(lst) - 1:
            break
        if lst[count] == lst[-1]:
            if lst[count] - lst[count-1] == 1:
                result += f"-{lst[count]}"
            else:
                result += f", {lst[count]}"
        elif lst[count] - lst[i] == 1:
            if lst[count + 1] - lst[count] == 1:
                pass
            else:
                result += f"-{lst[count]}"
        else:
            result += f", {lst[count]}"
        count += 1
    return result
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))