#D = x^3 − 3x^2 − 12x + 10
import math

def danger_level(x):
    return x ** 3 - 3 * (x ** 2) - 12 * x + 10

max_danger = float(input("Введите максимально допустимый уровень опасности: "))
while max_danger <= 0:
    print("Максимально допустимый уровень опасности должен быть больше 0. Повторите попытку :", end = "")
    max_danger = float(input())

d_min = 0
d_max = 4
while  True:
    d_middle = (d_min + d_max) / 2
    d = danger_level(d_middle)

    x += 0.0001
    level = danger_level(x)
    print(level)
    if abs(level - 0.01) < 1e-3:
        break


print(x)


