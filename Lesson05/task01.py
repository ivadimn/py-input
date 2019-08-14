# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os


def create_dirs():
    for i in range(1, 10):
        new_dir = os.path.join(os.getcwd(), "{}_{}".format("dir", i))
        os.mkdir(new_dir)


def delete_dirs():
    for i in range(1, 10):
        del_dir = "{}_{}".format("dir", i)
        os.removedirs(del_dir)

#create_dirs()
delete_dirs()