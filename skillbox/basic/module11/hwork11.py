import math
"""
price_eoro = float(input("Введите стоимость покупки в евро: "))
price_usd = price_eoro * 1.25
price_rub = price_usd * 60.87
print("Стоимость покупки в долларах:", round(price_usd, 2))
print("Стоимость покупки в рублях:", round(price_rub, 2))


numbers_count = int(input("Введите количество чисел в поледовательности: "))
for n in range(1, numbers_count + 1):
    print("Введите", n, "-е число последовательности: ", end="")
    number = float(input())
    if number > 0:
        number = math.ceil(number)
        print("x = ", number, "  log(x) = ", math.log(number))
    elif number < 0:
        number = math.floor(number)
        print("x = ", number, "  exp(x) = ", math.exp(number))
    else:
        print("Ноль не обрабатывается")

file_size = int(input("Укажите размер файла для скачивания: "))
while file_size <= 0:
    print("Размер файла должен быть целым положительным числом большее 0, повторите попытку: ", end = "")
    file_size = int(input())
speed = int(input("Какова скорость вашего соединения? "))
while speed <= 0:
    print("Скорость соединения должна быть целым положительным числом большее 0, повторите попытку: ", end = "")
    speed = int(input())
time_count = 0
download_size = 0
while download_size < file_size - speed:
    time_count += 1
    download_size += speed
    percent = int(round((download_size * 100) / file_size, 0))
    print("Прошло", time_count, "сек. Скачано", speed * time_count, "из",  file_size, "Мб", "(", percent, "%)")
else:
    time_count += 1
    print("Прошло", time_count, "сек. Скачано", file_size, "из", file_size, "Мб", "( 100 %)")

number = float(input("Введите действительное положительное число: "))
first_digit = int(number * 10) % 10
print("Первая цифра после десятичной точки числа", number, "  :", first_digit )


earth_volum = 10.8321e11
radius = float(input("Введите радиус случайной планеты: "))
volum = 4 * math.pi * (radius ** 3) / 3
if earth_volum > volum:
    print("Объём планеты Земля больше в", round(earth_volum / volum, 3), "раз")
elif earth_volum < volum:
    relation = earth_volum / volum
    print("Объём планеты Земля меньше в (1/",round(relation, 3), ") =", round(1 / relation, 3),  "раз")
else:
    print("Обэёмы равны!")
"""

low_bound = int(input("Нижняя граница: "))
up_bound = int(input("Верхняя граница: "))
step = int(input("Шаг: "))
print("C", " \t",  "F")
for t in range(low_bound, up_bound, step):
    farengeit = t * 1.8 + 32
    print(t, "\t", int(farengeit))
else:
    farengeit = up_bound * 1.8 + 32
    print(up_bound, "\t", int(farengeit))