class Stack:

    def __init__(self):
        self.__stack = []

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


class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __str__(self):
        return "{0} {1}".format(self.priority, self.name)


class TaskManager:
    count_task = 0
    def __init__(self):
        self.stack = Stack()

    def new_task(self, name, priority):
        l = self.stack.length()
        task = Task(name, priority)
        if l > 0:
            self.insert_task(task)
            print("*********************************************")
        else:
            self.stack.push(Task(name, priority))

    def insert_task(self, task):
        print("---------------------------{0}".format(task))
        t : Task = self.stack.pop()
        print("Извлекли {0}".format(t))
        if t.priority <= task.priority and self.stack.length() > 0:
            self.insert_task(task)
            self.stack.push(t)
            print("Gоложили {0} ".format(t))
        else:
            if t.priority == task.priority:
                self.stack.push(t)
                self.stack.push(task)
            else:
                self.stack.push(task)
                self.stack.push(t)
            print("Конец рекурсии положили {0} и {1}".format(task, t))

    def __str__(self):
        if self.stack.length() > 0:
            return "\n".join(["{0} {1}".format(self.stack.pop().priority, self.stack.pop().name) for _ in
                              range(self.stack.length())])

    def print_tasks(self):
        for _ in range(self.stack.length()):
            t = self.stack.pop()
            print(t)


manager = TaskManager()
manager.new_task("сделать уборку 1", 4)
manager.new_task("помыть посуду 2", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поиграть", 5)
manager.new_task("поесть 1", 2)
manager.new_task("сдать дз 2", 2)
#manager.new_task("лечь спать 3", 4)

manager.print_tasks()
manager.print_tasks()

