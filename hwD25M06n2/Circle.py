class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __add__(self, other):
        return self.radius + other.radius

    def __sub__(self, other):
        return self.radius - other.radius

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __isub__(self, other):
        self.radius -= other.radius
        return self

c1 = Circle(15)
c2 = Circle(12)

print(c1 == c2)
print(c1 < c2)
print(c1 <= c2)
print(c1 > c2)
print(c1 >= c2)

c1 += c2
print(c1.radius)
c1 -= c2
print(c1.radius)