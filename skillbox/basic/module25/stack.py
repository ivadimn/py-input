class Stack:

    def __init__(self):
        self.__stack = list()

    def push(self, object):
        self.__stack.insert(0, object)

    def pop(self):
        l = len(self.__stack)
        if l > 0:
            t = self.__stack.pop(0)
            return t
        else:
            return None

    def length(self):
        return len(self.__stack)

    def print_stack(self):
        for object in self.__stack:
            print(object)


class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __str__(self):
        return "{0} {1}".format(self.priority, self.name)


class TaskManager:
    count_task = 0

    def __init__(self):
        self.tasks = Stack()

    def new_task(self, name, priority):
        task = Task(name, priority)
        l = self.tasks.length()
        print("*****Вызов функции new_task*** {0}, размер стека {1}\n".format(task, l))
        if l > 0:
            self.insert_task(task)
        else:
            self.tasks.push(Task(name, priority))

        self.count_task += 1

    def insert_task(self, task):
        t : Task = self.tasks.pop()
        if self.tasks.length() > 0:
            if t.priority <= task.priority:
                self.insert_task(task)
                self.tasks.push(t)
            else:
                self.tasks.push(t)
                self.tasks.push(task)
        else:
            if t.priority > task.priority:
                self.tasks.push(t)
                self.tasks.push(task)
            else:
                self.tasks.push(task)
                self.tasks.push(t)

    def __str__(self):
        if self.tasks.length() > 0:
            return "\n".join(["{0} {1}".format(self.tasks.pop().priority, self.tasks.pop().name) for _ in
                              range(self.tasks.length())])

    def print_tasks(self):
        self.tasks.print_stack()


tasks = {"сделать уборку 1": 4, "помыть посуду 2": 4, "отдохнуть": 1,
         "поиграть": 5, "поесть 1": 2, "сдать дз 2": 2}

manager = TaskManager()

for k, v in tasks.items():
    manager.new_task(k, v)
    print("************Печать стека*********************************")
    manager.print_tasks()
    print("*********************************************\n")

manager.new_task("лечь спать 3", 4)

manager.print_tasks()


