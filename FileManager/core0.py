import os
import shutil
import datetime
import sys


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


def change_dir(name):
    try:
        os.chdir(name)
    except FileNotFoundError:
        print("Каталога с именем: {} не существует".format(name))


def save_info(message):
    current_time = datetime.datetime.now();
    result = "{} - {}".format(current_time, message)
    with open("log.txt", 'a', encoding="utf-8") as f:
        f.write(result + "\n")


def play():
    print("Компьютер буде угадывать задуманное Вами число!!")
    input("Задумайте чило от 1 до 100 и нажмите Enter ")
    number = 50
    delta = number
    result = None
    while result != "=":
        result = input(
            "Ваше число {} если Ваше число больше введите '>' если меньше '<' если угадал '=' : ".format(number))
        delta = delta // 2 + delta % 2
        if result == ">":
            number = number + delta
        elif result == "<":
            number = number - delta
    print("Компьютер угадал число {} ".format(number))


def show_command():
    print("Список доступных команд:")
    print("Показать список файлов и каталогов: list [dir - если нужны только каталоги]")
    print("Создать файл: create_file filename [текс для записи в файл]")
    print("Создать каталог: create_folder foldername")
    print("Копировать файл или каталог: copy source destination")
    print("Удалить файл или каталог: delete filename")
    print("Изменить текущий рабочий каталог: change foldername")
    print("Поиграть с компьютером: play")
