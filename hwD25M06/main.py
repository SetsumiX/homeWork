import math

class TheAreaOf:

    @staticmethod
    def rectangle():
        action = input(f"Для расчёта площади, выберите по какому варианту вы будете его вести:\n"
                       f"1 - По формуле длины и ширины.\n"
                       f"2 - По формуле стороны и диагонали.\n"
                       f"3 - По формуле периметра и одной стороны.\n"
                       f"Ответ: ")

        def rectOne(a, b):
            S = a * b
            return S

        def rectSec(a, d):
            S = a * math.sqrt(d**2 - a**2)
            return S

        def rectThi(p, a):
            S = (p * a) - 2 * a
            return S

        while True:
            match action:
                case "1":
                    a = int(input("длина, a = "))
                    b = int(input("длина ширина, b = "))
                    print(rectOne(a, b))
                    break
                case "2":
                    a = int(input("длина стороны, a = "))
                    d = int(input("диагональ, d = "))
                    print(rectSec(a, d))
                    break
                case "3":
                    p = int(input("периметр, p = "))
                    a = int(input("длина стороны, a = "))
                    print(rectThi(p, a))
                    break
                case _:
                    print("Нет такого")

    @staticmethod
    def circle():
        action = input(f"Для расчёта площади, выберите по какому варианту вы будете его вести:\n"
                       f"1 - По формуле через радиус.\n"
                       f"2 - По формуле через диаметр.\n"
                       f"3 - По формуле через длину окружности.\n"
                       f"Ответ: ")
        def circleOne(r):
            S = 3.14159 * (r**2)
            return round(S, 2)

        def circleSec(d):
            S = (3.14159 * (d**2)) / 4
            return round(S, 2)

        def circleThi(l):
            S = (l**2) / (4 * 3.14159)
            return round(S, 2)

        while True:
            match action:
                case "1":
                    r = int(input("радиус, r = "))
                    print(circleOne(r))
                    break
                case "2":
                    d = int(input("диаметр, d = "))
                    print(circleSec(d))
                    break
                case "3":
                    l = int(input("длина окружности, l = "))
                    print(circleThi(l))
                    break
                case _:
                    print("Нет такого")

    @staticmethod
    def right_triangle():
        action = input(f"Для расчёта площади, выберите по какому варианту вы будете его вести:\n"
                       f"1 - По формуле катетов.\n"
                       f"2 - По формуле гипотенузы и высоты.\n"
                       f"3 - По формуле гипотенузы и острому углу.\n"
                       f"4 - По формуле вписанной окружности.\n"
                       f"Ответ: ")

        def right_triangleOne(a, b):
            S = (a * b) / 2
            return S

        def right_triangleSec(a, h):
            S = (a * h) / 2
            return S

        def right_triangleThi(a, r):
            rad = math.radians(r)
            S = ((a**2) * math.sin(rad * 2)) / 4
            return S

        def right_triangleFour(a, r):
            S = r * (r + a)
            return S

        while True:
            match action:
                case "1":
                    a = int(input("катет, a = "))
                    b = int(input("катет, b = "))
                    print(right_triangleOne(a, b))
                    break
                case "2":
                    a = int(input("гипотенуза, a = "))
                    h = int(input("высота, h = "))
                    print(right_triangleSec(a, h))
                    break
                case "3":
                    a = int(input("гипотенуза, a = "))
                    r = int(input("угол, r = "))
                    print(right_triangleThi(a, r))
                    break
                case "4":
                    a = int(input("гипотенуза, a = "))
                    r = int(input("радиус окружности, r = "))
                    print(right_triangleFour(a, r))
                    break
                case _:
                    print("Нет такого")

    @staticmethod
    def trapezoid():
        action = input(f"Для расчёта площади, выберите по какому варианту вы будете его вести:\n"
                       f"1 - По формуле оснований и высоте.\n"
                       f"2 - По формуле средней линии и высоте.\n"
                       f"3 - По формуле диагоналей и углу между ними.\n"
                       f"4 - По формуле четырёх сторон.\n"
                       f"Ответ: ")
        def trapOne(A_base_L, B_base_L, drawn_base):
            S = (A_base_L + B_base_L) * drawn_base / 2
            return S

        def trapSec(m, h):
            S = m * h
            return S

        def trapThi(d1, d2, deg):
            x = math.radians(deg)
            S = (d1 * d2 * math.sin(x)) / 2
            return round(S, 2)

        def trapFour(a, b, c, h):
            S = ((a + b) / 2) * math.sqrt((c**2) - ((b - a)**2 + (h**2) / 4))
            return S

        while True:
            match action:
                case "1":
                    a = int(input("длина основания, a = "))
                    b = int(input("длина основания, b = "))
                    h = int(input("высота, проведённая к основанию, h = "))
                    print(trapOne(a, b, h))
                    break
                case "2":
                    m = int(input("средняя линия трапеции, m = "))
                    h = int(input("высота трапеции, h = "))
                    print(trapSec(m, h))
                    break
                case "3":
                    d1 = int(input("длина диагонали, a = "))
                    d2 = int(input("длина диагонали, b = "))
                    deg = int(input("x угол между диагоналями, x = "))
                    print(trapThi(d1, d2, deg))
                    break
                case "4":
                    a = int(input("длина основания, a = "))
                    b = int(input("длина основания, b = "))
                    c = int(input("длинна диагонали, c = "))
                    h = int(input("высота, опущенная на основание, h = "))
                    print(trapFour(a, b, c, h))
                    break
                case _:
                    print("Нет такого")

findTheArea = TheAreaOf()
# findTheArea.trapezoid()
# findTheArea.rectangle()
# findTheArea.circle.txt()
# findTheArea.right_triangle()