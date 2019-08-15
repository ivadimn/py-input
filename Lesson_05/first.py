

# 1: Создайте модуль (модуль - программа на Python, т.е.
#     файл с расширением .py). В нем создайте функцию
# создающую директории от dir_1 до dir_9 в папке из которой
# запущен данный код. Затем создайте вторую функцию удаляющую эти папки.
# Проверьте работу функций в этом же модуле.

import os, sys

name = str('Lesson 5')

def creation():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        os.mkdir(new_path)

def removal():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        os.rmdir(new_path)

#creation()
removal()





