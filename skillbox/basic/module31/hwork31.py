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


def get_episod_death(dl: List[dict], id: int, season: int,  episod: int) -> dict:
    for d in dl:
        if d["id"] == id and d["season"] == season and d["episod"] == episod:
            return d
    return dict()


base_url = "https://www.breakingbadapi.com/api/"
episods_url = "{0}{1}".format(base_url, "episodes")
deaths_url = "{0}{1}".format(base_url, "deaths")

result = requests.get(episods_url)
episodes = json.loads(result.text)
print(episods[0])

result = requests.get(deaths_url)
deaths : List[dict] = json.loads(result.text)
for episod in episods:
    deaths_episod = list(filter(lambda elem: elem["episode"] == episod["episode_id"], deaths))
