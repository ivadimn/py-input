from typing import Callable, Any, Optional
import functools
from datetime import datetime


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print("Название метода: {}".format(func.__name__))
        print("Позиционные аргументы: {0}".format(args))
        #print("Именованные аргументы: {0}".format(**kwargs))
        print("Документация: {0}".format(func.__doc__))
        result = func(*args, **kwargs)
        return result
    return wrapper


def createtime(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print("Время создания класса: {0}".format(datetime.utcnow()))

        print("Методы класса {0}: {1}".format(cls.__name__, dir(cls)))
        return instance
    return wrapper


def for_all_methods(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        for func_name in dir(cls):
            if not func_name.startswith("__"):
                method = getattr(cls, func_name)
                decorate_method = decorator(method)
                setattr(cls, func_name, decorate_method)
        return cls
    return decorate


@createtime
@for_all_methods(logging)
class Functions:

    def __init__(self, max_number: int) -> None:
        self.__max_number = max_number

    def square_sum(self) -> int:
        """Вычисляет сумму квадратов чисел до заданного значения """
        number = 100
        result = 0
        for _ in range(number + 1):
            result = sum([i_num ** 2 for i_num in range(self.__max_number)])
        return result

    def cube_sum(self, number: int) -> int:
        """Вычисляет сумму кубов чисел до заданного значения """
        result = 0
        for _ in range(number + 1):
            result = sum([i_num ** 3 for i_num in range(self.__max_number)])
        return result


funcs = Functions(1000)
funcs.square_sum()
funcs.cube_sum(1000)