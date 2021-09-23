"""
seconds = int(input("Введите количество секунд: "))
for second in range(seconds, 0, -1):
    print(second)
print("Я иду искать!")

soldiers = int(input("Ведите количество солдат: "))
rules_count = int(input("Введите количество правил: "))
push_up = 0
for soldier in range(soldiers - 4, -1, -4):
    print(soldier, "-й солдат")
    if int(input("Сколько првил в уставе: ")) != rules_count:
        push_up += soldier * 10
print("Всего отжиманий:", push_up)
"""

seconds = int(input("Введите количество секунд: "))
for second in range(seconds - seconds % 2, 0, -2):
    print(second)
print("Я иду искать!")
