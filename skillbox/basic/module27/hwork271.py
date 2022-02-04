from typing import Callable, Any

"""
def args_values(*args) -> str:
    values = []
    for arg in args:
        if isinstance(arg, str):
            values.append("'{0}'".format(arg))
        else:
            values.append("{0}".format(arg))
    return ", ".join(values)


def kwargs_values(**kwargs) -> str:
    values = []
    for k, v in kwargs.items():
        if isinstance(v, str):
            values.append("{0}='{1}'".format(k, v))
        else:
            values.append("{0}={1}".format(k, v))
    return ", ".join(values)


def debug(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        args_info = []
        if len(args) > 0:
            args_info.append(args_values(*args))
        if len(kwargs) > 0:
            args_info.append(kwargs_values(**kwargs))
        print("\nВызывается {0}({1})".format(func.__name__, ", ".join(args_info)))
        result = func(*args, **kwargs)
        print("'{0}' вернула значение '{1}'".format(func.__name__, result))
        return result
    return wrapped_func

@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


print(greeting("Том"))
print(greeting("Миша", age=100))
print(greeting(name="Катя", age=16))
"""


def counter(acc: list) -> Callable:
    def wrapper_func(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            acc.append(1)
            print("Функция вызвана {0}-й раз".format(len(acc)))
            result = func(*args, **kwargs)
            return result
        return wrapper
    return wrapper_func


@counter(acc = [])
def do_work():
    print("Doing ....")

for _ in range(10):
    do_work()