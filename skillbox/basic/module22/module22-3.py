import os
"""
file = open('/home/vadim/task/Additional_info/group_1.txt', 'r', encoding="utf-8")
summa = 0
diff = 0
for i_line in file:
    info = i_line.split()
    balls = int(info[2])
    summa += balls
    diff -= balls
file.close()

file_2 = open('/home/vadim/task/Dont touch me/group_2.txt', 'r', encoding="utf-8")
compose = 1
for i_line in file_2:
    info = i_line.split()
    compose *= int(info[2])
file_2.close()

print(summa)
print(diff)
print(compose)
"""


def find_files(cur_path, file_name):
    files = []
    #print("Просматриваем каталог: {0}".format(cur_path))
    for elem in os.listdir(cur_path):
        path = os.path.join(cur_path, elem)
        if os.path.isdir(path):
            files.extend(find_files(path, file_name))
        else:
            if elem == file_name:
                files.append(path)
    return files

path = os.path.abspath(os.path.join("..", ".."))
files = find_files(path, "hello.go")
file = open(files[0], "r", encoding = "utf-8")
for line in file:
    print(line, end = "")