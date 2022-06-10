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
"https://www.hotels.com/ho203837/" \
"hotel-caesar-prague-prague-czech-republic/" \
"?chkin=2022-06-18" \
"&chkout=2022-06-20" \
"&x_pwa=1" \
"&rfrr=HSR" \
"&pwa_ts=1654850324750" \
"&referrerUrl=aHR0cHM6Ly93d3cuaG90ZWxzLmNvbS9Ib3RlbC1TZWFyY2g%3D" \
"&useRewards=false" \
"&rm1=a2&" \
"regionId=2872" \
"&destination=Prague%2C+Czech+Republic" \
"&destType=MARKET" \
"&neighborhoodId=6004758" \
"&trackingData=AAAAEBFpRWP1IEq7JJRZdbTemmibt4Z6-88-v0pdZbdCPZ0yDXep-uzBTrf6i3NA3HaA1dL7DH7HftBkLexTG6_shxq4h4L8ZwyjIzUE1CEBt9YOXZcFI7W2IcTcocpFI8-xFzCgrAZxQH8yO-1pU4HOd6b_R1WrJu5MZLyE6gNc7HXzY1RPG2JvCVQPgK-bOEjO8abwQeE4ZDGgKgbSn9lFW-LBKOOHXX9HXYjovKR80A59cnXOVrCk5rse4HND1DdmMk_LB1yE4Iy3ZUm7q_fYveIyxvUGMITRxWNZv_TvR_vBedNMmAyrnm2ThsZLQs1btwqYjzLbsGP0QZ1gl9bJz9WHCROWBlQlch3pRgMDC2denuvj1aNAyNU43N9uK6sR3eDMNY34uhboNVa5cfsHfe6nv4zUUaETarYRbs5J04mghGVFD9lEkZ5EbuMdhjoWS9tQWOVArWI3IiaxHBbDhnniNqWUJYVVyE6R-RtEA64CzkDjuOm9U5GQiTo4BTuqjg35YcDfY6aqfs0aRxodzMkxQTilKaQCCVXfigBgWSnRqIPXQhUSdyzhMWjLl7b00JGAGo1aJXmiUGOynoIP_GrNJnYl-8wS5I5Ez341QLoUrtk0GbuXde-zJVHnPzq7xSKVE5b1gh2L4ce8mwrodDwmfWwKf_tcIZt_xxV7teeK6fpcIm7Ls5191_JKNzNcIeRhH8dkGvKmCGSJbc3VnbFCBNGYXK4_gMc4WPHAfp00skKO4hqSyvpLvo-0YMqPuj8mlAfHI_3o_H8vVjDgH4OUsEI8bNiK_Lic_GXx9VWU8Ba8eZvuLLsLoG08z2tDM793IKc-OoXBNzE3DfnYUHZaODsSUco4CBh-fhpk77Q4nWdgIeyUdxt5RWoKiLu-gYdGWFAlDvYdYXqXQ4jNw2ifYUHKAg-a6WWLWJUYDf--ok1WkPjso6S9E0am4almS_9KA_FAszUIf7Om3K7a0d6VCbjtXGmMF8AYDW8BhbZif6wysgIxxXM70gv095pTIQ%3D%3D" \
"&rank=1" \
"&testVersionOverride=Buttercup%2C43549.127812.0%2C43550.0.0%2C31936.102311.0%2C33775.98848.1%2C38414.114301.0%2C39483.0.0%2C38427.115718.1%2C42444.123988.0%2C42589.0.0%2C42876.124673.0%2C42973.124182.1%2C42974.123984.1%2C42975.124629.0%2C42976.125426.1%2C42802.125960.1%2C43153.128111.1%2C33739.99567.0%2C37898.109354.0%2C37930.119094.0%2C37949.0.0%2C37354.0.0%2C43191.128259.1%2C43435.128144.0" \
"&slots=HSR_A" \
"&position=1" \
"&beaconIssued=2022-06-10T08%3A38%3A43" \
"&sort=RECOMMENDED" \
"&top_dp=169" \
"&top_cur=EUR" \
"&semdtl=&userIntent=&selectedRoomType=311953&selectedRatePlan=200826002&expediaPropertyId=1236320"
"https://www.hotels.com/ho376202/?chkin=2022-06-18&chkout=2022-06-20"

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
