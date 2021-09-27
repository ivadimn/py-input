"""
badGradeCount = 0
for student in range(5):
    answer = input("Кто написал Евгения Онегина? ")
    if (answer == "Пушкин") or (answer == "пушкин"):
        print("Правильно")
        break
    print("Неправильно! Два.")
    badGradeCount += 1
print("Количество двоек:", badGradeCount)


finish = "Да, конечно, сделал"
while True:
    answer = input("Ты выполнил задания, которые выданы вчера? ")
    if answer == finish:
        break
"""
name = input("Как тебя зовут?")
print(name + ", купи слона!")
answer = input()
while True:
    print("Все говорят " + answer, ", а ты купи слона!")
    answer = input()