from abc import ABC, abstractmethod

class Ship(ABC):
    def __init__(self, name, residential_places, type):
        self._name = name
        self._residential_places = residential_places
        self._type = type
        self.power = False
        self.__move_speed = 0

    def __str__(self):
        return f"Судно, под названием {self._name}"

    def turn_on(self):
        if self.power == False:
            self.power = True
            print(f"Двигатели корабля {self._name} запущены.")
        else:
            print(f"Двигатели корабля {self._name} работают.")

    def turn_off(self):
        if self.power == True:
            self.power = False
            print(f"Двигатели корабля {self._name} заглушили.")
        else:
            print(f"Двигатели корабля {self._name} заглушены.")

    def get_info_ship(self):
        return f"Судно типа {self._type}, имеет {self._residential_places} спальных мест экипажа, название {self._name}"

    def get_info_speed(self):
        return f"{self._type} {self._name}, имеет ход в данный момент - ({self.__move_speed})."

    def move_a_dslow(self):
        print(f"Самый малый вперёд!")
        self.__move_speed = 1

    def move_a_slow(self):
        print("Малый вперёд!")
        self.__move_speed = 2

    def move_a_half(self):
        print("Половина вперёд!")
        self.__move_speed = 3

    def move_a_full(self):
        print("Полный вперёд!")
        self.__move_speed = 4

    def move_a_efull(self):
        print("Самый полный вперёд!")
        self.__move_speed = 5

    def move_stop(self):
        print("Стоп движение!")
        self.__move_speed = 0

    def move_b_slow(self):
        print("Малый назад!")
        self.__move_speed = -1

    def move_b_half(self):
        print("Половина назад!")
        self.__move_speed = -2

    def move_b_full(self):
        print("Полный назад!")
        self.__move_speed = -3



class Frigat(Ship):
    def __init__(self, name, residential_places, type, cannon, missiles):
        super().__init__(name, residential_places, type)
        self.cannon = cannon
        self.missiles = missiles

    def __str__(self):
        return (f"Перед вами появился утончённый {self._type} с орудиями, название судна {self._name}.\n"
                f"Вы взобрались на него, он был полностью готов к отплытию, как и команда.\n")

    def get_info_ship(self):
        return (f"Судно типа {self._type}, имеет {self._residential_places} спальных мест экипажа, название его {self._name}.\n"
                f"А так же на своём борту имеет {self.cannon}, и {self.missiles}\n")


class Destroyer(Ship):
    def __init__(self, name, residential_places, type, cannon, missiles, count_cann):
        super().__init__(name, residential_places, type)
        self.cannon = cannon
        self.missiles = missiles
        self.count_cann = count_cann

    def __str__(self):
        return (f"Войдя в порт, пред вами взмыл ввысь огромный {self._type} с орудиями на перевес, название данного судна звучало так {self._name}.\n"
                f"Вы взобрались на него, он был полностью готов к отплытию, как и команда.\n")

    def get_info_ship(self):
        return (
            f"Судно типа {self._type}, имеет {self._residential_places} спальных мест экипажа, название его {self._name}.\n"
            f"А так же на своём борту имеет {self.cannon}, общее количество орудий {self.count_cann}, и {self.missiles}\n")


class Cruiser(Ship):
    def __init__(self, name, residential_places, type, cannon, missiles, count_cann):
        super().__init__(name, residential_places, type)
        self.cannon = cannon
        self.missiles = missiles
        self.count_cann = count_cann

    def __str__(self):
        return (f"На порту вас ждал {self._type} под названием {self._name}, корабль, который может выполнять задачи независимо от основного флота.\n"
                f"После проверки готовности, вы ринулись в капитанский мостик.\n")

    def get_info_ship(self):
        return (f"{self._type.capitalize()} под названием {self._name}, имеет {self._residential_places} спальных мест для экипажа.\n"
                f"Имеет на себе основные {self.cannon}, а количество всех орудий {self.count_cann} шт., и {self.missiles}\n")



myFrigat = Frigat("Адмирал Горшков", 210, "Фригат", "130-мм АУ А-192М", "Универсальный корабельный стрельбовый комплекс 3С14(УКСК)")
print(myFrigat)
print(myFrigat.get_info_ship())

myFrigat.turn_on()
myFrigat.move_a_slow()

print(myFrigat.get_info_speed())

myDestroyer = Destroyer("Лидер", 500, "Эсминец", "130 мм АУ А-192М «Армат»", "УКСК Калибр, Оникс, Циркон", 4)
print(myDestroyer)
print(myDestroyer.get_info_ship())

myCruiser = Cruiser("Адмирал Лазарев", 744, "Крейсер", "АК-130 калибром 130 мм", "ПКР «Гранит»", 10)
print(myCruiser)
print(myCruiser.get_info_ship())