class ShoesModel:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoes_for, type_of, color_of, cost, brand, model, size):
        some_shoe = {
            "Пол": shoes_for,
            "Тип": type_of,
            "Цвет": color_of,
            "Цена": cost,
            "Производитель": brand,
            "Модель": model,
            "Размер": size
        }
        self.shoes.append(some_shoe)
        return some_shoe

    def chek_shoes(self):
        return self.shoes

    def get_shoe_by_params(self, brand, model, color, size):
        for shoe in self.shoes:
            if color.lower() in shoe["Цвет"].lower() and brand.lower() in shoe["Производитель"].lower() and model.lower() in shoe["Модель"].lower() and size == shoe["Размер"]:
                return shoe
        return None

    def del_shoe(self, brand, model, color, size):
        shoe = self.get_shoe_by_params(brand, model, color, size)
        if shoe:
            self.shoes.remove(shoe)
            return True
        return False

class ShoeView:
    def display_shoe(self, shoe):
        if shoe:
            print(f"Информация о обуви:\n"
                  f"Пол: {shoe['Пол']}\n"
                  f"Тип: {shoe['Тип']}\n"
                  f"Цвет: {shoe['Цвет']}\n"
                  f"Цена: {shoe['Цена']}\n"
                  f"Производитель: {shoe['Производитель']}\n"
                  f"Модель: {shoe['Модель']}\n"
                  f"Размер: {shoe['Размер']}\n")

    def display_all_shoes(self, shoes):
        print("Список всей обуви: ")
        for i, shoe in enumerate(shoes):
            print(f"{i}. {shoe['Производитель']} {shoe['Модель']} размер {shoe['Размер']}, цвет: {shoe['Цвет']}")

    def display_massage(self, massage):
        print(massage)

class ShoeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_shoe(self, shoes_for, type_of, color_of, cost, brand, model, size):
        shoe = self.model.add_shoe(shoes_for, type_of, color_of, cost, brand, model, size)
        self.view.display_massage(f"Обувь {brand} {model} была добавлена")

    def show_all_films(self):
        shoes = self.model.get_all_shoes()
        self.view.display_all_shoes()

    def show_shoe(self, brand, model, color, size):
        shoe = self.model.get_shoe_by_params(brand, model, color, size)
        self.view.display_shoe(shoe)

    def del_shoe(self, brand, model, color, size):
        result = self.model.del_shoe(brand, model, color, size)
        if result:
            self.view.display_massage(f"Обувь {brand} {model} размером {size}, и цветом {color}, была удалена")
        else:
            self.view.display_massage(f"Обувь {brand} {model} размером {size}, и цветом {color}, не найдена")

if __name__ == "__main__":
    model = ShoesModel()
    view = ShoeView()
    controller = ShoeController(model, view)

    controller.add_shoe("Мужской", "Ботинки", "Песочный", "16000", "LOWA", "ZEPHYR MK2 GTX LO", "43")

    controller.show_shoe("lowa", "zephyr", "песоч", "43")

    controller.del_shoe("lowa", "zephyr", "песоч", "43")

    controller.del_shoe("lowa", "zephyr", "песоч", "43")