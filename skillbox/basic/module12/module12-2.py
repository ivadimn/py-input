"""
def greeting():
    print('Привет!')
    print('Добро пожаловать!')

while True:
    a = input('Зайдёте? Да/Нет: ')
    if a == 'Да':
        greeting()
    print('Следующий.\n')

def howMuch():
    a = int(input())
    b = int(input())
    print("Всего", a + b, "шт.")

print("Сколько мешков рыбы и мяса?")
howMuch()
print("Сколько буханок белого и чёрного хлеба?")
howMuch()
print("Сколько вёдер воды и молока?")
howMuch()
"""

first_name = "Иванов"
second_name = "Василий"
street = "Пушкина"
house = 32

def showData():
    print("Фамилия: ", first_name)
    print("Имя: ", second_name)
    print("Улица: ", street)
    print("Дом: ", house)
    print()

showData()
showData()
showData()
