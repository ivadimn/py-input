"""
size = 6
for row in range(size):
    for col in range(size):
        print(row + col * 2 , end = "\t")
    print()


number = int(input("Введите число: "))
for row in range(1, number + 1):
    for col in range(1, row + 1):
        print(row, end = " ")
    print()


width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))
for row in range(height):
    for col in range(width):
        if ((row == 0) or (row == height - 1)) and (0 < col < width - 1):
            print("-", end = "")
        elif (col == 0) or (col == width - 1):
            print("|", end="")
        else:
            print(" ", end = "")
    print()


size = int(input("Введите размер: "))
for row in range(size):
    for col in range(size):
        if (row == col) or (col == size - row - 1):
            print("^", end = "")
        else:
            print(" ", end="")
    print()


seq_count = int(input("Введите количество чисел в последовательности: "))
simple_count = 0
for n in range(1, seq_count + 1):
    print("Введите", n, "-е число последовательности: ", end = "" )
    number = int(input())
    for d in range(2, number):
        if number % d == 0:
            break
    else:
        if number > 1:
            simple_count += 1
print("Количество простых чисел в последовательности: ", simple_count)


numbers_count = int(input("Введите число: "))
summ_factorial = 1
for number in range(2, numbers_count + 1):
    factorial = 1
    for n in range(2, number + 1):
        factorial *= n
    summ_factorial += factorial
print("Сумма факториалов чисел от 1 до", numbers_count, "равна", summ_factorial)


seq_count = int(input("Введите количество чисел в последовательности: "))
max_summa = 0
max_number = 0
for n in range(1, seq_count + 1):
    summ_digits = 0
    print("Введите", n, "-е число последовательности: ", end="")
    number = int(input())
    n = number
    while n > 0:
        summ_digits += n % 10
        n //= 10
    if summ_digits > max_summa:
        max_summa = summ_digits
        max_number = number
print("Число", max_number, "имеет максимальную сумму цифр: ", max_summa)


height = int(input("Введите высоту пирамиды: "))
width = height * 2 - 1
for row in range(1, height + 1):
    w = row * 2 - 1
    bound_left = (width - w) // 2
    for col in range(1, width + 1):
        if (col > bound_left) and (col < bound_left + w + 1):
           print("#", end = "")
        else:
           print(" ", end = "")
    print()
"""

levels = int(input("Введите количество уровней: "))
width = levels * 2
number = 1

for row in range(1, levels + 1):
    prs = 0
    spos = levels - row
    for col in range(width):
        if (col == spos) and (prs < row):
           print(number, end = "")
           number += 2
           prs += 1
           spos += 2
        else:
            print(" ", end="")
    print()


number = int(input("Введите число: "))
width = number * 2
for row in range(number):
    for col in range(width):
        if (col <= row):
           print(number - col, end = "")
        elif col >= width - row - 1:
           print(col - number + 1, end = "")
        else:
            print(".", end="")
    print()
