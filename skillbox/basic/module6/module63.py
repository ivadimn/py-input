"""weather = int(input("Введите температуру воздуха: "))
path = 0
while weather > 15:
    path += 20
    weather -=2
    if weather <= 15:
        break
    path += 10
print("Полный путь: ", path)"""


"""number = int(input("Введите число: "))
summ = 0
while number != 0:
    last_digit = number % 10
    if last_digit == 5:
        print("Обнаружен разрыв")
        break
    summ += last_digit
    number //= 10
print(summ)"""

summa = int(input("Введите стартовую сумму: "))
while summa < 10000:
    number = int(input("Сколько выпало на кубике? "))
    if number == 3:
        summa = 0
        print("Вы проиграли всё!")
        break
    print("Вы выиграли 500 рублей")
    summa += 500
print("Игра закончилась!")
print("Итого осталось: ", summa)
