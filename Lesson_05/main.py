# 3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.

import task01
from task02 import get_random_item, empty_items

main_items = [10, 20, 30, 40, 230, 890, 340, "12366", "84789", 2570]

task01.create_dirs()
#task01.delete_dirs()
print("Случайно выбранный элемент - ", get_random_item(main_items))
print("Случайно выбранный элемент - ", get_random_item(empty_items))
