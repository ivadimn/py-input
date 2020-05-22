# 2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle,
# прочитать из них информацию. И получить объект: словарь из предыдущего задания.

import pickle
import json

json_file = "group.json"
pickle_file = "group.pickle"

with open(json_file,'r', encoding="utf-8") as fs:
    my_favourite_group = json.load(fs)

print("После чтения из файла group.json")
print(my_favourite_group)
print(type(my_favourite_group))

with open(pickle_file,'rb') as fp:
    my_favourite_group = pickle.load(fp)

print("После чтения из файла group.pickle")
print(my_favourite_group)
print(type(my_favourite_group))