"""
def ask_user(question, compliant = "Неверный ввод. Пожалуйста, введите 'да' или 'нет'", retry = 4):
    while True:
        answer = input("{0} ".format(question))
        if answer.lower() == "да":
            return 0
        elif answer.lower() == "нет":
            return 1
        else:
            retry -= 1

            if retry == 0:
                print("Количество попыток истекло.")
                break
            print(compliant)
            print("Осталось попыток {0}".format(retry))


ask_user("Вы действительно хотите выйти?")
ask_user("Удалить файл?", compliant="Так удалить или нет?")
ask_user("Записать файл?", retry=2)


def add_num(num, lst = None):
    if lst == None:
        lst = []
    lst.append(num)
    print(lst)

add_num(5)
add_num(10)
add_num(15)
"""

def create_dict(data, template=None):
    if isinstance(data, dict):
        return data
    if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
        template = dict()
        template[data] = data
        return template


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        new_list.append(create_dict(i_element))
    return new_list


data = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data)
print(data)