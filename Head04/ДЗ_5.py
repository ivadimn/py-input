#1: Создайте функцию, принимающую на вход имя, возраст и город
# проживания человека. Функция должна возвращать строку вида
# «Василий, 21 год(а), проживает в городе Москва»

def my_func(name, age, city):
    return name +', ' + str(age) + " год(а), проживает в городе " + city

print(my_func("Василий",21,"Москва"))


#2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def func_max(val1,val2,val3):
     return  max(val1,val2,val3)

print(func_max(23,77,55))