class Vehicles:

    def __init__(self, name):
        self.name = name

    def does(self):
        return print(f"{self.name}, перемещается.")

# ////////////////////////////////////////////////////////////////////////////////

class GroundVehicle(Vehicles):

    def __init__(self, name, brand, color, ground):
        super().__init__(name)
        self.ground = ground
        self.color = color
        self.brand = brand

    def does(self):
        return print(f"{self.name} {self.brand} цвета {self.color}, едет по: {self.ground}")

class AirVehicle(Vehicles):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def does(self):
        return print(f"{self.color} {self.name}, летит по воздуху.")

class WaterVehicle(Vehicles):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def does(self):
        return print(f"{self.name} цвета {self.color}, плывёт по воде.")

# ////////////////////////////////////////////////////////////////////////////////

class Wheeled(GroundVehicle):

    def __init__(self, name, brand, color, type, model, ground):
        super().__init__(name, brand, color, ground)
        self.type = type
        self.model = model

    def does(self):
        return print(f"{self.name.capitalize()}, марка {self.brand}, модель {self.model}, цвет {self.color}, едет по {self.ground}")

    def what_type_of(self):
        return print(f"Кузов данного авто, {self.type}")

myminivan = Wheeled("Машина", "Toyota", "Чёрный", "минивэн", "Alphard", "асфальту")
myminivan.does()
myminivan.what_type_of()

class PassengerClass(AirVehicle):

    def __init__(self, name, company, count_engines, count_passengers, color):
        super().__init__(name, color)
        self.count_engines = count_engines
        self.count_passengers = count_passengers
        self.company = company
        self.is_fly = False

    def take_off(self):
        if self.is_fly == False:
            print(f"{self.name.capitalize()}, компании {self.company}, взлетает.")
            self.is_fly = True
        else:
            print(f"{self.name.capitalize()}, уже летит.")

    def landing(self):
        if self.is_fly == True:
            print(f"{self.name}, компании {self.company}, идёт на посадку")
            self.is_fly = False
        else:
            print(f"Самолёт {self.name} не летит.")

airliner = PassengerClass("Boeing 737", "Пожилой Airlines", 2, 189, "белый")
airliner.take_off()
airliner.take_off()
airliner.landing()
airliner.landing()

class EngineBoat(WaterVehicle):

    def __init__(self, name, color, engine_count, engine_ph):
        super().__init__(name, color)
        self.engine_count = engine_count
        self.engine_ph = engine_ph
        self.engine_turn = False

    def engineON(self):
        if self.engine_turn == False:
            print(f"Заводим лодку {self.name}")
            self.engine_turn = True
        else:
            print("Лодка заведена")

    def engineOFF(self):
        if self.engine_turn == True:
            print(f"Глушим лодку {self.name}")
            self.engine_turn = False
        else:
            print("Лодка заглушена")

    def go_by_boat(self):
        if self.engine_turn == True:
            print(f"{self.name} плывёт на всех скоростях")
        else:
            print(f"{self.name} ещё не заведена, для перемещения заведите её.")

    def boat_info(self):
        return print(f"Лодка {self.name}, имеет двигатели в размере {self.engine_count} шт., так же, общая мощность составляет {self.engine_ph} лс.")

myBoat = EngineBoat("Yamaha 25", "grey", 2, 350)
myBoat.boat_info()
myBoat.go_by_boat()
myBoat.engineOFF()
myBoat.engineON()
myBoat.go_by_boat()
myBoat.engineON()
myBoat.engineOFF()