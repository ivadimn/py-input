# 6. В программе генерируется случайное целое число от 0 до 100.
#  Пользователь должен его отгадать не более чем за 10 попыток.
#  После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
#  чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.

from random import randint


def get_number(s: str) -> int:
    while True:
        try:
            return int(input(s))
        except ValueError:
            print("Вы ввели не целое число!")
            continue


print("Компьютер загадал число от 0 до 100 Вам необходимо его угадать !!")
number = randint(0, 100)
delta = number
step = 1
while step <= 10:
    user_number = get_number("Введите число : ")
    delta = delta // 2 + delta % 2
    if user_number < number:
        user_number = user_number + delta
        print("Вы ввели число меньше загаданного")
    elif user_number > number:
        user_number = user_number - delta
        print("Вы ввели число больше загаданного")
    else:
        print(f"Вы угадали число {number} за {step} попыток")
        break
    step += 1
else:
    print("Вы не угадали за 10 попыток")


