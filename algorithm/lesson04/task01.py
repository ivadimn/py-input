from collections import namedtuple

prop = ["name", "income"]
Factory = namedtuple("Factory", prop)


def average_income(fs: list) -> float:
    a_summa = 0
    for f in fs:
        a_summa += f.income
    a_summa /= len(fs)
    return a_summa


factorys = []
count = int(input("Введите количество предприятий : "))
for i in range(count):
    name = input(f"Введите наименование {i + 1}-го предприятия : ")
    income = list(map(int, input("Введите прибыль за каждый квартал через пробел : ").split()))
    factorys.append(Factory(name, sum(income)))

summa = average_income(factorys)
print(f"Средняя прибыль за года по всем предприятиям = {summa}")
for f in factorys:
    if f.income > summa:
        print(f"У предприятия {f.name} прибыль = {f.income} выше средней ")
    else:
        print(f"У предприятия {f.name} прибыль = {f.income} ниже средней ")


