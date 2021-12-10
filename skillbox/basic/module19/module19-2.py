"""
small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}
big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)
print(big_storage)

product = input("Введите наименование товара: ")
count = big_storage.get(product)
if count == None:
    print("Ошибка: такого товара нет")
else:
    print(product, ":", count)


incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
print("Общий доход за год составил", sum(incomes.values()), "рублей")
sorted_keys = sorted(incomes, key = incomes.get)
print("Самый маленький доход у", sorted_keys[0], ". Он составляет",  incomes[sorted_keys[0]],  "рублей")
"""

text = input("Введите текст: ")
frequency = {ch : text.count(ch) for ch in sorted(set(text))}
print(frequency)
