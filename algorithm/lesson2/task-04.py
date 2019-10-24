def get_number(s: str) -> int:
    while True:
        try:
            return int(input(s))
        except ValueError:
            print("Вы ввели не целое число!")
            continue

b1 = 1
q = -0.5
n = get_number("Введите количество элементов ряда : ")
summa = b1 * (1 - q ** n) / (1 - q)
print(f"Сумма {n} членов геометрической прогресси, где b1 = {b1} со знаменателем  {q} = {summa}")