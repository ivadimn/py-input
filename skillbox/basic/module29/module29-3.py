from typing import Callable, Any, Optional
import time

"""
def repeate(count: int = 1) -> Callable:
    def wrapper_func(func: Callable) -> Callable:
        def wrapper(*args, **kwarsg) -> Any:
            result = 0
            for i in range(count):
                result = func(*args, **kwarsg)
            return result
        return wrapper
    return wrapper_func


@repeate(count=3)
def func(text: str) -> None:
    print(text)

func("Text1")
func("Text2")
"""


def waiting(_func: Optional[Callable] = None, *, waiting_time: int = 1) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def surrogate_func(*args, **kwargs) -> Any:
            print("Ждём!")
            for _ in range(waiting_time):
                print("-", end = "")
                time.sleep(1)
            print("\nПоехали!!")
            result = func(*args, **kwargs)
            return result
        return surrogate_func
    if _func is None:
        return wrapper
    else:
        return wrapper(_func)

@waiting(waiting_time=4)
def do_work() -> None:
    print("Функция выполняется....")

do_work()