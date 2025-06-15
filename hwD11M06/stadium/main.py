class Stadium:
    def __init__(self, name, date, country, city, capacity):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity
    def info(self):
        print(f"\nСамым большим стадионом, является *{self.name}*\n"
              f"В стране под названием {self.country}\n"
              f"Город {self.city}\n"
              f"Дата создания данного стадиона: {self.date}\n"
              f"А вместимость составляет {self.capacity} человек")

kndr_phen = Stadium("Стадион Первого мая", "1 мая 1989 года", "КНДР", "Пхеньян", 114000)

kndr_phen.info()