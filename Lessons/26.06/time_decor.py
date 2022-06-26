from argparse import ArgumentError
import time

finish = 0

def time_measure(func):
    def wrapper(n):
        global finish
        finish = 0
        start = time.time()
        res = func(n)
        finish = time.time() - start
        return res
    return wrapper


def get_time_res():
    return finish