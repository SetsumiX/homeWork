import sqlite3

conn = sqlite3.connect("all_data.db")
cursor = conn.cursor()

prod_arr = [
    ('Ноутбук', 50000, 'Электроника'),
    ('Смартфон', 30000, 'Электроника'),
    ('Книга', 500, 'Литература'),
    ('Наушники', 3000, 'Электроника'),
    ('Ручка', 50, 'Канцелярия')
]

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL,
        category TEXT
    )
""")

cursor.executemany("INSERT INTO products (name, price, category) VALUES (?, ?, ?)", prod_arr)

# conn.commit()

cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]

cursor.execute("SELECT AVG(price) FROM products")
avg_price = cursor.fetchone()[0]

cursor.execute("SELECT MAX(price) FROM products")
_max_price = cursor.fetchone()[0]

print(f"|||     Ценовая политика товаров     |||\n"
      f"|||         Число товаров: {count}         |||\n"
      f"|||   Средняя цена товаров: {avg_price}  |||\n"
      f"||| Максимальная цена товара {_max_price} |||")

conn.close()