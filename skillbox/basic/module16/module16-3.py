"""
main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]

main.extend(first_company)
main.extend(second_company)
main.extend(third_company)

print("Общий список задач:", main)
print("Кол-во невыполненных задач:", main.count(0))


message1 = input("Первое сообщение: ")
message2 = input("Второе сообщение: ")

list_ch1 = list(message1)
list_ch2 = list(message2)
count_spec1 = list_ch1.count("!") + list_ch1.count("?")
count_spec2 = list_ch2.count("!") + list_ch2.count("?")
if count_spec1 > count_spec2:
    print(message1, message2)
elif count_spec1 < count_spec2:
    print(message2, message1)
else:
    print("Ой!")
"""

pack = []
decode = []
bad_pack_count = 0
pack_count = int(input("Кол-во пакетов: "))
for i_pack in range(pack_count):
    print("Пакет номер", i_pack + 1)
    for i_bit in range(4):
        print(i_bit + 1, "бит: ", end = "")
        pack.append(int(input()))
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print("Много ошибок в пакете.")
        bad_pack_count += 1
    pack.clear()
print("Полученное сообщение:", decode)
print("Кол-во ошибок в сообщении:", decode.count(-1))
print("Кол-во потепянных пакетов:", bad_pack_count)


