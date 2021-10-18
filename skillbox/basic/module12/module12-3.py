import math
"""
def aboutWater(price):
    print("Название: КлирВотер")
    print("Производитель: ВодЗавод")
    print("Цена:", price)
    print()

aboutWater(50)
aboutWater(45)
aboutWater(30)

def sphereArea(radius):
    print("Площадь сферы: ", 4 * math.pi * (radius ** 2))

def sphereVolume(radius):
    print("Объём шара: ", 4 * math.pi * (radius ** 3) / 3)

radius = float(input("Введите радиус: "))
sphereArea(radius)
sphereVolume(radius)
"""

def isPrime(number):
    for d in range(2, number):
        if number % d == 0:
            break
    else:
        if number > 1:
            print(number, "- простое число!")

seq_count = int(input("Введите количество чисел в последовательности: "))
for n in range(1, seq_count + 1):
    print("Введите", n, "-е число последовательности: ", end = "" )
    number = int(input())
    isPrime(number)
