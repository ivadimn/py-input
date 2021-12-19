data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

def get_name(s: int , num: int):
    f_name, s_name = data.get((s, num), ())
    return f_name, s_name

f_name, s_name = get_name(6000, 111111)
print(f_name, s_name)

phone_book = dict()
while True:
    print(phone_book)
    phone = input("Введите Фамилия Имя и номер телефона через пробел: ").split()
    phone_book[(phone[0], phone[1])] = phone[2]
