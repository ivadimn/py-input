def extra(self, arg):
    print(arg)

def required():
    return True

class Extras(type):
    def __init__(Class, classname, superclasses, attributedict):
        print("Init Extras")
        print(Class.__name__, classname)
        if required():
            Class.extra = extra


class Client1(metaclass=Extras):
    def __init__(self):
        print("Init Client")


x = Client1()
x.extra(arg = "Какое-то сообщение!")