from abc import abstractmethod

class Device:
    def __init__(self, name):
        self.name = name
        self.power = False

    def __str__(self):
        return f"Электронное устройство под названием: {self.name}"

    @abstractmethod
    def turn_on(self):
        if self.power == False:
            self.power = True
            print(f"Устройство {self.name} включили.")
        else:
            print(f"Устройство {self.name} уже включено.")

    @abstractmethod
    def turn_off(self):
        if self.power == True:
            self.power = False
            print(f"Устройство {self.name} выключили.")
        else:
            print(f"Устройство {self.name} уже выключено.")

    @abstractmethod
    def turn_func(self):
        print(f"Устройство {self.name}, выполнила функцию по предназначению")



class CoffeeMachine(Device):
    def __init__(self, name):
        super().__init__(name)
        self.power = False

    def __str__(self):
        return f"Перед вами кофемашина {self.name}"

    def turn_on(self):
        if self.power == False:
            self.power = True
            print(f"Кофемашину {self.name} включили.")
        else:
            print(f"Кофемашина {self.name} уже включена.")

    def turn_off(self):
        if self.power == True:
            self.power = False
            print(f"Кофемашину {self.name} выключили.")
        else:
            print(f"Кофемашина {self.name} уже выключена.")

    def turn_func(self):
        print(f"Кофемашина {self.name}, налила вам кофе.")


class Blender(Device):
    def __init__(self, name):
        super().__init__(name)
        self.power = False

    def __str__(self):
        return f"Перед вами блендер {self.name}"

    def turn_on(self):
        if self.power == False:
            self.power = True
            print(f"Блендер {self.name} включили.")
        else:
            print(f"Блендер {self.name} уже включён.")

    def turn_off(self):
        if self.power == True:
            self.power = False
            print(f"Блендер {self.name} выключили.")
        else:
            print(f"Блендер {self.name} уже выключен.")

    def turn_func(self, vegetables):
        print(f"Засовываем: ({vegetables.lower()}), в {self.name}, получили мякоть.")


class MeatGrinder(Device):
    def __init__(self, name):
        super().__init__(name)
        self.power = False

    def __str__(self):
        return f"Перед вами мясорубка {self.name}"

    def turn_on(self):
        if self.power == False:
            self.power = True
            print(f"Мясорубку {self.name} включили.")
        else:
            print(f"Мясорубку {self.name} уже включено.")

    def turn_off(self):
        if self.power == True:
            self.power = False
            print(f"Мясорубку {self.name} выключили.")
        else:
            print(f"Мясорубку {self.name} уже выключено.")

    def turn_func(self, meat):
        print(f"Засунули мясо: ({meat.lower()}), в {self.name}, получили фарш")


cm = CoffeeMachine("Redmond RCM-1517")
print(cm)
cm.turn_on()
cm.turn_func()

b = Blender("HURAKAN HKN-BLW2")
print(b)
b.turn_on()
b.turn_func("морковь")

m = MeatGrinder("Libhof MG-800b")
print(m)
m.turn_on()
m.turn_func("утка")