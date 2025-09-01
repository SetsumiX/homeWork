import sqlite3

conn = sqlite3.connect("all_data.db")
cursor = conn.cursor()

cstmr_arr = [
    ('иван', 'иванов', 'dada@mail.ru'),
    ('МАРИЯ', 'СИДОРОВА', ''),
    ('пЁтР', 'пЕтРоВ', ''),
    ('Дмитрий', '', 'dimdos@gmail.com'),
    ('аЛЕКС', '', '')
]

cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT DEFAULT "*Пусто*",
        email TEXT DEFAULT "*Пусто*"
    )
""")

cursor.executemany("INSERT INTO customers (name, surname, email) VALUES (?, ?, ?)", cstmr_arr)

# conn.commit()

cursor.execute("SELECT * FROM customers")
new_cstmr_arr = cursor.fetchall()

print("Исходная база данных:")
for row in new_cstmr_arr:
    print(f"id: {row[0]}\nИмя: {row[1]}\nФамилия: {row[2]}\nПочта: {row[3]}\n")

print("Данные в нормальном виде:")
for row in new_cstmr_arr:
    print(f"Клиент: {row[1].title()} {row[2].title()}")

conn.close()