from typing import Callable, Any
import time

"""
def how_are_you(func  : Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        answer = input("Как дела? ")
        if answer.lower() == "хорошо":
            print("А у меня не очень!", end = " ")
        elif answer.lower() == "плохо":
            print("А у меня очень хорошо!", end=" ")
        else:
            print("Вот и я не знаю!", end=" ")
        print("Ладно, держи свою функцию.")
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@how_are_you
def do_work() -> None:
    print("Функция выполняется....")


do_work()


def waiting(waiting_time: int) -> Callable:
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
    return wrapper


@waiting(waiting_time=5)
def do_work() -> None:
    print("Функция выполняется....")

do_work()
"""
