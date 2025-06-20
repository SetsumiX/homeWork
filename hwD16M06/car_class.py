class Car:
    count_cars = 0

    def __init__(self, brand, capacity, year):
        self.brand = brand
        self.capacity = capacity
        self.year = year
        Car.count_cars += 1

    def get_in(self):
        return print(f"\nМарка авто: {self.brand}\nОбъём двигателя: {self.capacity} л.\nГод выпуска: {self.year} год")

    def set_in(self, model, color):
        self.model = model
        self.color = color

    @staticmethod
    def see_count():
        return print(f"Количество зарегистрированных машин: {Car.count_cars}")

car_Andrey = Car("Lada", 1.6, 1997) # 2109
car_Veniamin = Car("JEEP", 3.7, 2008) # Grand Cheeroke
car_Danil = Car("Lada", 1.6, 2006) # Priora
car_Alexandr = Car("Ford", 2.2, 2012) # Ranger T6
car_Gregoriy = Car("Subaru", 1.8, 1993) # Legacy I

car_Andrey.set_in("2109", "Баклажановый")
car_Veniamin.set_in("Grand Cheeroke", "Серебристый")
car_Danil.set_in("Priora", "Чёрный")
car_Alexandr.set_in("Ranger T6", "Красный")
car_Gregoriy.set_in("Legacy I", "Синий")

Car.see_count()

car_Andrey.get_in()
car_Veniamin.get_in()
car_Danil.get_in()
car_Alexandr.get_in()
car_Gregoriy.get_in()