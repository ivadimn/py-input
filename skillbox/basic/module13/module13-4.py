"""
budget = float(input("Введите бюджет страны: "))
nalog = float(input("Новые поступления (налог): "))
new_budget = budget + nalog
if abs(new_budget - budget) < 1e-15:
    print("Результат: Бюджет не изменится")
else:
    print("Результат: Бюджет увеличится")
"""

def equv(a, b, c):
    d = a + b
    if abs(d - c) < 1e-15:
        return True
    else:
        return False

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

print(equv(a, b, c))