from typing import Callable, Any

app = {}

def callback(url: str) -> Callable:
    def wrapper_callback(func: Callable) -> Callable:
        app[url] = func
        def wrapper(*args, **kwargs) -> Any:
            result = func(*args, **kwargs)
            return result
        return wrapper
    return wrapper_callback

@callback("//")
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')