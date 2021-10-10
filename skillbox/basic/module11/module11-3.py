"""
chatls = int(input("Сколько чатлов: "))
cr = chatls / 2200
print("Это", cr, "CR")
print("Можно купить кораблей", int(cr / 0.5), "кораблей")


while True:
    print("Введите местополржение фигуры")
    x = float(input("По горизонтали: "))
    y = float(input("По вертикали: "))
    print("Фигура находится в клетке (", int(x * 10),",", int(y * 10), ")")
"""

while True:
    print("Введите местополржение фигуры")
    x = float(input("По горизонтали: "))
    y = float(input("По вертикали: "))
    cell_x = int(x * 10)
    cell_y = int(y * 10)
    delta_x = round((cell_x + 0.5) / 10 - x, 3)
    delta_y = round((cell_y + 0.5) / 10 - y, 3)
    print("Фигура находится в клетке (", cell_x,",", cell_y, ")")
    print("Поправьте положение фигуры на (", delta_x,",", delta_y, ")")