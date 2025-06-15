class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
    def info(self):
        print(f"\nКнига под названием *{self.name}*, была выпущена в {self.year} году, писателем {self.author}\n"
              f"Жанр данного произведения {self.genre}\n"
              f"Издательство: {self.publisher}\n"
              f"Цена: {self.price} рублей")

the_hero_of_our_time_1840 = Book("Герой нашего времени", 1840, "<<АСТ>>", "роман", "М. Ю. Лермонтов", 200)

the_hero_of_our_time_1840.info()