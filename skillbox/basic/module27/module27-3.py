from typing import Callable, Any
import time

"""
def do_twice(func : Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapped_func

@do_twice
def greeting(name):
    print('Привет, {name}!'.format(name=name))

greeting("Tom")
"""

def timer(func : Callable) -> Any:
    def wrapped_func(*args, **kwargs) -> int:
        start_at = time.time()
        result = func(*args)
        finish_at = time.time()
        print("Функция выполнялась {0} сек.".format(round(finish_at - start_at, 4)))
        return result
    return wrapped_func

@timer
def sum_cube(number : int) -> int:
    summa = 0
    for n in range(number):
        summa += sum([n ** 3 for n in range(number)])
    return summa

print(sum_cube(1000))
