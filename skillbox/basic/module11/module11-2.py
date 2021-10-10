"""
stavka = float(input("Ваша ставка: "))
koeff = float(input("Какой коэффициент: "))
print("Потенциальный выигрыш: ", round(stavka * koeff, 2))


age = int(input("Возраст сына: "))
temperature = float(input("Температура тела: "))
print("Отец подарит сыну: ", round(age * temperature * 1.5, 2))
"""

weight = float(input("Введите ваш вес: "))
lenght = float(input("Введите ваш рост: "))
bmi = round(weight / (lenght ** 2), 2)
print("Ваш  индекс массы тела:", bmi)
if bmi < 18.5:
    print("У вас недобор")
elif bmi < 25:
    print("У вса всё нормально")
elif bmi < 30:
    print("У вас избыточный вес")
else:
    print("У вас ожирение")





