from typing import Callable, Any, List
import time
import datetime
import random

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

def write_error_log(func_name: str, error: str) -> None:
    now = datetime.datetime.today()
    now_str = "{0}.{1}.{2} {3}:{4}".format(
        now.day if now.day > 9 else "".join(["0", str(now.day)]),
        now.month if now.month > 9 else "0".join(["0", str(now.month)]),
        now.year, now.hour, now.minute)
    with open("function_errors.log", "a") as f:
        f.write("{0}\tошибка в функции: {1} - {2}\n".format(now_str, func_name, error))



def logging(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        print("\nВыполняется функция: {0}".format(func.__name__))
        print("Документация: {0}".format(func.__doc__))
        try:
            result = func(*args, **kwargs)
            print("Функция: {0} выполнилась без ошибок".format(func.__name__))
            return result
        except Exception as ex:
            print("В функция: {0} возниклв ошибка".format(func.__name__))
            write_error_log(func.__name__, ex.args[0])
    return wrapped_func


@logging
def summa(lst: List[int]) -> int:
    """
    Функция возвращает сумму последовательности чисел"""
    summa = 0
    for n in lst:
        if n < 0:
            raise ValueError("В последовательности встретилось отрицательное число....")
        summa += n
    return summa


@logging
def f():
    """
    Функция возвращает результат деления 2-х случайныйх чисел"""
    x = random.randint(0, 10)
    y = random.randint(0, 5)
    if y == 0:
        raise ZeroDivisionError("Деление на 0")
    return x / y

summa([1, 2, 3, 4, 5, 6])
summa([1, -2, 3, 4, 5, 6])
f()
f()
f()

