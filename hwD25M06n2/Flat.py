class Flat:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.cost > other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __ge__(self, other):
        return self.cost >= other.cost

    def __le__(self, other):
        return self.cost <= other.cost

f1 = Flat(200, 1500000)
f2 = Flat(190, 1600000)

print(f1 == f2)
print(f1 != f2)
print(f1 > f2)
print(f1 < f2)
print(f1 >= f2)
print(f1 <= f2)