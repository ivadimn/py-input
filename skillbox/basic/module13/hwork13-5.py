def get_num_count(number):
    num_count = 0
    while number > 0:
        num_count += 1
        number = number // 10
    return num_count

def change_digits(number, num_count):
    last_digit = number % 10
    first_digit = number // 10 ** (num_count - 1)
    between_digits = number % 10 ** (num_count - 1) // 10
    number = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit
    return number

def doWork(number1, number2):
    change_num1 = 0
    change_num2 = 0
    num_count = get_num_count(number1)
    if num_count < 3:
        print("В первом числе меньше трёх цифр.")
        return
    else:
        change_num1 = change_digits(number1, num_count)
        print("Изменённое первое число:", change_num1)

    num_count = get_num_count(number2)
    if num_count < 4:
        print("Во втором числе меньше четырёх цифр.")
        return
    else:
        change_num2 = change_digits(number2, num_count)
        print("Изменённое второе число:", change_num2)

    print("Сумма чисел:", change_num1 + change_num2)
first_n = int(input("Введите первое число: "))
second_n = int(input("Введите второе число: "))
doWork(first_n, second_n)