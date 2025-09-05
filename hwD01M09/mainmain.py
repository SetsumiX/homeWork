import sqlite3

class Calculator:
    def __init__(self, db="calcDB.db"):
        self.db = db
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS calcul_log(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first REAL,
                operator TEXT,
                second REAL,
                result REAL,
                create_date TEXT DEFAULT CURRENT_DATE)
            """)
            connect.commit()

    def save_in_data(self, arr_res):
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("INSERT INTO calcul_log(first, operator, second, result) VALUES (?, ?, ?, ?)", arr_res)
            # connect.commit()

    def log(self):
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM calcul_log")
            for row in cursor.fetchall():
                print(f"\n{row[0]}) {row[1]} {row[2]} {row[3]} = {row[4]}\nДата(ГГГГ-ММ-ДД):{row[5]}")

    def clear_log(self):
        with sqlite3.connect(self.db) as connect:
            cursor = connect.cursor()
            cursor.execute("DELETE FROM calcul_log")

    def menu(self):
        while True:
            choice = input(f"\n1 - Сложение\n"
                           f"2 - Вычитание\n"
                           f"3 - Умножение\n"
                           f"4 - Деление\n"
                           f"5 - История вычислений\n"
                           f"6 - Очистка истории\n"
                           f"7 - Выход\n"
                           f"Ввод(1-6): ")
            match choice:
                case "1":
                    self.addition()
                case "2":
                    self.substraction()
                case "3":
                    self.multiplication()
                case "4":
                    self.division()
                case "5":
                    self.log()
                case "6":
                    self.clear_log()
                case "7":
                    break
                case _:
                    print("Неверно введена команда")

    def addition(self):
        try:
            op = "+"
            a = input(f"Введите a. (a {op} b = ?)\n"
                      f"Ввод:")
            if a.lower() == "q": self.menu()
            b = input(f"А теперь введите b. ({a} {op} b = ?)\n"
                      f"Ввод:")
            if a.lower() == "q": self.menu()
            result = int(a) + int(b)
            print(f"{a} {op} {b} = {result}")
            arr_res = (a, op, b, result)

            self.save_in_data(arr_res)

        except Exception as err:
            print(f"Видимо что-то пошло не так\n"
                  f"Попробуйте ещё раз\n"
                  f"Или введите Q, чтоб выйти\n"
                  f"Ошибка:{err}\n")

    def substraction(self):
        try:
            op = "*"
            a = input(f"Введите a. (a {op} b = ?)\n"
                      f"Ввод:")
            if a.lower() == "q": self.menu()
            b = input(f"А теперь введите b. ({a} {op} b = ?)\n"
                      f"Ввод:")
            if a.lower() == "q": self.menu()
            result = int(a) * int(b)
            print(f"{a} {op} {b} = {result}")
            arr_res = (a, op, b, result)

            self.save_in_data(arr_res)

        except Exception as err:
            print(f"Видимо что-то пошло не так\n"
                  f"Попробуйте ещё раз\n"
                  f"Или введите Q, чтоб выйти\n"
                  f"Ошибка:{err}\n")

    def multiplication(self):
        try:
            op = "*"
            a = input(f"Введите a. (a {op} b = ?)\n"
                      f"Ввод:")
            if a.lower() == "q": self.menu()
            b = input(f"А теперь введите b. ({a} {op} b = ?)\n"
                      f"Ввод:")
            if a.lower() == "q": self.menu()
            result = int(a) * int(b)
            print(f"{a} {op} {b} = {result}")
            arr_res = (a, op, b, result)

            self.save_in_data(arr_res)

        except Exception as err:
            print(f"Видимо что-то пошло не так\n"
                  f"Попробуйте ещё раз\n"
                  f"Или введите Q, чтоб выйти\n"
                  f"Ошибка:{err}\n")

    def division(self):
        try:
            op = "/"
            a = input(f"Введите a. (a {op} b = ?)\n"
                      f"Ввод:")
            if a.lower() == "q": self.menu()
            b = input(f"А теперь введите b. ({a} {op} b = ?)\n"
                      f"Ввод:")
            if a.lower() == "q": self.menu()
            result = int(a) / int(b)
            print(f"{a} {op} {b} = {result}")
            arr_res = (a, op, b, result)

            self.save_in_data(arr_res)

        except Exception as err:
            print(f"Видимо что-то пошло не так\n"
                  f"Попробуйте ещё раз\n"
                  f"Или введите Q, чтоб выйти\n"
                  f"Ошибка:{err}\n")

def main():
    calc = Calculator()
    calc.menu()

if __name__ == "__main__":
    main()