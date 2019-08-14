# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.


def max_val(number1, number2, number3):
    return max(number1, number2, number3)


#другой вариант
def max_val2(*args):
    return max(args)


print(max_val(10, 34, 102))
print(max_val2(1, 6, 3, 10, 27, 120))
