from abc import ABC
import pickle, json

class Pack_data:
    def __init__(self):
        self.full_data = {
            "История браузера": ["Главная Google", "YouTube - котики", "Википедия: Python", "Новости IT", "Курсы по алгоритмам"],
            "Музыкальный плейлист": ["Bohemian Rhapsody", "Hotel California", "Sweet Child O'Mine", "Smells Like Teen Spirit", "Imagine"],
            "Список дел": ["Зарядка", "Лекция по структурам данных", "Обед", "Прогулка", "Подготовка к экзамену"],
            "Навигация по городам": ["Москва", "Санкт-Петербург", "Казань", "Сочи", "Владивосток"],
            "Журнал научных статей": ["Квантовые вычисления", "ИИ в медицине", "Блокчейн технологии", "Космические исследования", "Биоинформатика"],
            "Операции с банковским счетом": ["Пополнение: +5000р", "Покупка в Amazon: -1200р", "Перевод другу: -300р", "Кэшбэк: +50р", "Комиссия: -30р"],
            "Этапы разработки ПО": ["Анализ требований", "Проектирование", "Кодирование", "Тестирование", "Внедрение"],
            "Список покупок": ["Хлеб", "Молоко", "Яйца", "Фрукты", "Шоколад"],
            "Хронология исторических событий": ["1969: Высадка на Луну", "1989: Падение Берлинской стены", "1991: Распад СССР", "2001: Запуск Wikipedia", "2020: Пандемия COVID-19"],
            "Список книг для чтения": ["1984 - Оруэлл", "Мастер и Маргарита - Булгаков", "Гарри Поттер - Роулинг", "Преступление и наказание - Достоевский", "Маленький принц - Экзюпери"],
        }

    def __str__(self):
        count = 0
        temp = []
        for i in self.full_data:
            temp.append(i)
            count += 1
        return f"\n{count} разделов со списками: {temp}\n"

    def print_data(self):
        count = 1
        for k, v in self.full_data.items():
            print(f"{count} {k}: ", v)
            count += 1

    def pack_pickle(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def unpuck_pickle(cls, filename):
        with open(filename, "rb") as file:
            data = pickle.load(file)
        return data

    def pack_json(self, filename):
        with open(filename, "w") as file:
            data = {
                "История браузера": self.full_data["История браузера"],
                "Музыкальный плейлист": self.full_data["Музыкальный плейлист"],
                "Список дел": self.full_data["Список дел"],
                "Навигация по городам":self.full_data["Навигация по городам"],
                "Журнал научных статей": self.full_data["Журнал научных статей"],
                "Операции с банковским счетом": self.full_data["Операции с банковским счетом"],
                "Этапы разработки ПО": self.full_data["Этапы разработки ПО"],
                "Список покупок": self.full_data["Список покупок"],
                "Хронология исторических событий": self.full_data["Хронология исторических событий"],
                "Список книг для чтения": self.full_data["Список книг для чтения"]
            }
            json.dump(data, file)

    @classmethod
    def unpuck_json(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            cls.full_data = data

pk_data = Pack_data()
print(pk_data)

pk_data.pack_json("my_list.json")
pk_data.unpuck_json("my_list.json")

pk_data.print_data()

pk_data.pack_pickle("my_list.txt")
pk_data.unpuck_pickle("my_list.txt")

pk_data.print_data()