from typing import List
import pandas as np
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from time import sleep
import json


def read_subjects(filename: str) -> List[str]:
    subs = list()
    with open(filename, "r") as f:
        for line in f:
            subs.append(line[:-1].lower())
        return subs


def save_locations(locs: List):
    with open("locations.txt", "w") as f:
        for l in locs:
            f.write("{0},{1},{2}\n".format(l[0], l[1][0], l[1][1]))


def map_locations(locations: np.Series):
    #geolocator = Nominatim(user_agent='Gazprom_app', timeout=3)
    unique_locations = locations.unique()
    map_locs = []
    for location in unique_locations:
        sleep(1)
        if location:
            #position = geolocator.geocode(location)
            position = Nominatim(user_agent='Gazprom_app', timeout=3).geocode(location)
            if position is not None:
                map_locs.append((location, (position.latitude, position.longitude)))
                print(location, position.latitude, position.longitude)
            else:
                map_locs.append((location, (None, None)))
                print(location, "None", "None")
    #return np.DataFrame(map_locs, columns=['country_subject', 'position'])
    return map_locs


if __name__ == "__main__":
    l = read_subjects("subjects.txt")
    locs = np.Series(l)
    save_locations(map_locations(locs))

