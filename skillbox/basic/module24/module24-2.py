import random
"""
class Toyota:
    color = 'Red'
    price = 2000000
    max_speed = 250
    current_speed = 0

car1 = Toyota()
car2 = Toyota()
car3 = Toyota()

car1.current_speed = random.randint(0, 250)
car2.current_speed = random.randint(0, 250)
car3.current_speed = random.randint(0, 250)
print(car1.current_speed)
print(car2.current_speed)
print(car3.current_speed)
"""

class Monitor:
    name = "Samsung"
    matrix = 'VA'
    resolution = "WQHD"
    frequency = 0

    def __str__(self):
        return "Name: {0}, Matrix: {1}, Resolution: {2}, Frequency: {3}".format(self.name, self.matrix, self.resolution, self.frequency)

class Headphones():
    name = "Sony"
    sensitivity = 108
    is_microphone = False

    def __str__(self):
        return "Name: {0}, Sensitivity: {1}, Has microphone: {2}".format(self.name, self.sensitivity,
                                                                            "No" if self.is_microphone else "Yes")


monitors = [Monitor() for _ in range(4)]
for monitor in monitors:
    monitor.frequency = random.randint(60, 150)
    print(monitor)

heads = [Headphones() for _ in range(4)]
for head in heads:
    head.is_microphone = True if random.randint(0, 1) == 1 else False
    print(head)
