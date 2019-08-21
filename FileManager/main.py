import sys
from core import create_file, create_folder, copy_file, delete_file, get_list, save_info


command = sys.argv[1]

if command == "list":
    get_list()
elif command == "create_file":
    pass
elif command == "create_folder":
    pass
elif command == "copy":
    pass
elif command == "delete":
    pass
elif command == "help":
    pass


