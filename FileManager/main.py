import sys
from core import create_file, create_folder, copy_file, delete_file, get_list, save_info, change_dir

save_info("Start")
command = sys.argv[1]

if command == "list":
    if len(sys.argv) > 2 and sys.argv[2] == "dir":
        get_list(True)
    else:
        get_list()
elif command == "create_file":
    try:
        name = sys.argv[2]
        if len(sys.argv) == 3:
            create_file(name)
        else:
            text = "\n".join(sys.argv[3:])
            create_file(name, text)
    except IndexError :
        print("Необходимо указать имя файла")
elif command == "create_folder":
    try:
        name = sys.argv[2]
        create_folder(name)
    except IndexError :
        print("Необходимо указать имя каталога")
elif command == "copy":
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
        copy_file(name, new_name)
    except IndexError:
        print("Необходимо имя файла источника и имя нового файла")
elif command == "delete":
    try:
        name = sys.argv[2]
        delete_file(name)
    except IndexError:
        print("Необходимо указать имя файла или каталога")
elif command == "change":
    try:
        name = sys.argv[2]
        change_dir(name)
        get_list()
    except IndexError:
        print("Необходимо указать имя каталога")
elif command == "help":
    print("Список доступных команд:")
    print("Показать список файлов и каталогов: list [dir - если нужны только каталоги]")
    print("Создать файл: create_file filename [текс для записи в файл]")
    print("Создать каталог: create_folder foldername")
    print("Копировать файл или каталог: copy source destination")
    print("Удалить файл или каталог: delete filename")
    print("Изменить текущий рабочий каталог: change foldername")
