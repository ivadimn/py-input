"""
Пример программы для работы с функциями (аналог файла 01_hours_salary.py)

Аргументы
- стоимость часа в руб
- количество дней в руб

Сделать
- функцию, которая вернет размер зарплаты в руб
"""


def salary(cost: int, days: int):
    total = (days * 8) * cost
    return total - (total * .13)


cost_hour = 1200
print(salary(cost_hour, 5))
