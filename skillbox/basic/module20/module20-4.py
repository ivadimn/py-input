"""
incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
for name, price in incomes.items():
    print("{0} -- {1}".format(name, price))
"""

server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for key, val in server_data.items():
    print("{0}:".format(key))
    for key1, val1 in val.items():
        print("\t{0}: {1}".format(key1, val1))


print([val for key, val in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if key % 2 == 0])