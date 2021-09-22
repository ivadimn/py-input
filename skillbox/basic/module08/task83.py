numbers = int(input("Введите количество чисел "))
for number in range(numbers // 2):
    n = number * 2 + 1
    print("Число", n, " ** 3 равно", n ** 3)