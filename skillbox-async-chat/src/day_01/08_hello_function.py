"""
Пример программы для работы с функциями

Сделать
- функцию hello, которая выводит текст приветствия клиенту
"""


def hello(client):
    print(f"Hello, {client}")


clients = ['John', 'David', 'Kate', 'Alex']
for client in clients:
    hello(client)
