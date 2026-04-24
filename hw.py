from functools import reduce
import time


def operation(func, x: int, y: int) -> int:
    return func(x, y)


def my_map(func, my_list: list) -> list:
    return [func(x) for x in my_list]


def filter_even_numbers(numbers: list) -> list:
    return list(filter(lambda x: x % 2 != 0, numbers))
def recursive_factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)


def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Time:", time.time() - start)
        return result
    return wrapper


def compose(*funcs):
    def inner(x):
        for f in reversed(funcs):
            x = f(x)
        return x
    return inner
def partial(func, *args):
    return lambda *more: func(*args, *more)


def factorial_reduce(n: int) -> int:
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]

    return wrapper


def my_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer

    for x in it:
        value = func(value, x)

    return value


def sort_by_last_letter(words: list) -> list:
    return sorted(words, key=lambda w: w[-1])


def recursive_reverse(my_list: list) -> list:
    if not my_list:
        return []
    return [my_list[-1]] + recursive_reverse(my_list[:-1])


def find_max(numbers: list) -> int:
    return reduce(lambda a, b: a if a > b else b, numbers)


def remove_elements(my_list: list, element):
    return list(filter(lambda x: x != element, my_list))


def repeat(n: int):
    return lambda s: s * n


def recursive_sum(my_list: list) -> int:
    if not my_list:
        return 0
    return my_list[0] + recursive_sum(my_list[1:])


def add_two_lists(list1: list, list2: list) -> list:
    return list(map(lambda x, y: x + y, list1, list2))