"""
numbers = int(input("Введите количество чисел: "))
for number in range(1, numbers + 1, 2):
    print("Число", number," ** 3 равно", number ** 3)

numbers = int(input("Введите число: "))
summ = 0
for number in range(1, numbers + 1, 5):
    summ += number
    print("Номер стула", number)
print("Сумма:", summ)
"""
wake_up = int(input("Введите час пробуждения: "))
water_volum = 0
calories = 0
for hour in range(wake_up, 23, 3):
    water_volum += 1
    calories += int(input("Сколько калориев съел? "))
    print("Прошло:", hour, "часов")
print("Всего выпито воды:", water_volum)
print("Всего съедно калориев:", calories)
