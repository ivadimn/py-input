"""
numbers = [3,7,5]
while True:
    number = int(input('Новое число: '))
    numbers.append(number)
    print('Текущий список чисел:', numbers)
    for i in numbers:
        print(i ** 2, i ** 3, i ** 4)
    print()


numbers = [n for n in range(101)]
print(numbers)
"""

persons = []
count_person = int(input("Кол-во сотрудников в офисе: "))
for _ in range(count_person):
    id = int(input("ID сотрудника: "))
    persons.append(id)
search_id = int(input("Какой ID ищем? "))
if search_id in persons:
    print("Сотрудник работает!")
else:
    print("Сотрудник не работает!")