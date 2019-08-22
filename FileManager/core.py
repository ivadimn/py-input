import os
import shutil
import datetime


# создание файла
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# создание папки
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('такая папка уже есть')


# просмотр списка файлов и папок
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# удаление файла или папки
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


# копирование фалов и папок
def copy_file(name, new_name):
    if os.path.isdir(name):  # копирование папки
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:  # копирование файла
        shutil.copy(name, new_name)


# смена текущей директории
def change_dir(name):
    os.chdir(name)
    print(os.getcwd())  # печать новой директории


# запись информации о работе менеджера в файл
def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


if __name__ == '__main__':
    pass
