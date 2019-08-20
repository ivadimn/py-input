numbers = [4, 8, 6, 7, 2, 0, -59, -47, -28, -45, 5679, - 3654, 9]
numbers2 = [number for number in numbers if number % 3 == 0 and number > 0
            and number % 4 != 0]

print(numbers2)