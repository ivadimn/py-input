import random
"""
BRUCE_WILLIS = 42
input_data = input('Введите строку: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError:
    print("Значение не может быть преобразовано в целое число.")
except IndexError:
    print("Выход за границу строки.")
"""

names = ["Pete", "Vasiliy", "Elena", "Olga", "Jack", "Alex", "Anna", "Andrew", "Mike", "Nick"]

try:
    file = open("words.txt", "r")
    out_file = open("result.txt", "x")
    for line in file:
        try:
            out_line = "{0} - {1}\n".format(random.choice(names), int(line))
            out_file.write(out_line)
        except ValueError:
            print("Значение не может быть преобразовано в целое число.")
    out_file.close()
    file.close()

except IsADirectoryError:
    print("На чтение ожидался файл, но это оказалась директория.")
except FileExistsError:
    print("Выходной файл уже создан.")
