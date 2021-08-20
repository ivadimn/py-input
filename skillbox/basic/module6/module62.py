"""number = int(input("Введите число: "))
summ = 0
while number != 0:
 summ += number
 number = int(input("Введите число: "))
print(summ)"""

password = int(input("Введите пароль: "))
while password != 235:
 print("Неверный пароль!")
 password = int(input("Попробуйте ещё раз: "))
print("Пароль верный!, Добро пожаловать!")

summ = 0
while summ < 500000:
 summ += int(input("Сколько положить денег: "))
print("Вы накопили", summ)