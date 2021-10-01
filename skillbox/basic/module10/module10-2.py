"""
size = int(input("Введите размер матрицы: " ))
for row in range(1, size + 1):
    for col in range(1, size + 1):
        if row % 2 == 0:
            print(row, end = " ")
        else:
            print(col, end = " ")
    print()


size = int(input("Введите размер матрицы: " ))
for row in range(1, size + 1):
    for col in range(1, size + 1):
        if col == 3:
            print(col, end = " ")
        elif (col == size) and (size % 2 == 0):
            print(size, end=" ")
        else:
            print(row, end=" ")
    print()
"""

for row in range(20):
    for col in range(50):
        if row == 9:
            print("-", end = "")
        elif col == 24:
            print("|", end = "")
        else:
            print(" ", end = "")
    print()