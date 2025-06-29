class Complex:
    def __init__(self, x, xj):
        self.x = x
        self.xj = xj

    def __add__(self, other):
        return self.x + other.x, self.xj + other.xj

    def __sub__(self, other):
        return self.x - other.x, self.xj - other.xj

    def __mul__(self, other):
        return self.x * other.x, self.xj * other.xj

    def __truediv__(self, other):
        return self.x / other.x, self.xj / other.xj

c1 = Complex(4, 12)
c2 = Complex(2, 7)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)