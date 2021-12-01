"""
name = input("Имя: ")
order_num = int(input("Номер заказа: "))
welcom_message = f"Здравствуйте, {name}! Ваш номер заказа: {order_num}. Приятного дня!"
print(welcom_message.format(name = name, order_num = order_num))


name = input("Введите имя: ")
credit = int(input("Введите долг: "))
message = "{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}! "
print(message.format(name, credit))
"""
def get_ip_part():
    ip_part = int(input("Введите часть IP-адреса от 0 до 255: "))
    while not (0 <= ip_part <= 255):
        ip_part = int(input("Вы ошиблись попробуйте ещё раз от 0 до 255: "))
    return ip_part

ip_address = "{0}.{1}.{2}.{3}"
print("Введите IP - адрес")
parts_list = [get_ip_part() for _ in range(4)]
print(ip_address.format(parts_list[0], parts_list[1], parts_list[2], parts_list[3]))



