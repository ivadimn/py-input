"""
def average(a, b):
    summ = 0
    for n in range(a, b + 1):
        summ += n
    print("Среднее арифметическое чисел в диапазоне [", a, ",", b, "]:", summ / (b - a + 1))

a = int(input("Введите левую границу: "))
b = int(input("Введите прапвую границу: "))
average(a, b)


def myAddress(fname, sname, country, city, street, house_number, flat_number):
    print("Фамилия:", fname)
    print("Имя:", sname)
    print("Страна проживания:", country)
    print("Город:", city)
    print("Улица:", street)
    print("Номер дома:", house_number)
    print("Номер квартиры:", flat_number)
    print()

myAddress("Пупкин", "Вася", "USA", "Denver", "57-street", 35, 10)
"""
import math

choice  = int(input("Чего вы хотите — 1 найти расстояние от себя до точки или 2 найти расстояние между двумя произвольными точками: "))
if choice == 1:
    x = float(input("Введите координату точки X: "))
    y = float(input("Введите координату точки Y: "))
    distance = math.sqrt(x ** 2 + y ** 2)
    print("Расстояние до точки с координатами", x, ",", y, "равно:", distance)
elif choice == 2:
    x1 = float(input("Введите координату точки X1: "))
    y1 = float(input("Введите координату точки Y1: "))
    x2 = float(input("Введите координату точки X2: "))
    y2 = float(input("Введите координату точки Y2: "))
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("Расстояние между точками с координатами", x1, ",", y1, "и", x2, ",", y2,  "равно:", distance)
else:
    print("Не правильный выбор!")