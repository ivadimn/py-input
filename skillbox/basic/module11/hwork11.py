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


print("Введите местополржение коня")
horse_x = float(input("По горизонтали: "))
while horse_x < 0 or horse_x > 0.8:
    print("Вводимое значение должно быть больше 0 и меньше 0.8. Повторите попытку! ")
    horse_x = float(input("По горизонтали: "))

horse_y = float(input("По вертикали: "))
while horse_y < 0 or horse_y > 0.8:
    print("Вводимое значение должно быть больше 0 и меньше 0.8. Повторите попытку! ")
    horse_y = float(input("По вертикали: "))

print("Введите местополржение точки на доске:")
point_x = float(input("По горизонтали: "))
while point_x < 0 or point_x > 0.8:
    print("Вводимое значение должно быть больше 0 и меньше 0.8. Повторите попытку! ")
    point_x = float(input("По горизонтали: "))

point_y = float(input("По вертикали: "))
while point_y < 0 or  point_y > 0.8:
    print("Вводимое значение должно быть больше 0 и меньше 0.8. Повторите попытку! ")
    point_y = float(input("По вертикали: "))

horse_x = int(horse_x * 10)
horse_y = int(horse_y * 10)
point_x = int(point_x * 10)
point_y = int(point_y * 10)
print("Конь в клетке (", horse_x, ",", horse_y, "). Точка в клетке (", point_x, "," , point_y, ").")
if ((abs(point_x - horse_x) == 1) and (abs(point_y - horse_y) == 2)) \
        or ((abs(point_x - horse_x) == 2) and (abs(point_y - horse_y) == 1)):
    print("Да, конь может ходить в эту точку.")
else:
    print("Нет, конь не может ходить в эту точку.")

# при повороте часовой стрелки на 1 градус
# минутная стрелка поворачивается на 12 градусов
hours_hand_angle = float(input("Введите угол, на который повернулась часовая стрелка: "))
bound_hour_angle = hours_hand_angle % 30
minute_hand_angle = bound_hour_angle  * 12 + 360 * int(abs(math.sin((90 + bound_hour_angle) * (math.pi / 180)))) \
                    * math.ceil(abs(math.sin(hours_hand_angle) * (math.pi / 180)))
print("Минутная стрелка с начала последнего часа повернулась на", minute_hand_angle, "градусов" )


print("Введите коэффитценты квадратного уравнения (ax^2 + bx + c = 0)")
a = float(input("Коэффициент a: "))
b = float(input("Коэффициент b: "))
c = float(input("Коэффициент c: "))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(x2, x1)
elif d == 0:
    x = -(b / (2 * a))
    print(x)
"""
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
max = ((a + b) + abs(a - b)) / 2
print(int(max))


