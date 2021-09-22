#import task_1
#import task_2
#import task_3
#import task_4
#import task_5
#import task_6
#import task_7
#import task_8
#import task_9
#import task10
experience = int(input("Введите количество опыта: "))
if experience < 1000:
  print("Ваш уровень: ", 1)
elif experience < 2500:
  print("Ваш уровень: ", 2)
elif experience < 5000:
  print("Ваш уровень: ", 3)
else:
  print("Ваш уровень: ", 4)

x1 = int(input("Введите первое число: "))
x2 = int(input("Введите второе число: "))
x3 = int(input("Введите третье число: "))
if x1 > x2 and x1 > x3:
  print("Максимальное число:", x1)
elif x2 > x1 and x2 > x3:
  print("Максимальное число:", x2)
else:
  print("Максимальное число:", x3)

x = int(input("Введите икс: "))
if x == 0:
  print("Игрек равен", 5)
elif x > 0:
  print("Игрек равен", x - 1)
else:
  print("Игрек равен", x * x)

rating = int(input("Введите место в списке поступающих: "))
ball = int(input("Введите количество баллов за экзамены: "))
if rating <= 10 and ball >= 290:
  print("Поздравляем, Вы поступили!")
  print("Бонусом Вам будет начисляться стипендия")
elif rating <= 10:
  print("Поздравляем, Вы поступили!")
  print("Но Вам не хватило баллов для стипендии")
else:
  print("К сожалению, вы не поступили.")

rating = int(input('Что получил по математике? '))
if rating == 4 or rating == 5:
    print('Молодец! Можешь отдохнуть.')
else:
    print('Плохо. Марш учиться!')

n = int(input("Введите число: "))
if (n > 9 and n < 100) or (n < -9 and n > -100):
  print("Число", n, "вошло в диапазон")
else:
  print("Число", n, "не вошло в диапазон")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
if a == b and b == c:
  print(3)
elif a == b or b == c or a == c:
  print(2)
else:
  print(0)

space = int(input("Введите площадь квартиры: "))
price = int(input("Введите стоимость квартиры в млн.: "))
if (space >= 100 and price <= 10) or (space >= 80 and price <= 7):
  print("Квартира подхолит")
else:
  print("Квартира не подхолит")

profit = int(input("Введите величину дохода: "))
if profit < 0:
    print("Доход не может быть меньше нуля")
elif profit < 10000:
    tax = profit * 13 / 100
    print("Ставка налога при доходе",  profit, "равна", tax)
elif profit < 50000:
    tax = (profit - 10000) * 20 / 100 + (10000 * 13 / 100)
    print("Ставка налога при доходе",  profit, "равна", tax)
else:
    tax = (profit - 50000) * 30 / 100 + (40000 * 20 / 100) + (10000 * 13 / 100)
    print("Ставка налога при доходе",  profit, "равна", tax)


t = int(input("Введите время в часах: "))
if (t > 8 and t < 10) or (t > 12 and t < 14) or (t > 15 and t < 18) or (t > 20 and t < 22) :
    print("Можно получить посылку")
else:
    print("Нельзя получить посылку")

if  (t <= 8) or (t >= 10 and t <= 12) or (t >= 14 and t <= 15) or (t >= 18 and t <= 20) or t >= 22:
    print("Нельзя получить посылку")
else:
    print("Можно получить посылку")