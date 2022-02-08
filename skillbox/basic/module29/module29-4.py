from typing import Callable, Any, Optional
import functools
from datetime import datetime


def createtime(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print("Время создания класса: {0}".format(datetime.utcnow()))
        return instance
    return wrapper


@createtime
class Functions:

    def __init__(self, max_number: int) -> None:
        self.__max_number = max_number

    def square_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result = sum([i_num ** 2 for i_num in range(self.__max_number)])
        return result

    def cube_sum(self, number: int) -> int:
        result = 0
        for _ in range(number + 1):
            result = sum([i_num ** 3 for i_num in range(self.__max_number)])
        return result

funcs = Functions(1000)