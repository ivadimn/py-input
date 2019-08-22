import sys
from core import create_file, create_folder, delete_file, get_list, copy_file, save_info, change_dir
from game import game, game_number

save_info('старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Отсутсвуте параметр вызова')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвуте название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвуте название файла')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвуте название файла')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Отсутсвуте название файла')
        else:
            copy_file(name, new_name)
    elif command == 'c_dir':    # --------- СМЕНА ПАПКИ ------------
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутсвуте название файла')
        else:
            change_dir(name)
    elif command == 'game':     # ------------- ИГРА --------------
        try:
            game_n = sys.argv[2]
        except IndexError:
            print('У нас аж 2 игры. Выберите игру.')
        else:
           if sys.argv[2] == 1:
               game_number()
           elif sys.argv[2] == 2:
               game()
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('c_dir - копирование файла или папки')
        print('game - игра. 1 - вы загажываете число, 2 - компьютер загадывает число')

save_info('конец')
