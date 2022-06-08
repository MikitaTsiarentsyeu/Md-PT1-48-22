def check_str(string : str) -> str:
    """
        Return formated str with number of upper case and lower case 
        characters in given string.
        string - given str to count.
    """
    upper_case = 0
    lower_case = 0
    for ch in string:
        if ch.isupper():
            upper_case += 1
        elif ch.islower():
            lower_case += 1

    return f'{upper_case} upper case, {lower_case} lower case'

def is_prime(number: object) -> bool:
    """
        Check is sended number is prime.
        number - given number to function.
    """
    if number < 2:
        return False

    for n in range(2, number-1):
        if number % n == 0:
            return False
    return True


import typing
def get_generator_of_ranges(list_to_convert : list) -> typing.Generator:
    """
        Converts sorted list to generated pars of ranges.
        (range_start_number, range_end_number)
        list_to_convert - sorted list without repetitions.\n
        [0, 1, 2, 3, 4, 7, 8, 10] -> (0, 4), (7, 8), (10, 10)
    """
    swap_number = list_to_convert[0]
    swaped_from_indxex = 0

    for list_i, value in enumerate(list_to_convert[1:], 1):
        if value == (swap_number+1):
            swap_number = value
        else:
            yield list_to_convert[swaped_from_indxex], list_to_convert[list_i - 1]
            swaped_from_indxex = list_i
            swap_number = value

    yield list_to_convert[swaped_from_indxex], list_to_convert[len(list_to_convert) - 1]




def get_ranges(swap_list : list) -> str:
    swap_list = get_generator_of_ranges(swap_list)
    swap_str = ''

    for value_from, value_to in swap_list:
        if value_from == value_to:
            swap_str = f'{swap_str}, {value_from}'
        else:
            swap_str = f'{swap_str}, {value_from}-{value_to}'

    return swap_str[2:]
    
if __name__ == '__main__':
    print(check_str('The quick Brown Fox'))

    print(is_prime(787), True)
    print(is_prime(777), False)

    print([0, 1, 2, 3, 4, 7, 8, 10], ' | ', "0-4, 7-8, 10")
    print([4, 7, 10], ' | ', '4, 7, 10')
    print([2, 3, 8, 9], ' | ', '2-3, 8-9')
    