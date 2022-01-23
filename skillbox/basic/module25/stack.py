class Stack:

    def __init__(self):
        self.__stack = list()

    def push(self, object):
        self.__stack.insert(0, object)
        print(self.__stack)

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

    def __init__(self):
        self.stack = Stack()

    def new_task(self, name, priority):
        l = self.stack.length()
        if  l > 0:
            self.insert_task(Task(name, priority))
        else:
            self.stack.push(Task(name, priority))

    def insert_task(self, task):
        temp = []
        l = self.stack.length()
        for _ in range(l):
            t = self.stack.pop()
            if t.priority < task.priority:
                temp.insert(0, t)
            else:
                self.stack.push(t)
                self.stack.push(task)

        for t in temp:
            self.stack.push(t)

    def __str__(self):
        if self.stack.length() > 0:
            return "\n".join(["{0} {1}".format(self.stack.pop().priority, self.stack.pop().name) for _ in
                              range(self.stack.length())])

    def print_tasks(self):
        for _ in range(self.stack.length()):
            t = self.stack.pop()
            print(t.priority, t.name)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.print_tasks()
lst = []
lst.insert(0, 1)
lst.insert(0, 2)
print(lst)
