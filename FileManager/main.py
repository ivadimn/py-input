import sys
from core import create_file, create_folder, copy_file, delete_file, get_list, save_info, change_dir, show_command, play

save_info("Start")
try:
    command = sys.argv[1]
except IndexError:
    print("Необходимо ввести команду")
    command = "help"

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
        save_info("Создан файл - {}".format(name))
    except IndexError:
        print("Необходимо указать имя файла")
elif command == "create_folder":
    try:
        name = sys.argv[2]
        create_folder(name)
        save_info("Создан каталог - {}".format(name))
    except IndexError :
        print("Необходимо указать имя каталога")
elif command == "copy":
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
        copy_file(name, new_name)
        save_info("Скопировано из {} в {}".format(name, new_name))
    except IndexError:
        print("Необходимо имя файла источника и имя нового файла")
elif command == "delete":
    try:
        name = sys.argv[2]
        delete_file(name)
        save_info("Удалено - {}".format(name))
    except IndexError:
        print("Необходимо указать имя файла или каталога")
elif command == "change":
    try:
        name = sys.argv[2]
        change_dir(name)
        get_list()
    except IndexError:
        print("Необходимо указать имя каталога")
elif command == "play":
    play()
elif command == "help":
    show_command()


save_info("End")