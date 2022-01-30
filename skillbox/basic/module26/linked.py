class Element:
    def __init__(self, obj):
        self.data = obj
        self.next = None

    def __str__(self):
        return "{0}".format(self.data)


class LinkedList():

    def __init__(self):
        self.head = None
        self.__current = None

    def append(self, obj):
        if self.head is None:
            self.head = Element(obj)
        else:
            data = self.head
            while not (data.next is None):
                data = data.next
            data.next = Element(obj)

    def __iter__(self):
        self.__current = self.head
        return self

    def __next__(self):
        data = self.__current
        if data is None:
            raise StopIteration
        self.__current = data.next
        return data

    def __str__(self) -> str:
        data = self.head
        elems = []
        while not data is None:
            elems.append(str(data))
            data = data.next
        return "[{0}]".format(" ".join(elems))

    def get(self, index: int):
        curr_i = 0
        data = self.head
        while not (data is None) and curr_i != index:
            data = data.next
            curr_i += 1
        return data.data

    def remove(self, index: int):
        if index == 0:
            self.head = self.head.next
            return
        curr_i = 0
        data = self.head
        prev = self.head
        while not (data is None) and curr_i != index:
            prev = data
            data = data.next
            curr_i += 1
        if not data is None:
            prev.next = data.next


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.append(60)
my_list.append(70)


print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:')
for elem in my_list:
    print(elem,  end = " ")

