from typing import Callable, Any
import time
"""
def func_2(func: Callable, *args) -> Any:
    return func(*args) * func(*args)


def func_1(x: int) -> int:
    return x + 10

print(func_2(func_1, 9))
"""

def timer(func : Callable, *args) -> Any:
    start_at = time.time()
    result = func(*args)
    finish_at = time.time()
    print("Функция выполнялась {0} сек.".format(round(finish_at - start_at, 4)))
    return result


def sum_cube(number : int) -> int:
    summa = 0
    for n in range(number):
        summa += sum([n ** 3 for n in range(number)])
    return summa


r = timer(sum_cube, 10_000)
print(r)
