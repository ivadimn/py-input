"""
matrix = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]
for line in matrix:
    for elem in line:
        print(elem, end = " ")
    print()

l = [[n + i * 4 for n in range(1, 5)] for i in range(3) ]
print(l)
count_mans = int(input("Количество участников: "))
count_in_group = int(input("Кол-во человек в команде: "))
list_groups = []
if count_mans % count_in_group == 0:
    num = 1
    for _ in range(count_mans // count_in_group):
        group = []
        for i in range(count_in_group):
            group.append(num + i)
        list_groups.append(group)
        num += count_in_group
    print("Общий список команд:", list_groups)
else:
    print(count_mans, "участников невозможно поделить на команды по", count_in_group,
          "человек!")
"""

list_fruits = [["яблоки", 50], ["апельсины", 190], ["груши", 100],
               ["нектарины", 200], ["бананы", 77]]
print("Текущий ассортимент: ", list_fruits)

new_fruit = input("Новый фрукт: ")
price = int(input("Цена: "))

list_fruits.append([new_fruit, price])
print("Новый ассортимент: ", list_fruits)
for fruit in list_fruits:
    fruit[1] += fruit[1] * 0.08
print("Новый ассортимент с увел. ценой:", list_fruits)