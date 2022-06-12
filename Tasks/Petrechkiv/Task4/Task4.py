def check_str(string: str):
    not_empty_string = string.replace(' ', '').replace(',', '').replace('.', '').replace(':', '')
    up = sum([i.isupper() for i in not_empty_string])
    return f"{up} - upper case, {len(not_empty_string)-up} - lower case"
def is_prime(number: int):
    if number % 2 == 0:
        return False
    i = 3
    while i * i < number:
        if number % i == 0:
            return False
        i += 2
    return True
def is_prime2(number: int):   
    if number % 2 == 0:
        return False
    i = 3
    while i * i < number and number % i != 0:
        i += 2
    return i * i > number
def get_ranges(lt: list):
    integer = []
    for i in lt:
        if i == lt[-1]:
            integer.append(i)
            break
        elif i == lt[0] or integer[-1] == ', ':
            integer.append(i)
            if integer[-1] != lt[lt.index(i) + 1] - 1:
                integer.append(', ')
            else:
                integer.append('-')
        else:  
            if i != lt[lt.index(i) + 1] - 1:
                integer.append(i)
                integer.append(', ')
    return ''.join([str(elem) for elem in integer])
test_string = "A test string with the characters Top. and the Lower register he...llO, Mikita!"
print(check_str(test_string))
print(is_prime(777))
print(is_prime2(787))
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))