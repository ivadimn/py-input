from typing import Callable, Any

def callback(url: str) -> Callable:
    def wrapper_callback(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            result = func(*args, **kwargs)
            return result
        return wrapper
    return wrapper_callback

@callback("//")
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

print(example())