#  Функция для замера памяти
import sys

def show_sizeof(x, level=0):
    print("\t" * level, x.__class__, sys.getsizeof(x), x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_sizeof(xx, level + 1)

#подсчитывает общий размер объекта
def sizeof(x):
    size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                size += sizeof(xx)
        elif not isinstance(x, str):
            for xx in x:
                size += sizeof(xx)
    return size