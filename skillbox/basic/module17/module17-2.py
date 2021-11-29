"""
left_bound = int(input("Левая граница: "))
right_bound = int(input("Правая граница: "))

cube_list = [n ** 3 for n in range(left_bound, right_bound + 1)]
squ_list = [n ** 2 for n in range(left_bound, right_bound + 1)]
print("Список кубов чисел в диапазоне от", left_bound, "до",  right_bound, ":", cube_list)
print("Список квадратов чисел в диапазоне от", left_bound, "до",  right_bound, ":",squ_list)


line = input("Введите строку: ")
symbol = input("Введите дополнительный символ: ")

first_list = [ch * 2 for ch in line]
second_list = [e + symbol for e in first_list]

print("Список удвоенных символов:", first_list)
print("Склейка с дополнительным символом:", second_list)
"""

def get_new_price(price, percent):
    return price * (1 + percent / 100)

list_price = [float(input("Цена на товар: ")) for _ in range(5)]
percent = int(input("Повышение на первый год: "))
list_first = [get_new_price(price, percent) for price in list_price]

percent = int(input("Повышение на второй год: "))
list_second = [get_new_price(price, percent) for price in list_first]

print("Сумма цен за каждый год:", round(sum(list_price), 2), round(sum(list_first), 2), round(sum(list_second), 2))