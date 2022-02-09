from typing import Callable, Any

user_permissions = ['admin']


def check_permission(user: str) -> Callable:
    def wrapper_func(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            if user not in user_permissions:
                error = "У пользователя {0} недостаточно прав, чтобы выполнить функцию {1}".format(user, func.__name__)
                raise PermissionError(error)
            else:
                return func(*args, **kwargs)
        return wrapper
    return wrapper_func


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()


def singleton(cls):
    def wrapper(*args, **kwargs):
        if wrapper.instance is None:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance
    wrapper.instance = None
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()
print(id(my_obj))
print(id(my_another_obj))
print(my_obj is my_another_obj)


from typing import Callable, Any
from datetime import datetime
import time


def create_format(format: str) -> str:
    fmt = ""
    for ch in format:
        if ch.isalpha():
            fmt= "".join([fmt, "%", ch])
        else:
            fmt = "".join([fmt, ch])
    return fmt


def logging(cls, func: Callable, format: str) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        now = datetime.today()
        print("- Запускается '{0}.{1}'. Дата и время запуска: {2}".
              format(cls.__name__, func.__name__, now.strftime(create_format(format))))
        start = time.time()
        result = func(*args, **kwargs)
        print("- Завершение '{0}.{1}', время работы = {2}s".format(cls.__name__, func.__name__, round(time.time() - start, 3)))
        return result
    return wrapped_func

def log_methods(format: str) -> Callable:
    def decorate(cls):
        for func_name in dir(cls):
            if not func_name.startswith("__"):
                func = getattr(cls, func_name)
                decorate_method = logging(cls, func, format)
                setattr(cls, func_name, decorate_method)
        return cls
    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника")

    def test_sum_2(self):
        print("Тут метод test sum 2 у наследника")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()


def decorator_with_args_for_any_decorator(func: Callable) ->Callable:
    def wrapper(*args, **kwargs) -> Any:
        print("Переданные арги и кварги в декоратор: {0} {1}".format(args, kwargs))
        result = func(*args, **kwargs)
        return result
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    def wrapper_decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            result = func(*args, **kwargs)
            return result
        return wrapper
    return wrapper_decorator


@decorated_decorator(100, 'рублей', 200, 'друзей', 1000, "мелочей")
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)