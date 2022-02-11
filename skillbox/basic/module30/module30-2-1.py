from typing import Callable, Any
#import builtins
#count = 0

def counter(func: Callable) -> Callable:
    count = 0
    def wrapper(*args, **kwargs) -> Any:
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        print(count)
        return result
    return wrapper

@counter
def f1(msg : str) -> None:
    print("Сообщение: {0}".format(msg))

f1("Hello 1!")
f1("Hello 2!")
f1("Hello 3!")
f1("Hello 4!")

print(dir(__builtins__))



