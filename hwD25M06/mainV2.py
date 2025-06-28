import math

class Figure:
    def _area(self):
        return 0

    def __int__(self):
        return int(round(self._area(), 2))

    def __str__(self):
        return f"{self.__class__.__name__} (площадь = {int(self)})"

class Rectangle(Figure):
    def __init__(self, height, width):
        self.width = width
        self.height = height

    def _area(self):
        return self.width * self.height

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def _area(self):
        return math.pi * self.radius ** 2

class RightTriangle(Figure):
    def __init__(self, leg1, leg2):
        self.leg1 = leg1
        self.leg2 = leg2

    def _area(self):
        return (self.leg1 * self.leg2) / 2

class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def _area(self):
        return (self.base1 + self.base2) * self.height / 2

rec = Rectangle(6, 10)
print(rec)
print(int(rec))

circ = Circle(5)
print(circ)
print(int(circ))

tri = RightTriangle(5, 8)
print(tri)
print(int(tri))

trap = Trapezoid(2, 4, 8)
print(trap)
print(int(trap))