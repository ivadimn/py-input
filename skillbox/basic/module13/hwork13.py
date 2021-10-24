import math

"""
def exponent(number):
   exp = 0
   while number >= 10 or number < 1:
       if number >= 10:
            number /= 10
            exp += 1
       elif number < 1:
           number *= 10
           exp -= 1
   return exp, number

x = float(input("Введите число: "))
while x <= 0:
    print("Вводимое число должнл быть больше 0. Попробуйте ещё раз: ", end = "")
    x = float(input())
exp, x  = exponent(x)
print("Формат плавающей точки: x =", x, "* 10 **", exp)



def max_number(n1, n2, n3):
    return max(n1, max(n2, n3))


n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))
n3 = int(input("Введите третье число: "))

print("Максимальное из трёх чисел: ", max_number(n1, n2, n3))


def invers(number):
    n = 0
    while number > 0:
        d = number % 10
        number //= 10
        n *= 10
        n += d
    return n

n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))
n1_inv = invers(n1)
n2_inv = invers(n2)

print("\nПервое число наоборот: ", n1_inv)
print("Второе число наоборот: ", n2_inv)
print("Сумма:", n1_inv + n2_inv)
print("\nСумма наоборот :", invers(n1_inv + n2_inv))


def get_mantissa_exponent(exp_number):
    mantissa = ""
    exponent = ""
    is_mantissa = True
    for ch in exp_number:
        if ch.isdigit() or ch == ".":
            if is_mantissa:
                mantissa += ch
            else:
                exponent += ch
        else:
            is_mantissa = False

    return mantissa, exponent


exp_number = input("Введите строку, содержащую экспоненциальную форму числа: ")

mantissa, exponent = get_mantissa_exponent(exp_number)
print("Мантисса:", mantissa)
print("Порядок:", exponent)


begin_amplitude = float(input("Введите начальную амплитулу: "))
while begin_amplitude <= 0:
    print("Амплитуда должна быть больше 0. Попробуйтк ещё: ", end = "")
    begin_amplitude = float(input())

end_amplitude = float(input("Введите амплитулу остановки: "))
while end_amplitude <= 0:
    print("Амплитуда должна быть больше 0. Попробуйтк ещё: ", end="")
    end_amplitude = float(input())

swing_count = 0
while begin_amplitude >= end_amplitude:
    swing_count += 1
    begin_amplitude -= begin_amplitude * 8.4 / 100
print("Маятник считается остановившимся через", swing_count, "колебаний")
"""

print(2 ** 6)
print(math.factorial(2))