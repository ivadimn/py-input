import requests
import json
import pprint
import swapi

"""
result = requests.get("https://swapi.dev/api/people/3/")
data = json.loads(result.text)
data["name"] = "Vadim"
pprint.pprint(data)
print("*" * 40)
homeworld = requests.get(data["homeworld"])
home_data = json.loads(homeworld.text)
pprint.pprint(home_data)

with open("starwar.json", "w") as file:
    json.dump(data, file, indent=4)

"""
result = requests.get("https://swapi.dev/api/starships/9/")
data = json.loads(result.text)
pprint.pprint(data)

print("*" * 40)
result = requests.get("https://swapi.dev/api/planets/2/")
data = json.loads(result.text)
pprint.pprint(data)

film = swapi.get_film(1)
#people = swapi.get_all('people')
#luke = swapi.get_person(1)
#tatooine = swapi.get_planet(1)
#print(luke)