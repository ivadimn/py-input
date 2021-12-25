"""
def print_num(num):
    if num == 1:
        print(num)
        return
    print_num(num - 1)
    print(num)


num = int(input("Введите num: "))
print_num(num)

def zip_1(*args):
    min_len = len(sorted(args, key=len)[0])
    return (tuple(list(arg)[l] for arg in args) for l in range(min_len))


dict1 = {"Alex": 20, "Mike": 30, "Ann": 18, "Pete": 50}
nums1 = [1, 2, 3, 90]
nums2 = (0, 2, 3, 8, 10)
line = "any line"
zip_gen = zip_1(nums1, dict1, nums2, line)
print(zip_gen)
print(list(zip_gen))


def fib1(pos):
    f_val1 = f_val2 = 1
    for _ in range(2, pos):
        f_val1, f_val2 = f_val2, f_val1 + f_val2
    return  f_val2


def fib2(pos):
    if pos in (1, 2):
        return 1
    return fib2(pos - 1) + fib2(pos - 2)


pos = int(input("Введите позицию числа в ряде Фибоначчи: "))
print("Число:", fib1(pos))


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

import sys
def find_key(d, key, deep = sys.getrecursionlimit()):
    if deep == 0:
        return None
    if key in d:
        return d[key]
    if isinstance(d, dict):
        for val in d.values():
            result = find_key(val, key, deep - 1)
    else:
        result = None
    return result

key = input("Введите искомый ключ: ")
if input("Хотите ввести максимальную глубину? Y/N: ").lower() == "y":
    deep = int(input("Введите максимальную глубину: "))
    result = find_key(site, key, deep)
else:
    result = find_key(site, key)
print("Значение ключа:", result)


def calculating_math_func(data, vals = dict()):
    if data in vals:
        return vals[data]
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    vals[data] = result ** 10
    print("Calculated")
    return vals[data]

print(calculating_math_func(10))
print(calculating_math_func(20))
print(calculating_math_func(10))
print(calculating_math_func(20))


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

def site_copy(d : dict, client: str):
    d_copy = dict()
    for key, val in d.items():
        if isinstance(val, dict):
            d_copy[key] = site_copy(val, client)
        else:
            if key == "title":
                val = "Куплю/продам {0} недорого".format(client)
            elif key == "h2":
                val = "У нас самая низкая цена на {0}".format(client)
            d_copy[key] = val

    return d_copy

def site_print(k: str, d: dict, deep = 0):
    if deep == 0:
        print("{0}{1} = {2}".format("\t" * deep, k, "{"))
    else:
        print("{0}'{1}' : {2}".format("\t" * deep, k, "{"))
    for key, val in d.items():
        if isinstance(val, dict):
            site_print(key, val, deep + 1)
        else:
            print("{0}'{1}' : {2}".format("\t" * (deep + 1), key, val))
    print("{0}{1}".format("\t" * deep, "}"))


def sites_print(sites: dict):
    for key, val in sites.items():
        print("Сайт для {0}:".format(key))
        site_print("site", val)


site_count = int(input("Сколько сайтов: "))
sites = dict()
for i_site in range(site_count):
    site_name = input("Введите название продукта для нового сайта: ")
    sites[site_name] = site_copy(site, site_name)
    sites_print(sites)
    print()

def sum(*args):
    summa = 0
    for arg in args:
        if isinstance(arg, list):
            summa += sum(*arg)
        else:
            summa += arg
    return summa



print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))


def line_list(lst: list):
    llst = list()
    for elem in lst:
        if isinstance(elem, list):
            llst.extend(line_list(elem))
        else:
            llst.append(elem)
    return llst



nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(line_list(nice_list))
"""

def move(n, frm, to):
    if n == 1:
        print("Переложить диск {0} со стержня номер {1} на стержень номер {2}".format(n, frm, to))
    else:
        tmp = 6 - frm - to
        move(n - 1, frm, tmp)
        print("Переложить диск {0} со стержня номер {1} на стержень номер {2}".format(n, frm, to))
        move(n - 1, tmp, to)

nums = int(input("Введите количество дисков: "))
move(nums, 1, 3)