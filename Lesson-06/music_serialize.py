# 1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
# вывести результаты в терминал. Записать результаты в файлы group.json, group.pickle соответственно.
# В файле group.json указать кодировку utf-8

import pickle
import json
json_file = "group.json"
pickle_file = "group.pickle"

my_favourite_group = {
"name": "Г.М.О.",
"tracks": ["Последний месяц осени", "Шапито"],
"Albums": [{"name": "Делать панк-рок","year": 2016},
{"name": "Шапито","year": 2014}]}
print("Исходный объект:")
print(my_favourite_group)
print(type(my_favourite_group))

json_data = json.dumps(my_favourite_group);
print("После преобразования в JSON :")
print(json_data)
print(type(json_data))

with open(json_file, "w", encoding="utf-8") as fs:
    json.dump(my_favourite_group, fs)

print("Записано в файл group.json")

byte_data = pickle.dumps(my_favourite_group);
print("После преобразования в bytes :")
print(byte_data)
print(type(byte_data))

with open(pickle_file, "wb") as fp:
    pickle.dump(my_favourite_group, fp)

print("Записано в файл group.pickle")