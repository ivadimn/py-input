"""count = 10
while count > -2:
    if count < 0:
        print('Время вышло!')
    else:
        print(count)
    count -= 1"""

"""while True:
    is_working = int(input("Продолжаем работать? 1/0: "))
    if is_working == 0:
        print("Приложение закрывается…")
        break
    print("Программа работает...")
print("Работа завершена!")"""

while True:
    print("Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!")
    code = input("Введите код: ")
    if code == "0550":
        print("Код верный, завершаю работу...")
        break