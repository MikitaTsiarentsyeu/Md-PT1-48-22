from itertools import groupby


def check_str(st: str) -> str:
    big = len([letter for letter in st if letter.isupper()])
    low = len([letter for letter in st if letter.islower()])
    return f'{big} upper case, {low} lower case'


def is_prime(n: int) -> bool:
    for i in range(2, int(n ** .5 + 1)):
        if n % i == 0: return False
    return True


def get_ranges(x: list) -> str:
    """
    First You create a list with groupby function from itertools module and specified parameters
    first parameter is enumerate function, it's creating a tuple consist of an index and a value,
    second parameter is unnamed function lambda it returns the index and the value calculation results.
    for example:
    We have a list [34, 35, 36, 37, 38, 41, 42, 50] and we get a result:
                                first: 0 - second: 34 = -34
                                first: 1 - second: 35 = -34
                                first: 2 - second: 36 = -34
                                first: 3 - second: 37 = -34
                                first: 4 - second: 38 = -34
                                first: 5 - second: 41 = -36
                                first: 6 - second: 42 = -36
                                first: 7 - second: 50 = -43
    In other words, we get same results if the number is consecutive
    After that, the formatted result is returned
    """
    sequence_list = []
    for _, g in groupby(enumerate(x), lambda x: x[0] - x[1]):
        sequence_list.append([x for i, x in g])
    result = []
    for sequence in sequence_list:
        if len(sequence) > 1:
            result.append(f'{sequence[0]}-{sequence[-1]}')
        else:
            [result.append(str(ss)) for ss in sequence]
    return ', '.join(result)


if __name__ == '__main__':
    # print(check_str(input('Enter a string to count the number of lowercase and uppercase letters: ')))
    print(check_str('The quick Brown Fox'))
    # print(is_prime(int(input('Enter an integer to check if it is prime or not: '))))
    print(is_prime(787))
    print(is_prime(777))
    # userLst = list(map(int, input('To get a range extraction list, you need to enter integers with a space between: ')))
    # print(get_ranges(userLst))
    print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
    print(get_ranges([4, 7, 10]))
    print(get_ranges([2, 3, 8, 9]))
