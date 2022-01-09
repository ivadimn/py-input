"""
def write_error_log(error : str):
    with open("errors.log", "a") as log_file:
        log_file.write("{}\n".format(error))


def get_len(word: str):
    length = len(word)
    if length < 3:
        raise BaseException("В строке {0} встретилось слишком короткое имя - {1}".format(index + 1, line))
    return length


sym_count = 0
try:
    with open("people.txt", "r") as file:
        for index, line in enumerate(file):
            if line.endswith("\n"):
                line = line[:-1]
            try:
                sym_count += get_len(line)
            except BaseException as be:
                print(be.args[0])
                write_error_log(be.args[0])
except FileNotFoundError:
    print("Файл не найден ... ")
finally:
    print("Найденная сумма символов = {0}".format(sym_count))


import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    if y == 0:
        raise ZeroDivisionError("в функции 'f' деление на 0")
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    if x == 0:
        raise ZeroDivisionError("в функции 'f2' деление на 0")
    return y / x


try:
    with open('coordinates.txt', 'r') as file:
        with open('result.txt', 'w') as file_2:
            for line in file:
                nums_list = line.split()
                try:
                    res1 = f(int(nums_list[0]), int(nums_list[1]))
                    res2 = f2(int(nums_list[0]), int(nums_list[1]))
                    number = random.randint(0, 100)
                    my_list = sorted([res1, res2, number])
                    s = ' '.join([str(elem) for elem in my_list])
                    print(s)
                    file_2.write("{}\n".format(s))
                except Exception as ex:
                    print("Что-то пошло не так - {0}".format(ex.args[0]))
                    file_2.write("Что-то пошло не так - {0}\n".format(s))
except FileNotFoundError:
    print("Файл не найден....")

import random


summa = 0
lst = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
with open("numbers.txt", "w") as file:
    while summa < 777:
        try:
           number = int(input("Введите целое число: "))
           if lst[random.randint(0, 12)]:
                raise Exception("Произошла ошибка, программа завершена.")
           file.write("{0}\n".format(number))
           summa += number
        except ValueError:
            print("Введено не целое число...")
    print("Вы успешно выполнили условие для выхода из порочного цикла!")



def validate_data(data: str):
    lst_data = data.split()
    if len(lst_data) < 3:
        raise IndexError("НЕ присутствуют все три поля.")
    if not lst_data[0].isalpha():
        raise NameError("Поле имени содержит НЕ только буквы.")
    if not ("@" in lst_data[1] and "." in lst_data[1]):
        raise SyntaxError("Поле «Имейл» НЕ содержит @ и .(точку).")
    if lst_data[2].isdigit():
        if not (10 <= int(lst_data[2]) <= 99):
            raise ValueError("Поле «Возраст» НЕ является числом от 10 до 99")
    else:
        raise ValueError("Поле «Возраст» НЕ является числом")
    return True


try:
    with open("registrations.txt", "r") as f_data, open("registrations_good.log", "w") as f_good, \
        open("registrations_bad.log", "w") as f_bad:
        for i, data in enumerate(f_data):
            if data.endswith("\n"):
                data = data[:-1]
            try:
                validate_data(data)
                f_good.write("{0}\n".format(data))
            except Exception as ex:
                err = "В строке {0} ошибка - {1}".format(i + 1, ex.args[0])
                print(err)
                f_bad.write("{0}\n".format(err))
except FileNotFoundError:
    print("Файл не найден....")



def cal(oper: str):
    result = 0
    opers = oper.split()
    if len(opers) < 3:
        raise IndexError("Не достаточно данных для вычисления.")
    try:
        op1 = int(opers[0])
        op2 = int(opers[2])
        if opers[1] == "+":
            result = op1 + op2
        elif opers[1] == "-":
            result = op1 - op2
        elif opers[1] == "*":
            result = op1 * op2
        elif opers[1] == "/":
            if op2 == 0:
                raise ZeroDivisionError("Деление на 0 - ({0} / {1})".format(op1, op2))
            result = op1 / op2
        elif opers[1] == "//":
            if op2 == 0:
                raise ZeroDivisionError("Деление на 0 - {0} // {1}".format(op1, op2))
            result = op1 // op2
        elif opers[1] == "**":
            result = op1 ** op2
        elif opers[1] == "%":
            result = op1 % op2
        else:
            raise NameError("Неправильная операция - {0}".format(opers[1]))
    except ValueError:
        raise ValueError("Один из операндов не является целым числом.")
    return result


summa = 0
try:
    with open("calc.txt", "r") as f_calc:
        for i, oper in enumerate(f_calc):
            if oper.endswith("\n"):
                oper = oper[:-1]
            try:
                summa += cal(oper)
            except Exception as ex:
                print("Произошла ошибка в строке {0} - {1}".format(i + 1, ex.args[0]))
        print("Результат вычислений = {0}".format(summa))
except FileNotFoundError:
    print("Файл не найден...")
"""


def cal(oper: str):
    result = 0
    opers = oper.split()
    if len(opers) < 3:
        raise IndexError
    try:
        op1 = int(opers[0])
        op2 = int(opers[2])
        if opers[1] == "+":
            result = op1 + op2
        elif opers[1] == "-":
            result = op1 - op2
        elif opers[1] == "*":
            result = op1 * op2
        elif opers[1] == "/":
            if op2 == 0:
                raise ZeroDivisionError
            result = op1 / op2
        elif opers[1] == "//":
            if op2 == 0:
                raise ZeroDivisionError
            result = op1 // op2
        elif opers[1] == "**":
            result = op1 ** op2
        elif opers[1] == "%":
            result = op1 % op2
        else:
            raise NameError
    except ValueError:
        raise ValueError
    return result


summa = 0
try:
    with open("calc.txt", "r") as f_calc:
        for i, oper in enumerate(f_calc):
            if oper.endswith("\n"):
                oper = oper[:-1]
            while True:
                try:
                    summa += cal(oper)
                    break
                except Exception:
                    answer = input("Обнаружена ошибка в строке: {0} Хотите исправить? ".format(oper))
                    if answer.lower() == "да":
                        oper = input("Введите исправленную строку: ")
                    else:
                        break
        print("Сумма результатов = {0}".format(summa))
except FileNotFoundError:
    print("Файл не найден...")