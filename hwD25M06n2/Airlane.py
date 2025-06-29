class Airlane:
    def __init__(self, type, pass_total):
        self.type = type
        self.pass_total = pass_total

    def __eq__(self, other):
        return self.type == other.type

    def __lt__(self, other):
        return self.pass_total < other.pass_total

    def __le__(self, other):
        return self.pass_total <= other.pass_total

    def __gt__(self, other):
        return self.pass_total > other.pass_total

    def __ge__(self, other):
        return self.pass_total >= other.pass_total

    def __add__(self, other):
        return self.pass_total + other

    def __sub__(self, other):
        return self.pass_total - other

    def __iadd__(self, other):
        self.pass_total += other
        return self

    def __isub__(self, other):
        self.pass_total -= other
        return self

a1 = Airlane(1, 80)
a2 = Airlane(2, 74)
a3 = Airlane(1, 83)

print(a1 == a2)
print(a1 == a3)

print(a1 - 20)
print(a1 + 20)
a1 += 3
print(a1.pass_total)
a2 -= 4
print(a2.pass_total)