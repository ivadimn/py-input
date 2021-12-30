import os

"""
path = os.path.abspath(os.path.join(os.path.curdir, "module22-4.py"))
if os.path.exists(path):
    if os.path.isdir(path):
        print("{0} - это директория ".format(path))
    elif os.path.isfile(path):
        print("{0} - это файл ".format(path))
        print("Размер файла: {0} байт".format(os.path.getsize(path)))
    elif os.path.islink(path):
        print("{0} - это ссылка".format(path))
else:
    print("Укзанного пути не существует.")
"""


def find_files(cur_path, file_name):
    #print("Просматриваем каталог: {0}".format(cur_path))
    for elem in os.listdir(cur_path):
        path = os.path.join(cur_path, elem)
        if os.path.isdir(path):
            find_files(path, file_name)
        else:
            if elem == file_name:
                print(path)

path = os.path.abspath(os.path.join("..", ".."))
find_files(path, "hello.go")

