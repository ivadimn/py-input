import math
class Circle:

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def get_area(self)-> float:
        return math.pi * self.radius * self.radius

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius

circle = Circle(10)
area = circle.get_area() # возвращает 314.1592653589793
perimeter = circle.get_perimeter() # возвращает 62.83184
print(area)
print(perimeter)
