"""
num = int(input("Введите целое число: "))
quarts = {n : n ** 2 for n in range(1, num + 1)}
print(quarts)


student_info = input("ведите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки):\n").split()
student = dict()
student["Имя"] = student_info[0]
student["Фамилмя"] = student_info[1]
student["Город"] = student_info[2]
student["Место учёбы"] = student_info[3]
student["Оценки"] = student_info[4:]
for k,v in student.items():
    print(k,":", v )
"""

contacts = dict()
def input_name():
    name = input("Введите имя ('finish' - для завершения): ")
    while name in contacts:
        print("Ошибка: такое имя уже существует.")
        name = input("Попробуйте ещё раз: ")
    return name

def print_contacts():
    print("Текущие контакты на телефоне:")
    for k, v in contacts.items():
        print(k, ":", v)
    print()

while True:
    print_contacts()
    name = input_name()
    phone = int(input("Введите номер телефона: "))
    if name == "finish":
        break
    contacts[name] = phone

