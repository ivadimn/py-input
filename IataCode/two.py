# Напишите функцию получения IATA-кода города из его названия, используя API Aviasales для усовершенствования
# приложения по парсингу информации об авиабилетах, созданного нами в ходе урока.
# Примечание: воспользуйтесь документацией по API, которая доступна на странице www.aviasales.ru/API
# (ссылка на значке «API-документация»). Вам необходимо изучить раздел «API для определения IATA-кода».

# Бибилиотека для работы с http/https
import requests
import json


# Функция получения IATA кода города
def get_iata(input):
    # Отправляем запрос через API
    resp = requests.get('https://www.travelpayouts.com/widgets_suggest_params?q=Из {} в Лондон'.format(input))
    # Получаем текст ответа
    text = resp.text
    # Выдаем IATA код, если ответ не пустой, т.е. город в базе есть, в противном случае - None
    if text != '{}':
        data = json.loads(text)
        return data.get('origin').get('iata')
    else:
        return None


# Запрашиваем у пользователя название города
city = input('Введите название города: ')
# Вызов функции получения кода IATA
iata = get_iata(city)
# Выводим результат
if iata:
    print('IATA код : {}'.format(iata))
else:
    print('Нет города в базе.')