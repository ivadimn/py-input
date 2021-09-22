"""
for meters in 100,90,95,87,102:
    if meters % 3 == 0:
        print(meters, 'Подходит')
    else:
        print(meters, 'Не подходит')

for number in 3,7,5,6,4:
    print(number ** 2, number ** 3, number ** 4)
"""
winners = 0
for ticket in 345,19,87,1020,421,555:
    if 99 < ticket < 1000 and ticket % 5 == 0:
        print(ticket, "- выигрфшный билет")
        winners += 1
print("Количество выигрышных билетов: ", winners)
