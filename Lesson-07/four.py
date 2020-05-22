def number2(x):
    result = "Ошибка, введите число от 1 до 100"
    while "квадрат" not in result:
        try:
            x = int(x)
            if 0 < x < 100:
                if x == 13:
                    raise ValueError()
                else:
                    x = x ** 2
                    result = f"квадрат = {x}"
                    return result
            else:
                print(result)
                x = input("Введите число: ")
        except (ValueError, TypeError):
            print(result)
            x = input("Введите число: ")


number = input("Введите число: ")
print(number2(number))