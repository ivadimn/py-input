"""
class File:

    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, mode = self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with File("examp.txt", "r") as file:
    file.read()
"""

class Example():

    def __init__(self):
        print("Вызов __init__")

    def __enter__(self):
        print("Вызов __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Вызов __exit__")
        if exc_type:
            print("Тип ошибки: {0}".format(exc_type))
            print("Значение ошибки: {0}".format(exc_val))
            print(" 'След' ошибки: {0}".format(exc_tb))
        return True

my_obj = Example()

with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')
    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')

    print('Я обязательно выведусь...')