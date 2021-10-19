import random
"""
def summa_n(number):
    summ = 0
    for n in range(1, number + 1):
        summ += n
    print("Я знаю, что сумма чисел от 1 до",  number, "равна", summ)

number = int(input("Введите число: "))
summa_n(number)


def test():
    number = int(input("Введите целое число: "))
    if number > 0:
        positive()
    elif number < 0:
        negative()
    else:
        zero()

def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

def zero():
    print("Ноль")

test()

def summa_digits(number):
    n = number
    summ = 0
    while n > 0:
        summ += (n % 10)
        n //= 10
    print("Сумма цифр числа" , number, "равна:", summ)

def max_digit(number):
    n = number
    max = 0
    while n > 0:
        d = (n % 10)
        if d > max:
            max = d
        n //= 10
    print("Максимальная цифра числа", number, "равна:", max)

def min_digit(number):
    n = number
    min = 9
    while n > 0:
        d = (n % 10)
        if d < min:
            min = d
        n //= 10
    print("Минимальная цифра числа", number, "равна:", min)

number = int(input("Введите целое положительное число: "))
print("Выберите что нужно сделать с эти числом:")
print("1. Вывести сумму его цифр.")
print("2. Вывести максимальную цифру.")
print("3. Вывести мимнимальную цифру.")
choice = int(input())
if choice == 1:
    summa_digits(number)
elif choice == 2:
    max_digit(number)
elif choice == 3:
    min_digit(number)
else:
    print("Не правильный выбор, необходимо ввести 1, 2 или 3")


def invers(number):
    n = 0
    while number > 0:
        d = number % 10
        number //= 10
        n *= 10
        n += d
    print("Число наоборот: ", n)

while True:
    number = int(input("Введите число или 0 для завершения: "))
    if number == 0:
        break
    else:
        invers(number)
print("Программа завершена!")



def count_letters(text, letter, digit):
    count_letter = 0
    count_digit = 0
    for l in text:
        if l == letter:
            count_letter += 1
        elif l == digit:
            count_digit += 1
    print("Количество цифр", digit, ":", count_digit)
    print("Количество букв", letter, ":", count_letter)

text = input("Введите текст: ")
digit = input("Какую цифру ищем? ")
letter = input("Какую букву ищем? ")
count_letters(text, letter, digit)


def is_in_bounds(x, y):
    if (-1 <= x <= 1) and (-1 <= y <= 1):
        print("Монетка где то рядом.")
    else:
        print("Монетки в области нет.")

x = float(input("Введите число x: "))
y = float(input("Введите число y: "))
is_in_bounds(x, y)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
min = ((a + b) - abs(a - b)) / 2
print(int(min))


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    print(a + b)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
nod(a, b)
"""

def rock_paper_scissors():
    word = input("Введите строку: ")
    n = random.randint(1, 3)
    if n == 1:    # у компьютера камень
        if word.lower() == "ножницы":
            print("Вы проиграли, у компьютера КАМЕНЬ!")
        elif word.lower() == "бумага":
            print("Вы выиграли, у компьютера КАМЕНЬ!")
        elif word.lower() == "камень":
            print("Ничья, у компьютера тоже КАМЕНЬ!")
        else:
            print("Ошибка, необходимо ввести камень, ножницы или бумага")
    elif n == 2: # у компьютера ножницы
        if word.lower() == "бумага":
            print("Вы проиграли, у компьютера НОЖНИЦЫ!")
        elif word.lower() == "камень":
            print("Вы выиграли, у компьютера НОЖНИЦЫ!")
        elif word.lower() == "ножницы":
            print("Ничья, у компьютера тоже НОЖНИЦЫ!")
        else:
            print("Ошибка, необходимо ввести камень, ножницы или бумага")
    else:  # у компьютера бумага
        if word.lower() == "камень":
            print("Вы проиграли, у компьютера БУМАГА!")
        elif word.lower() == "ножницы":
            print("Вы выиграли, у компьютера БУМАГА!")
        elif word.lower() == "бумага":
            print("Ничья, у компьютера тоже БУМАГА!")
        else:
            print("Ошибка, необходимо ввести камень, ножницы или бумага")
    mainMenu()

def guess_the_number():
    comp_number = random.randint(1, 10)
    while True:
        number = int(input("Введите число от 1 до 10: "))
        if number == comp_number:
            print("Поздравляю вы верно угадала число: ", number)
            break
        else:
            print("Сожалею вы не угадали, попытайтесь ещё раз!")
    mainMenu()

def mainMenu():
    print("\nВыберите игру в которую будем играть.")
    print("1. Камень, ножницы, бумага!")
    print("2. Угадай число!")
    print("3. Выход!")
    game = int(input())
    if game == 1:
        rock_paper_scissors()
    elif game == 2:
        guess_the_number()
    elif game != 3:
        print("Не правильный выбор...")
        mainMenu()

mainMenu()


def inBedroom():
    print("Вы в спальне. Куда идём?")
    print("1 - в ванну")
    print("2 - в коридор")
    where = int(input())
    if where == 1:
        inBathroom()
    elif where == 2:
        inHall()
    else:
        print("Такого направления нет!")
        inBedroom()

def inKitchen():
    print("Вы в кухне. Куда идём?")
    print("1 - в коридор")
    print("2 - в окно")
    where = int(input())
    if where == 1:
        inHall()
    elif where == 2:
        print("Вы упали и разбились!")
    else:
        print("Такого направления нет!")
        inKitchen()


def inHall():
    print("Вы в коридоре. Куда идём?")
    print("1 - в спальню")
    print("2 - в ванну")
    print("3 - на кухню")
    print("4 - в дверь")
    where = int(input())
    if where == 1:
        inBedroom()
    elif where == 2:
        inBathroom()
    elif where == 3:
        inKitchen()
    elif where == 4:
        print("Вы покинули квартиру!")
    else:
        print("Такого направления нет!")
        inHall()

def inBathroom():
    print("Вы в ванне. Куда идём?")
    print("1 - в коридор")
    print("2 - в спальню")
    where = int(input())
    if where == 1:
        inHall()
    elif where == 2:
        inBedroom()
    else:
        print("Такого направления нет!")
        inBathroom()

def mainMenu():
     n = random.randint(1, 4)
     if n == 1:
         inBedroom()
     elif n == 2:
         inBathroom()
     elif n == 3:
         inKitchen()
     else:
         inHall()

mainMenu()