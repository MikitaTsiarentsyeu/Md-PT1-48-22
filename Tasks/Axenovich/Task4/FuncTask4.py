import re

def check_str_v1(string: str="The quick Brown Fox") -> str:
    """Give me string and I return amount lower and amount upper letters\n
    (I use islower and isupper function)"""
    lowerCase = 0
    upperCase = 0
    for i in string:
        if not i.isalpha():
            continue
        elif i.islower():
            lowerCase += 1
        elif i.isupper():
            upperCase += 1
    return f'{upperCase} upper case, {lowerCase} lower case'


def check_str_v2(string: str="The quick Brown Fox") -> str:
    """Give me string and I return amount lower and amount upper letters\n
    (I use regular expressions)"""
    lowerCase = len(re.findall('[a-zа-яё]{1}', string))
    upperCase = len(re.findall('[A-ZА-ЯЁ]{1}', string))
    return f'{upperCase} upper case, {lowerCase} lower case'


def is_prime(number: int) -> bool:
    """Give me number and I return is it a prime number or not"""
    for num in range(2, int(number**0.5) + 1):
        if number % num == 0:
                return False
        return True


def get_ranges(array: list) -> str:
    """Give me sort list without dublipicate number, and I return string with collapsed list"""
    result = []
    for i in array:
        interval = i - result[-1][-1] if result else 1 
        # create variable interval, if result empty, interval 1, else get interval between elements i and last in result

        if result and interval == 1:
            result[-1].append(i)
        elif interval:
            result.append([i])
    return ', '.join([str(i[0]) if len(i) == 1 else f'{i[0]}-{i[-1]}' for i in result]) # difficult to understand, but workable