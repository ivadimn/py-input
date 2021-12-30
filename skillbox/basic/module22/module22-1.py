import os
"""
file_name = "admin.bat"
path = os.path.join("..",  "..")
print(os.path.abspath(path))
print(path)



def print_dirs(path):
    for elem in os.listdir(path):
        print(os.path.abspath(elem))

path = os.path.join("..")
abs_path = os.path.abspath(path)
print_dirs(abs_path)
"""

print(os.path.curdir)
path = os.path.abspath(os.path.curdir)
print(os.path.sep)
print(os.path.join(os.path.splitdrive(path)[0], os.path.sep))
