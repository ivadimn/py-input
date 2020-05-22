# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

size = 5
matrix = [[randint(1, 50) for _ in range(size)] for _ in range(size)]
min_columns = [0] * size
for j in range(size):
    min_in_column = matrix[0][j]
    for i in range(size):
        if matrix[i][j] < min_in_column:
            min_in_column = matrix[i][j]
        min_columns[j] = min_in_column

print("Полученная матрица :")
for line in matrix:
    for item in line:
        print(f"{item:>4}", end="")
    print()
print("Минимальные элементы столбцов")
print(min_columns)
max_item = min_columns[0]
for item in min_columns:
    if item > max_item:
        max_item = item
print(f"Среди них максимальный = {max_item}")