"""number = int(input("Введите конечное число: "))
number_count = 1
while number_count <= number:
    print(number_count ** 3)
    number_count += 1"""

name = input("Имя должника? ")
summa = int(input("Сумма долга? "))
while summa > 0:
    repay = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
    summa -= repay
    if summa > 0:
        print("Маловато,", name + ".",  "Давайте ещё раз")
print("Отлично,", name + "!", "Вы погасили долг. Спасибо!")