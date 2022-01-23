class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return "Точка с коодинатами ({0}, {1})".format(self.__x, self.__y)


class Person:
    __count = 0

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Person.__count += 1

    def set_name(self, name : str):
        if name.isalpha():
            self.__name = name
        else:
            raise ValueError("Неправильное имя")

    def set_age(self, age):
        if age in range(1, 91):
            self.__age = age
        else:
            raise ValueError("Некорректный возраст")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __str__(self):
        return "Person: имя: {0}, возраст: {1}".format(self.__name, self.__age)


p = Person("AAA", 90)
p.set_age(70)
p._Person__age = 20
print(p)