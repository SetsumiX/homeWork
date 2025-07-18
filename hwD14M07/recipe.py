class RecipeModel:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, name, author, re_type, description, url_recipe, ingredients, country):
        recipe = {
            "Название": name,
            "Автор": author,
            "Подача": re_type,
            "Описание": description,
            "Видео": url_recipe,
            "Ингредиенты": ingredients,
            "Происхождение": country
        }
        self.recipes.append(recipe)
        return recipe

    def check_recipes(self):
        return self.recipes

    def get_recipe_by_name(self, name):
        for recipe in self.recipes:
            if name.lower() in recipe['Название'].lower():
                return recipe
        return None

    def delete_recipe(self, name):
        recipe = self.get_film_by_name(name)
        if recipe:
            self.recipes.remove(recipe)
            return True
        return False

class RecipeView:
    def display_recipe(self, recipe):
        if recipe:
            print(f"Содержимое рецепта: \n"
                  f"Название: {recipe['Название']}\n"
                  f"Автор: {recipe['Автор']}\n"
                  f"Подача: {recipe['Подача']}\n"
                  f"Описание: {recipe['Описание']}\n"
                  f"Видео: {recipe['Видео']}\n"
                  f"Ингредиенты: {recipe['Ингредиенты']}\n"
                  f"Происхождение: {recipe['Происхождение']}\n")

    def display_all_recipes(self, recipes):
        print("Список всех фильмов: ")
        for i, recipe in enumerate(recipes):
            print(f"{i}. {recipe['Название']}: {recipe['Описание']}, страна {recipe['Происхождение']}")

    def display_massage(self, massage):
        print(massage)

class RecipeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_recipe(self, name, author, re_type, description, url_recipe, ingredients, country):
        recipe = self.model.add_recipe(name, author, re_type, description, url_recipe, ingredients, country)
        self.view.display_massage(f"Рецепт {name} был добавлен")

    def show_all_recipes(self):
        recipes = self.model.get_all_resipes()
        self.view.display_all_recipes()

    def show_recipe(self, name):
        recipe = self.model.get_recipe_by_name(name)
        self.view.display_recipe(recipe)

    def del_recipe(self, name, author):
        result = self.model.del_recipe(name, author)
        if result:
            self.view.display_massage(f"Рецепт {author}, {name}, был удалён")
        else:
            self.view.display_massage(f"Рецепт {author}, {name}, не найден")

if __name__ == "__main__":
    model = RecipeModel()
    view = RecipeView()
    controller = RecipeController(model, view)

    controller.add_recipe("Луковый угар", "Роман Азазин", "Третье", "Выдуманный, но замечательный рецепт", r"https://www.youtube.com/watch?v=jtDnaGG_5Kg", "Картошка - 3 шт., Репчатый лук - 5 шт., Растительное масло, Апельсиновый сок - 300 мл., Вечина - 200 гр., Белый перец - 1 ст.л., Паприка - 3 ст.л., Соль - 5 ст.л., Макароны - 60 гр., Вермишель - 60 гр., Лимонный сок - 2 ч.л., Петрушка - щепотка, Укроп - щепотка, Кунжут - 1 ст.л, Чеснок - 3 зубчика, Чипсы - горсть", "Россия")

    controller.show_recipe("угар")