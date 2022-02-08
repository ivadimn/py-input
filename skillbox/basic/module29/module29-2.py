from contextlib import contextmanager
from typing import Iterator
import time
import os

"""
@contextmanager
def timer() -> Iterator:
    print("\nВошли в контекст менеджер")
    start = time.time()
    try:
        yield
    finally:
        print(time.time() - start)
        print("Вышли из контекст менеджера")

with timer() as t:
    print("Первый замер")
    x = 1000 ** 1000 * 10
"""


@contextmanager
def in_dir(dir : str) -> Iterator:
    current_dir =os.path.abspath(os.curdir)
    try:
        os.chdir(dir)
        yield
    except Exception as ex:
        print(ex)
    finally:
        os.chdir(current_dir)

with in_dir("/"):
    print(os.listdir())

print(os.listdir())