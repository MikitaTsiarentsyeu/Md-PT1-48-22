from math import sqrt
import re


def check_str(s: str) -> str:
    """Return string with a number of uppercase and lowercase charachters.

    Args:
        s (str): original string.

    Returns:
        str: result string.
    """
    s = s.replace(' ', '')
    counter = 0
    for ch in s:
        if ch.isupper():
            counter += 1
    result = f'{counter} upper case, {len(s) - counter} lower case'
    return result


def is_prime(n: int) -> bool:
    """Return True if the number is prime, False otherwise.

    Args:
        n (int): number.

    Returns:
        bool: True or False.
    """
    if any((n < 2, n > 2 and n % 2 == 0, n > 3 and n % 3 == 0)):
        return False
    limit = round(sqrt(n) + 1)
    divs = [*range(5, limit, 6), *range(7, limit, 6)]
    for i in divs:
        if n % i == 0:
            return False
    return True


def is_prime_worst_practice(n: int) -> bool:
    """Return True if the number is prime, False otherwise.

    Args:
        n (int): number.

    Returns:
        bool: True or False.
    """
    pattern = re.compile(r'^1?$|^(11+?)\1+$')
    s = '1' * n
    if not re.match(pattern, s):
        return True
    return False


def get_ranges(numbers: list) -> str:
    """Return string with ranges.

    Args:
        numbers (list): list of numbers.

    Returns:
        str: result string.
    """
    result = []
    begin = end = numbers[0]

    for n in numbers[1:] + [""]:
        if n != end + 1:
            if end == begin:
                result.append(str(begin))
            else:
                result.append(str(begin) + "-" + str(end))
            begin = n
        end = n

    return ", ".join(result)
