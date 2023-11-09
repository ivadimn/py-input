from typing import List
import pandas as np
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from time import sleep
import


def read_subjects(filename: str) -> List[str]:
    subs = list()
    with open(filename, "r") as f:
        for line in f:
            subs.append(line[:-1])
        return subs

def save_locations(locs: List):
    with open()

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
            else:
                map_locs.append((location, (None, None)))
            print(location, position.latitude, position.longitude)
    #return np.DataFrame(map_locs, columns=['country_subject', 'position'])
    return map_locs


if __name__ == "__main__":
    l = read_subjects("subjects.txt")
    locs = np.Series(l)
    print(map_locations(locs))

