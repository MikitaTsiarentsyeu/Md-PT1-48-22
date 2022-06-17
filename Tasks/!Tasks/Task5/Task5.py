import functools
import timeit


# Task5_1
def nested_list(lst: list) -> int:
    return sum(nested_list(x) if isinstance(x, list) else x for x in lst)


# Task5.2 with lru_cache
def fib_1(x: int) -> list:
    @functools.lru_cache(maxsize=None)
    def inner(n: int) -> list:
        return inner(n - 1) + inner(n - 2) if n > 1 else n

    lst = [inner(i) for i in range(x)]
    return lst


##Task5.2 without lru_cache
def fib_2(x: int) -> list:
    def inner(n: int) -> list:
        return inner(n - 1) + inner(n - 2) if n > 1 else n

    lst = [inner(i) for i in range(x)]
    return lst


if __name__ == '__main__':
    # Task_5.1
    print(nested_list([1, 2, [2, 4, [[7, 8], 4, 6]]]))
    # Task_5.2
    print(*fib_1(5))
    print(*fib_1(10))

    # calculate total execution time
    result = timeit.timeit(stmt='fib_1(30)', globals=globals(), number=5)
    result2 = timeit.timeit(stmt='fib_2(30)', globals=globals(), number=5)

    print(f"Execution time fib_1 = {round(result / 5, 5)} seconds")
    print(f"Execution time fib_2 = {round(result2 / 5, 5)} seconds")
