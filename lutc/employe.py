
class Employee:
    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary

    def give_raise(self, persent):
        self.salary += (self.salary * persent)

    def work(self):
        print(self.name, "does stuff")

    def __repr__(self):
        return "<Employee name = %s, salary = %s>" % (self.name, self.salary)


class Chef(Employee):
    def __init__(self, name):
        super().__init__(name, 50000)

    def work(self):
        print(self.name, "makes food")

class Server(Employee):
    def __init__(self, name):
        super().__init__(name, 40000)

    def work(self):
        print(self.name, "interfaces with customer")

class PizzaRobot(Chef):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        print(self.name, "makes pizza")

if __name__ == "__main__":
    bob = PizzaRobot("Bob")
    print(bob)
    bob.work()
    bob.give_raise(0.25)
    print(bob)
    print()
    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()


