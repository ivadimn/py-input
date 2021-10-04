"""
for row in range(20):
    for col in range(30):
        if row == 0:
            print("-", end = "")
        elif (col == 0) or (col == 29):
            print("|", end = "")
        else:
            print(" ", end = "")
    print()


for row in range(20):
    for col in range(50):
        if row == 9:
            print("-", end = "")
        elif col == row + 29:
            print("\\", end = "")
        elif col == -row + 19:
            print("/", end = "")
        elif col == 24:
            print("|", end = "")
        else:
            print(" ", end = "")
    print()
"""

size = int(input("Введите размер матрицы: "))
for row in range(size):
    for col in range(size):
        if col < size - row - 1:
            print(0, end = " ")
        elif col > size - row- 1:
            print(2, end = " ")
        else:
            print(1, end = " ")
    print()