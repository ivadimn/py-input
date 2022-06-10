from requests import request, codes
from pprint import pprint
import json
import re

RAPID_API_KEY = "f961b0c4f5mshb054c85654b883ep127525jsnbc10f2dddbb5"
RAPID_API_HOST = "hotels4.p.rapidapi.com"
CITY_URL = "https://hotels4.p.rapidapi.com/locations/v2/search"
HOTELS_URL = "https://hotels4.p.rapidapi.com/properties/list"
PHOTOS_URL = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"
DETAIL_URL = "https://hotels4.p.rapidapi.com/properties/get-details"
"https://hotels.com/dl/hotel/details.html?hotelId=376202&q-check-in=2022-08-01&q-check-out=2022-08-11&q-rooms=1&q-room-0-adults=1&q-room-0-children=0"
"https://hotels.com/dl/hotel/details.html?hotelId=376202"

city_id = 1634829
h1 = 376202
h2 = 372141


params = {"locale": "ru_RU", "currency": "USD"}
hotel_params  = {"destinationId": city_id, "pageNumber": 1, "pageSize": 25, "checkIn": "2022-01-08",
                 "checkOut": "2022-01-15", "adults1": 2, "sortOrder": "PRICE",
                 "locale": "en_US", "currency": "USD" }



def parce_result(text: str, pattern: str) -> dict:
    find = re.search(pattern, text)
    if find:
        return json.loads("{{{0}}}".format(find.group(0)))
    else:
        return {}


def query_api(url: str, params: dict) -> str:
    headers = {"x-rapidapi-host": RAPID_API_HOST, "x-rapidapi-key": RAPID_API_KEY}
    response = request("GET", url, headers=headers, params=params, timeout=10)
    if response.status_code == codes.ok:
        return response.text
    else:
        return ""


def get_city(city:  str):
    params.update({"query": city})
    data = query_api(CITY_URL, params)
    pprint(json.loads(data))

def get_hotels(id: int):
    hotel_params["destinationId"] = id
    data = query_api(HOTELS_URL, hotel_params)
    hotels = parce_result(data, r'(?<=)"results":.+?(?=,"pagination)')
    pprint(hotels)

def get_detail(id: int):
    hotel_params["id"] = id
    data = query_api(DETAIL_URL, {"id": id})
    details = json.loads(data)
    pprint(details)

get_hotels(city_id)
