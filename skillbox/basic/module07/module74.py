for number in range(1, 11):
    print(number ** 3)
"""
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
summ = 0
for number in range(first_number, second_number + 1):
    summ += number
print("Сумма чисел от", first_number, "до", second_number, " = ", summ)
"""
wake_up = int(input("Когда Саша проснулся? "))
awake_hours = 0
all_callories = 0
for hour in range(wake_up, 23):
    print(hour, "часов")
    callories = int(input("Сколько Саша съел калориев? "))
    all_callories += callories
    if all_callories > 2000:
        break
    awake_hours += 1
print("Всего съел калориев:", all_callories)
print("Оставался бодрым:", awake_hours, "часов")
