numbers = int(input("Введите количество чисел "))
for number in range(1, numbers // 2 + 1):
    n = number * 2
    print("Число", n, " ** 3 равно", n ** 3)