import os
import datetime


def get_chat_users():
    users = []
    if os.path.exists("chat_users.txt"):
        with open("chat_users.txt", "r") as file:
            users.extend([user[:-1] if user.endswith("\n") else user for user in file])
    return users


def register_user(user_name: str):
    with open("chat_users.txt", "a") as file:
        file.write("{0}\n".format(user_name))


def show_chat():
    print()
    print("*" * 10, "Содержание чата", "*" * 10)
    if os.path.exists("chat.txt"):
        with open("chat.txt", "r") as file:
            for msg in file:
                print(msg, end = "")
    else:
        print("Чат пока пустой!")
    print("-" * 40)

def send_message(user: str, msg: str):
    dt = datetime.datetime.now()
    dt_str = "{0}.{1}.{2} {3}:{4}".format(dt.day if dt.day > 9 else "0{}".format(dt.day),
                                          dt.month if dt.month > 9 else "0{}".format(dt.month),
                                          dt.year, dt.hour, dt.minute)
    with open("chat.txt", "a") as file:
        file.write("{0}, {1} - {2}\n".format(dt_str, user, msg))

def is_registered_user(user_name):
    is_registered = False
    if user_name not in users:
        answer = input("Вы не зарегистрированы. Желаете зарегистрироваться? ")
        if answer == "да":
            register_user(name)
            is_registered = True
    else:
        is_registered = True
    return is_registered

def print_menu():
    print("\n1. Посмотреть текущий текст чата.")
    print("2. Отправить сообщение...")


users = get_chat_users()
name = input("Здравствуйте, введите своё имя: ")
if is_registered_user(name):
    while True:
        print_menu()
        try:
            choice = int(input("Что будем делать? "))
            if choice == 1:
                show_chat()
            elif choice == 2:
                msg = input("Введите сообщение: ")
                if msg.lower() == "bye":
                    break
                send_message(name, msg)

        except ValueError:
            print("Неправильный выбор. Попробуйте ещё раз.")
print("До свидания {0}".format(name))

