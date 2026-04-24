from functools import reduce


def memoized_fibonacci(n: int) -> int:
    cache = {0: 0, 1: 1}

    def fib(x):
        if x in cache:
            return cache[x]
        cache[x] = fib(x - 1) + fib(x - 2)
        return cache[x]

    return fib(n)


def curry(func, *args):
    return lambda *more: func(*args, *more)


def my_zip(*iterables):
    min_len = min(len(i) for i in iterables)
    return ((tuple(i[j] for i in iterables)) for j in range(min_len))


def caching_decorator(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]

    return wrapper


def recursive_flatten(input_list: list) -> list:
    result = []
    for item in input_list:
        if isinstance(item, list):
            result.extend(recursive_flatten(item))
        else:
            result.append(item)
    return result


def check_args(*arg_types):
    def decorator(func):
        def wrapper(*args):
            for a, t in zip(args, arg_types):
                if not isinstance(a, t):
                    raise TypeError("wrong type")
            return func(*args)
        return wrapper
    return decorator