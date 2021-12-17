"""
violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count_songs = int(input("Сколько песен выбрать? "))
total_duration = 0
for i in range(1, count_songs + 1):
    song = input("Название {0} песни: ".format(i))
    total_duration += violator_songs.get(song, 0)

print("Общее время звучания песен {0:.2f} минут".format(total_duration))


count_countries = int(input("Кол-во стран: "))
countries = dict()
for i in range(1, count_countries + 1):
    country = input("{0} страна: ".format(i)).split()
    countries.update({city : country[0] for city in country[1:]})

for i in range(1, 4):
    city = input("{} город: ".format(i))
    print("Город {0} расположен в стране {1}.".format(city, countries.get(city, "")))


data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

def print_dict(d, count_tab):
    print()
    for k, v in d.items():
        print("\t" * count_tab, end = "")
        print("Ключ-{0}: значение-{1}".format(k, v))
        if isinstance(v, dict):
            print_dict(v, count_tab + 1)
        elif isinstance(v, list):
            print_list(v, count_tab + 1)


def print_list(l, count_tab):
    print()
    for li in l:
        print("\t" * count_tab, li)
        if isinstance(li, dict):
            print_dict(li, count_tab + 1)
        elif isinstance(li, list):
            print_list(li, count_tab + 1)



# Вывести списки ключей и значений словаря.
print("Cписки ключей и значений словаря:")
print_dict(data, 0)

# В “ETH” добавить ключ “total_diff” со значением 100.
data["ETH"]["total_diff"] = 100
print("\n", data["ETH"])

# Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
data["tokens"][0]["fst_token_info"]["name"] = "doge"
print("\n", data["tokens"][0]["fst_token_info"])

#Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
print()
total_out = 0
for token in data.get("tokens", []):
    total_out = token.pop("total_out", 0)
    print(token)
data["ETH"]["totalOut"] = total_out

#Внутри "sec_token_info" изменить название ключа “price” на “total_price”
print()
sec_token_info = data["tokens"][1].get("sec_token_info")
price = sec_token_info.pop("price", False)
sec_token_info.update({"total_price": price})
print(sec_token_info)


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for name, code in goods.items():
    summ = 0
    total_count = 0
    for good in  store.get(code, []):
        count = good.get("quantity", 0)
        summ += good.get("price", 0) * count
        total_count += count
    print("{0} - {1} шт, стоимость {2} руб".format(name, total_count, summ))


def print_dict(d : dict):
    for k, v in d.items():
        print("{0} : {1}".format(k, v))


def invers_dict(d: dict):
    return { key : [k for k, v in d.items() if v == key]  for key in set(d.values())}


text = input("Введите текст: ")
frequency_dict = {ch : text.count(ch) for ch in sorted(set(text))}
print("Оригинальный словарь частот:")
print_dict(frequency_dict)
print("Инвертированный словарь частот:")
print_dict(invers_dict(frequency_dict))


def get_synonym(d: dict, w: str):
    for k, v in d.items():
        if w.lower() == k.lower():
            return v
        elif w.lower() == v.lower():
            return k
    return ""

count = int(input("Введите количество пар слов: "))
synonym_dict = dict()
for i in range(1, count + 1):
    pair = input("{0} пара: ".format(i)).split("-")
    synonym_dict[pair[0]] = pair[1]

while True:
    word = input("Введите слово: ")
    synonym = get_synonym(synonym_dict, word)
    if synonym == "":
        print("Такого слова в словаре нет.")
    else:
        print("Синоним: {0}".format(synonym))
        break


def print_dict(d : dict):
    for k, v in d.items():
        print("{0}:".format(k))
        for kp, count in d.get(k).items():
            print("\t{0}: {1}".format(kp, count))


count = int(input("Введите кол-во заказов: "))
orders = dict()
for i in range(1, count + 1):
    pizza = input("{0} заказ: ".format(i)).split()
    if pizza[0] in orders:
        if pizza[1] in orders[pizza[0]]:
            count = orders[pizza[0]][pizza[1]]
            orders[pizza[0]][pizza[1]] = count + int(pizza[2])
        else:
            orders[pizza[0]][pizza[1]] = int(pizza[2])
    else:
        orders[pizza[0]] = {pizza[1]: int(pizza[2])}
print_dict(orders)


max_num = int(input("Введите максимальное число: "))
probable_nums = set()
while True:
    nums = input("Нужное число есть среди вот этих чисел: ")
    if nums.lower() == "помогите":
        print("Артём мог загадать следующие числа: {0} ", " ".join(map(str, probable_nums)))
        break
    nums_set = {n for n in set(map(int, nums.split())) if n <= max_num}
    answer = input("Ответ Артёма: ")
    if answer.lower() == "да":
        if len(nums_set) == 1:
            print("Вы угадали!")
            break
        probable_nums = probable_nums.union(nums_set)
    elif answer.lower() == "нет":
        probable_nums = probable_nums - probable_nums.intersection(nums_set)
    if len(probable_nums) == 1:
        print("Артём загадал число: {0}".format(list(probable_nums)[0]))
        break
    print(probable_nums)

def print_dict(d: dict):
    for k in sorted(d):
        print("{0} {1}".format(k, d[k]))


count_people = int(input("Введите количество человек: "))
genealog_tree = dict()
for i in range(count_people - 1):
    pair = input("{0} пара: ".format(i + 1)).split()
    if len(genealog_tree) == 0:
        genealog_tree[pair[1]] =  0
        genealog_tree[pair[0]] = 1
    else:
        if pair[1] not in genealog_tree:
            print("Нет родителя с именем {0}".format(pair[1]))
        else:
            height = genealog_tree.get(pair[1])
            genealog_tree[pair[0]] = height + 1
    print(genealog_tree)
print_dict(genealog_tree)
"""

def is_can_palindrom(ft : dict, lw : int):
    can = False
    evens = [1 if v % 2 == 0 else 0 for v in ft.values()]
    if lw % 2 == 0:
        can = sum(evens) == len(ft)
    else:
        can = sum(evens) == (len(ft) - 1)
    return can


line = input("Введите строку: ")
freq_table = {ch : line.count(ch) for ch in sorted(set(line))}
is_palindrom = is_can_palindrom(freq_table, len(line))
if is_palindrom:
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")






