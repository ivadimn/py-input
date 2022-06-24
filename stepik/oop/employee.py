class Employee:

    @classmethod
    def from_string(cls, data: str):
        empl = data.split("-")
        return cls(empl[0], empl[1], int(empl[2]))

    def __init__(self, first_name: str, last_name: str, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

emp1 = Employee('Mary', 'Sue', 60000)
emp2 = Employee.from_string('John-Smith-55000')

print(emp1.first_name)
print(emp1.salary)
print(emp2.first_name)
print(emp2.salary)