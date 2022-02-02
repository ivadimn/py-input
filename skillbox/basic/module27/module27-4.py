from typing import Callable, Any


def sandwich(*args) -> Any:
    for arg in args:
        print(arg)



sandwich("помидоры", "сыр", "мясо")