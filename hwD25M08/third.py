import sqlite3

conn = sqlite3.connect("all_data.db")
cursor = conn.cursor()

order_arr = [
    ('фёдор', 800, '2024-01-15'),
    ('гЕНАДИЙ', 2500, '2024-01-16'),
    ('Олег', 7000, '2024-01-17'),
    ('Денис', 500, '2024-01-18'),
    ('София', 4500, '2024-01-19')
]

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        amount REAL,
        order_date TEXT
    )
""")

cursor.executemany("INSERT INTO orders (customer_name, amount, order_date) VALUES (?, ?, ?)", order_arr)

# conn.commit()

cursor.execute("""
    SELECT order_date, customer_name,
        CASE
            WHEN amount < 1000 THEN 'Недорогой'
            WHEN amount BETWEEN 1000 AND 5000 THEN 'Средний'
            ELSE 'Дорогой'
        END AS price_category
    FROM orders
    ORDER BY amount
""")

new_order_arr = cursor.fetchall()

print("Заказы(ГГГГ-ММ-ДД/Имя/Ценовая категория):")
for row in new_order_arr:
    print(f"{row[0]} | {row[1].title():8} | {row[2]}")

conn.close()