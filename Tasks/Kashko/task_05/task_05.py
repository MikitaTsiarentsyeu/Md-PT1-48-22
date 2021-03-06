from typing import Union


def recursive_sum(arr: list) -> Union[int, float]:
    """Function that returns the sum of all elements in a list of lists.

    Args:
        arr (list): list of lists.

    Returns:
        Union[int, float]: sum of all elements in a list of lists.
    """
    sum = 0
    for el in arr:
        if isinstance(el, list):
            sum += recursive_sum(el)
        else:
            sum += el
    return sum


def fib(n: int) -> list:
    """Returns a list of fibonacci numbers.

    Args:
        n (int): number of fibonacci numbers.

    Returns:
        list: list of fibonacci numbers.
    """
    cache = {0: 0, 1: 1}

    def inner(n: int) -> int:
        if n in cache:
            return cache[n]
        cache[n] = inner(n - 1) + inner(n - 2)
        return cache[n]

    inner(n - 1)
    return list(cache.values())
