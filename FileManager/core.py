import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding="utf-8") as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Папка с таким именем уже существует!")


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except FileNotFoundError:
        print("Файл с таким именем не найден!")


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print("Папка, с таким именем уже существует!")
    else:
        try:
            shutil.copy(name, new_name)
        except FileNotFoundError:
            print("Файл с именем {} не найден".format(name))


def save_info(message):
    current_time = datetime.datetime.now();
    result = "{} - {}".format(current_time, message)
    with open("log.txt", 'a', encoding="utf-8") as f:
        f.write(result + "\n")


