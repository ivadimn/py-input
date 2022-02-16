import re
import requests
import json
from pprint import pprint
from typing import List

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
"""

base_url = "https://www.breakingbadapi.com/api/"
episods_url = "{0}{1}".format(base_url, "episodes")
result = requests.get(episods_url)
episods = json.loads(result.text)
#for episod in episods:
#    print(episod["episode_id"])
pprint(episods[0])
print(len(episods))

print("*" * 40)

deaths_url = "{0}{1}".format(base_url, "deaths")
result = requests.get(deaths_url)
deaths : List[dict] = json.loads(result.text)
df = filter(lambda elem: elem["episode"] == 1, deaths)
#pprint(list(df))
pprint(deaths)

print(len(deaths))