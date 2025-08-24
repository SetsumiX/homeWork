import sqlite3

class DB_groceries:
    def __init__(self, db="default.db"):
        self.db = db
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS vegetables(
                    name TEXT UNIQUE,
                    category TEXT,
                    price REAL,
                    quantity INTEGER,
                    unit_measure TEXT,
                    discount INTEGER,
                    markdown BOOLEAN,
                    overdue BOOLEAN)
            """)
            cursor.execute("""
                UPDATE vegetables
                SET discount = 2
                WHERE price >= 150 AND discount IS Null
                """)
            connect.commit()

    def add_product(self, name, category, price, quantity, unit_measure, discount, markdown, overdue):
        with sqlite3.connect(self.db) as connect:
            try:
                cursor = connect.cursor()
                prdct = (name, category, price, quantity, unit_measure, discount, markdown, overdue)

                cursor.execute("""INSERT INTO vegetables(name, category, price, quantity, unit_measure, discount, markdown, overdue)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, prdct)
                connect.commit()
                print(f"Продукт {name} был добавлен в базу данных")
            except sqlite3.IntegrityError as err:
                if "name" in str(err).lower() or "UNIQUE constraint failed" in str(err):
                    print(f"Ошибка. Не может быть два одинаковых товара")
                else: print(f"Неизвестная ошибка. {err}")

    def showing_choice(self):
        while True:
            action = input(f"Выберите просмотр продуктов:\n"
                           f"1 - По возрастанию цен\n"
                           f"2 - По уценке\n"
                           f"3 - По просрочке\n"
                           f"4 - Показать всё\n"
                           f">>> ")
            match action:
                case "1":
                    self.show_by_lowprice()
                    break

                case "2":
                    self.show_markdown()
                    break

                case "3":
                    self.show_overdue()
                    break

                case "4":
                    self.show_all()
                    break

                case _:
                    print("Такого нет")

    def show_by_lowprice(self):
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM vegetables WHERE overdue = 0 ORDER BY price")
            vegets = cursor.fetchall()
            for veg in vegets:
                print(f"Название: {veg[0]}\n"
                      f"Категория: {veg[1]}\n"
                      f"Цена: {veg[2]}\n"
                      f"Количество: {veg[3]}\n"
                      f"Измерительная мера: {veg[4]}\n"
                      f"Скидка: {veg[5]}%\n"
                      f"Уценённое: {veg[6]}\n")

    def show_markdown(self):
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM vegetables WHERE markdown = 1")
            mrkdwn = cursor.fetchall()
            for veg in mrkdwn:
                print(f"Название: {veg[0]}\n"
                          f"Категория: {veg[1]}\n"
                          f"Цена: {veg[2]}\n"
                          f"Количество: {veg[3]}\n"
                          f"Измерительная мера: {veg[4]}\n"
                          f"Скидка: {veg[5]}%\n"
                          f"Уценённое: {veg[6]}\n"
                          f"Просрочено: {veg[7]}\n")

    def show_overdue(self):
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM vegetables WHERE overdue = 1")
            ovrd = cursor.fetchall()
            for veg in ovrd:
                print(f"Название: {veg[0]}\n"
                      f"Категория: {veg[1]}\n"
                      f"Цена: {veg[2]}\n"
                      f"Количество: {veg[3]}\n"
                      f"Измерительная мера: {veg[4]}\n"
                      f"Скидка: {veg[5]}%\n"
                      f"Уценённое: {veg[6]}\n"
                      f"Просрочено: {veg[7]}\n")
        self._del_overdue(input(f"Хотите удалить просрочку?\n"
                                f"Ответ(y/n(any)): "))

    def _del_overdue(self, answer):
        if answer.lower() == "y":
            with sqlite3.connect(self.db) as connect:
                cursor = connect.cursor()
                cursor.execute("DELETE FROM vegetables WHERE overdue = 1")
                connect.commit()

    def show_all(self):
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM vegetables WHERE unit_measure = 'кг'")
            res_kg = cursor.fetchall()
            if not res_kg:
                print("Данных о продуктах нет")
                return None
            for prdct_kg in res_kg:
                print(f"Название: {prdct_kg[0]}\n"
                      f"Категория: {prdct_kg[1]}\n"
                      f"Цена: {prdct_kg[2]}\n"
                      f"Количество: {prdct_kg[3]}\n"
                      f"Измерительная мера: {prdct_kg[4]}\n"
                      f"Скидка: {prdct_kg[5]}%\n"
                      f"Уценённое: {prdct_kg[6]}\n"
                      f"Просрочено: {prdct_kg[7]}\n")
            cursor.execute("SELECT * FROM vegetables WHERE unit_measure = 'шт'")
            res_sht = cursor.fetchall()
            if not res_sht:
                print("Данных о продуктах нет")
                return None
            for prdct_sht in res_sht:
                print(f"Название: {prdct_sht[0]}\n"
                      f"Категория: {prdct_sht[1]}\n"
                      f"Цена: {prdct_sht[2]}\n"
                      f"Количество: {prdct_sht[3]}\n"
                      f"Измерительная мера: {prdct_sht[4]}\n"
                      f"Скидка: {prdct_sht[5]}%\n"
                      f"Уценённое: {prdct_sht[6]}\n"
                      f"Просрочено: {prdct_sht[7]}\n")

db = DB_groceries("products.db")

while True:
    db.showing_choice()
