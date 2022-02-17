import re
import requests
import json
from pprint import pprint
from typing import List
import itertools

text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

"""
pattern = r"\b\w{4}[\s\.,]"
words = re.findall(pattern, text)
print(words)

text = "А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666"
pattern_car = r"\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}"
pattern_taxi = r"\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}"
numbers_car = re.findall(pattern_car, text)
numbers_taxi = re.findall(pattern_taxi, text)
print(numbers_car)
print(numbers_taxi)

phones = ['9999999999', '999999-999', '99999x9999', "89237226789", "8923722789", "8923789" ]
phone_pattern = r"^[89]\d{9}$"
for i, phone in enumerate(phones):
    print("{0} номер: {1}".format(i, "всё в порядке" if re.match(phone_pattern, phone) else "не подходит"))

pins = []
for pin in itertools.product("0123456789", repeat=4):
    pins.append("".join(pin))
print(pins)


h3_pattern = r"<[hH]3.*>(.*)</[hH]3>"

url = "http://www.columbia.edu/~fdc/sample.html"
result = requests.get(url)
h3 = re.findall(h3_pattern, result.text)
print(h3)

skillbox_url = "https://skillbox.ru/"
result = requests.get(skillbox_url)
h3 = re.findall(h3_pattern, result.text)
print(h3)
"""


deaths_list = []


def get_episod_death(dl: List[dict], id: int, season: int,  episode: int) -> dict:
    for d in dl:
        if d["ID эпизода"] == id and d["Номер сезона"] == season and d["Номер эпизода"] == episode:
            return d
    new_d = {"ID эпизода": id, "Номер сезона": season, "Номер эпизода": episode,
             "Общее количество смертей": 0, "Список погибших": []}
    dl.append(new_d)
    return new_d


base_url = "https://www.breakingbadapi.com/api/"
episods_url = "{0}{1}".format(base_url, "episodes")
deaths_url = "{0}{1}".format(base_url, "deaths")

result = requests.get(episods_url)
episodes = json.loads(result.text)


result = requests.get(deaths_url)
deaths : List[dict] = json.loads(result.text)
for episod in episodes:
    deaths_episod = filter(lambda elem: elem["episode"] == int(episod["episode"])
                                             and elem["season"] == int(episod["season"]), deaths)
    for de in deaths_episod:
        d = get_episod_death(deaths_list, episod["episode_id"], int(de["season"]), int(de["episode"]))
        d["Общее количество смертей"] += de["number_of_deaths"]
        d["Список погибших"].append(de["death"])

#pprint(deaths_list)
death_max = max(deaths_list, key=lambda elem: elem["Общее количество смертей"])
print("Максимальное количество смертей в: ")
for k, v in death_max.items():
    print("{0}: {1}".format(k, v))

with open("death_max.json", "w", encoding="UTF-8") as file:
    json.dump(death_max, file, skipkeys=True)
