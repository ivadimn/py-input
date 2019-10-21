# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

number1 = int(input("Введите первое число : "))
number2 = int(input("Введите второе число : "))
number3 = int(input("Введите третье число : "))


if number1 < number2 < number3:
    average = number2
elif number2 < number1 < number3:
    average = number1
else:
    average = number3

print("Среднее значение = {}".format(average))
