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

    def __eq__(self, other):
        return self.priority == other.priority and self.name == other.name



class TaskManager:

    def __init__(self):
        self.tasks = Stack()

    def new_task(self, name, priority):
        task = Task(name, priority)
        if self.tasks.length() > 0:
            self.insert_task(task)
        else:
            self.tasks.push(Task(name, priority))

    def insert_task(self, task):
        t : Task = self.tasks.pop()
        if t == task:
            self.tasks.push(t)
            return
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

    def delete_task(self, name, priority):
        task = Task(name, priority)
        if self.tasks.length() > 0:
            self.remove_task(task)

    def remove_task(self, task):
        t = self.tasks.pop()
        if t == task:
            return
        else:
            self.remove_task(task)
            self.tasks.push(t)

    def __dict(self):
        lst = [self.tasks.pop() for _ in range(self.tasks.length())]
        d = dict()
        for task in lst:
            if task.priority in d:
                d[task.priority] = "; ".join((d[task.priority], task.name))
            else:
                d[task.priority] = task.name
        for task in lst[::-1]:
            self.tasks.push(task)
        return d

    def print_tasks(self):
        d = self.__dict()
        for k, v in d.items():
            print("{0} {1}".format(k, v))


tasks = {"сделать уборку 1": 4, "помыть посуду 2": 4, "отдохнуть": 1,
         "поиграть": 5, "поесть 1": 2, "сдать дз 2": 2, "лечь спать": 4}

manager = TaskManager()

for k, v in tasks.items():
    manager.new_task(k, v)

#задача которая, уже есть в списке игнорируется
manager.new_task("лечь спать", 4)

manager.print_tasks()
print("*" * 40)

#удаление задач
manager.delete_task("сдать дз 2", 2)
manager.delete_task("лечь спать", 4)
manager.print_tasks()


