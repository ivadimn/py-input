#В этой игре человек загадывает число, а компьютер пытается его угадать.
#В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.
# Компьютер начинает его отгадывать предлагая игроку варианты чисел.
# Если компьютер угадал число, игрок выбирает “победа”.
# Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”.
# Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”.
# Игра продолжается до тех пор пока компьютер не отгадает число.

print("Компьютер буде угадывать задуманное Вами число!!")
input("Задумайте чило от 1 до 100 и нажмите Enter ")
number = 50
delta = number
result = None
while result != "=":
    result = input("Ваше число {} если Ваше число больше введите '>' если меньше '<' если угадал '=' : ".format(number))
    delta = delta // 2 + delta % 2
    if result == ">":
        number = number + delta
    elif result == "<":
        number = number - delta
print("Компьютер угадал число {} ".format(number))
