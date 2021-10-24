#D = x^3 − 3x^2 − 12x + 10
import math

def danger_level(x):
    return x ** 3 - 3 * (x ** 2) - 12 * x + 10

x = 0
while  x < 4 :
    x += 0.0001
    level = danger_level(x)
    print(level)
    if abs(level - 0.01) < 1e-3:
        break


print(x)


