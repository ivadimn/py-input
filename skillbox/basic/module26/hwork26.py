from collections.abc import Iterable, Iterator
import os

"""
class NumberSquare:
    def __init__(self, count: int) -> None:
        self.__count : int = count
        self.__current : int = 0

    def __iter__(self) -> Iterator:
        self.__current = 0
        return self

    def __next__(self) -> int:
        self.__current += 1
        if self.__current > self.__count:
            raise StopIteration
        return self.__current ** 2


def number_square(count: int) -> Iterable:
    for n in range(1, count + 1):
        yield n ** 2

count = int(input("Введите целое число: "))

num_square_generator = (n ** 2 for n in range(1, count + 1))

print("Квадраты чисел от 1 до {0}".format(count))
print("Класс итератор: ")
class_iter = NumberSquare(count)
for sn in class_iter:
    print(sn, end = " ")
print()

print("Функция генератор: ")
fg = number_square(count)
for sn in fg:
    print(sn, end = " ")

print()
print("Генераторное выражение: ")
for sn in num_square_generator:
    print(sn, end = " ")


def multi_nums_generator(lst1 : list, lst2: list) -> Iterable:
    for x in lst1:
        for y in lst2:
            yield x, y, x * y


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
for x, y, xy in multi_nums_generator(list_1, list_2):
    print(x, y, xy)
    if xy == to_find:
        print("Found!!")
        break
"""


def gen_files_path(cur_path: str) -> Iterable:
    if not os.path.exists(cur_path):
        return
    for elem in os.listdir(cur_path):
        path = os.path.join(cur_path, elem)
        if os.path.isdir(path):
            yield path
            yield from gen_files_path(path)
        else:
            yield path


def gen_files_path1(cur_path: str, search_dir: str) -> Iterable:
    if not os.path.exists(cur_path):
        return
    for elem in os.listdir(cur_path):
        path = os.path.join(cur_path, elem)
        if elem == search_dir:
            yield path
            return
        if os.path.isdir(path):
            yield path
            yield from gen_files_path1(path, search_dir)
        else:
            yield path



path = input("Введите путь, где искать: ")
search_dir = input("Введите искомый каталог: ")
fg = gen_files_path(path)

for f in fg:
    print(f)
    if f.endswith(search_dir):
        print("Нашли!!")
        break

fg1 = gen_files_path1("/home/vadim/sql", search_dir)
for f in fg1:
    print(f)
    if f.endswith(search_dir):
        print("Нашли!")





