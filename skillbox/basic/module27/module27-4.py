from typing import Callable, Any
import time
"""
def timer(func : Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> int:
        start_at = time.time()
        result = func(*args)
        finish_at = time.time()
        print("Функция выполнялась {0} сек.".format(round(finish_at - start_at, 4)))
        print("-" * 50)
        return result
    return wrapped_func


def logging(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        print("\nВыполняется функция: {name}\t"
              "Позиционные аргумениы: {args}\t"
              "Именованные аргументы: {kwargs}".format(
            name = func.__name__, args = args, kwargs = kwargs
        ))
        result = func(*args, **kwargs)
        print("Функция {name} завершила работу".format(name = func.__name__))
        print("-" * 50)
        return result
    return wrapped_func

def bakery(func : Callable) -> Any:
    def wrapped_func(*args, **kwarhs) -> Any:
        print("</----------\>")
        result = func(*args, **kwarhs)
        print("<\______/>")
        return result
    return wrapped_func


def show(func : Callable) -> Any:
    def wrapped_func(*args, **kwarhs) -> Any:
        result = func(*args, **kwarhs)
        return result
    return wrapped_func

@logging
@timer
def sum_cube(number : int) -> int:
    summa = 0
    for n in range(number):
        summa += sum([n ** 3 for n in range(number)])
    return summa

@bakery
@show
def sandwich(*args) -> Any:
    for arg in args:
        print(arg)

#print(sum_cube(1000))
sandwich("помидоры", "сыр", "мясо")
"""

PLUGINS = dict()


def register(func : Callable) -> Callable:
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name : str) -> None:
    print("Hello {name}".format(name = name))

@register
def say_goodby(name : str) -> None:
    print("Goodbyu {name}".format(name = name))


print(PLUGINS)
say_hello("Tom")
