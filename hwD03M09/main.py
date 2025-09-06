import sqlite3

class BookCollection:
    def __init__(self, db="bookbase.db"):
        self.db = db
        self.create_tb_author()
        self.create_tb_genres()
        self.create_tb_book()

    def create_tb_author(self):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS authors(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL
                    )
            """)
            connection.commit()

    def create_tb_genres(self):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS genres(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    genre TEXT NOT NULL UNIQUE
                    )
            """)
            connection.commit()

    def create_tb_book(self):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    date TEXT,
                    id_author INTEGER,
                    id_genre INTEGER,
                    FOREIGN KEY (id_author) REFERENCES authors (id) ON DELETE CASCADE,
                    FOREIGN KEY (id_genre) REFERENCES genres (id) ON DELETE CASCADE
                    )
            """)
            connection.commit()

    def add_to_author(self, name, surname):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO authors(name, surname) VALUES(?, ?)", (name, surname))
            connection.commit()

    def add_to_genre(self, genre):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO genres(genre) VALUES(?)", genre)
            connection.commit()

    def add_to_book(self, title, date, id_author, id_genre):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO books(title, date, id_author, id_genre) VALUES(?,?,?,?)",
                           (title,date,id_author,id_genre))
            connection.commit()

    def get_bk_by_auth(self, name, surname):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT books.title, books.date, genres.genre FROM books
            JOIN authors ON books.id_author = authors.id
            JOIN genres ON books.id_genre = genres.id
            WHERE authors.name = ? AND authors.surname = ?
            """, (name,surname))
            base_arr = cursor.fetchall()

            print(f"\nКниги по автору({name} {surname}):")
            for title, date, genre in base_arr:
                print(f"\nНазвание: {title}\n"
                      f"Жанр: {genre}\n"
                      f"Дата выпуска: {date}")
            return base_arr

    def get_bk_by_gnr(self, genre):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT books.title, books.date, authors.name, authors.surname FROM books
            JOIN authors ON books.id_author = authors.id
            JOIN genres ON books.id_genre = genres.id
            WHERE genres.genre = ?
            """, (genre,))
            base_arr = cursor.fetchall()

            print(f"\nКниги по жанру ({genre}):")
            for t, d, n, s in base_arr:
                print(f"\nАвтор: {n} {s}\n"
                      f"Название: {t}\n"
                      f"Дата выпуска: {d}")
            return base_arr

    def get_bk_auth_gnr(self, name, surname, genre):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT books.title, books.date, genres.genre FROM books
            JOIN authors ON books.id_author = authors.id
            JOIN genres ON books.id_genre = genres.id
            WHERE authors.name = ?, authors.surname = ?, genres.genre = ?
            """, (name, surname, genre))
            base_arr = cursor.fetchall()

            print(f"\nКниги по автору и жанру ({name} {surname}, {genre})")
            for t, d, g in base_arr:
                print(f"\nНазвание: {t}\n"
                      f"Жанр: {g}\n"
                      f"Дата выпуска: {d}")
            return base_arr

    def get_all_bk(self):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT authors.name, authors.surname, books.title, books.date, genres.genre
            FROM books
            JOIN authors ON books.id_author = authors.id
            JOIN genres ON books.id_genre = genres.id
            ORDER BY authors.name, authors.surname
            """)
            base_arr = cursor.fetchall()

            print("\nВсе книги:")
            for n, s, t, d, g in base_arr:
                print(f"\nАвтор: {n} {s}\n"
                      f"Книга: {t}\n"
                      f"Жанр: {g}\n"
                      f"Дата выпуска: {d}")
            return base_arr

    def get_count_by_authors(self):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT authors.name, authors.surname, COUNT(books.id) as count_book FROM authors
            LEFT JOIN books ON books.id_author = authors.id
            GROUP BY authors.id
            ORDER BY count_book DESC
            """)
            base_arr = cursor.fetchall()

            print("\nКоличество книг всех авторов")
            for n, s, cb in base_arr:
                print(f"\nАвтор: {n} {s}\n"
                      f"Количество книг в базе:{cb}")
            return base_arr

    def _del_cascade_bk_author(self, name, surname):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM authors WHERE authors.name = ? AND authors.surname = ?", (name, surname))
            connection.commit()
            print(f"\nУдаление: {name} {surname} и книг автора произведено успешно\n")

bdb = BookCollection()

author_arr = [
    ("Лев", "Толстой"),
    ("Фёдор", "Достоевский"),
    ("Антон", "Чехов")
]
genre_arr = [
    ("Роман",),
    ("Драма",),
    ("Повесть",)
]
book_arr = [
    ("Война и мир", "1869", 1, 1),
    ("Анна Каренина", "1877", 1, 1),
    ("Преступление и наказание", "1866", 2, 1),
    ("Вишневый сад", "1904", 3, 2)
]
for n, s in author_arr:
    bdb.add_to_author(n, s)

for g in genre_arr:
    bdb.add_to_genre(g)

for t,d,id_a,id_g in book_arr:
    bdb.add_to_book(t,d,id_a,id_g)

bdb.get_all_bk()
bdb.get_bk_by_gnr("Драма")
bdb.get_bk_by_auth("Лев", "Толстой")
bdb.get_count_by_authors()
bdb._del_cascade_bk_author("Лев", "Толстой")
bdb.get_all_bk()