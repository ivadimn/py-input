import os
"""
file = open("numbers.txt", "r")
summ = 0
for num in file:
    summ += int(num)
file.close()

out_file = open("summ.txt", "w")
out_file.write(str(summ))
out_file.close()
"""

def write_scripts(cur_path, file):
    file.write("Скрипты из папки {0} \n\n".format(cur_path))
    for elem in os.listdir(cur_path):
        path = os.path.join(cur_path, elem)
        if os.path.isdir(path):
            write_scripts(path, file)
        else:
            if elem.endswith("py"):
                with open(path, "r") as f:
                    file.write(f.read())
                    file.write("\n{0}\n".format("*" * 40))

path_scripts = os.path.abspath(os.path.join(os.path.sep, "home", "vadim", "Python_Basic"))
with open("scripts.txt", "w") as sf:
    write_scripts(path_scripts, sf)



