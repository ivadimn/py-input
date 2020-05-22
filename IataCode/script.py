import requests
import json


link = "https://www.travelpayouts.com/widgets_suggest_params?q="

print("Определение IATA кодов городов")
while True:
    origin = input("Введите город отправления : ")
    destination = input("Введите город назначения : ")
    search = "Из%20" + origin + "%20в%20" + destination
    data = json.loads(requests.get(link+search).text)
    key_origin = data.get("origin");
    if key_origin:
        print("Город отправления: IATA код города " + key_origin["name"] + " - " + key_origin["iata"])
    else:
        print("Вернулось пустое значение для города отправления !!!")
    key_destination = data.get("destination");
    if key_origin:
        print("Город назначения: IATA код города " + key_destination["name"] + " - " + key_destination["iata"])
    else:
        print("Вернулось пустое значение для города назначения!!!")
    if input("Нажмите ENTER для продолжения или exit для выхода ") == "exit":
        break