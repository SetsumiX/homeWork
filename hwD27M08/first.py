import sqlite3

conn = sqlite3.connect("all_data.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER DEFAULT 0,
        type TEXT
    )
""")

cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS product_insert_trigger
    BEFORE INSERT ON products
    FOR EACH ROW
    WHEN EXISTS(SELECT 1 FROM products WHERE name = NEW.name AND type = NEW.type)
    BEGIN
        UPDATE products 
        SET quantity = quantity + NEW.quantity 
        WHERE name = NEW.name AND type = NEW.type;
        
        SELECT RAISE(IGNORE);
    END
""")

prdct = [
    ("телефон", 3, "электроника"),
    ("нож", 4, "кухня"),
    ("телевизор", 5, "электроника")
]

cursor.executemany("INSERT INTO products (name, quantity, type) VALUES (?, ?, ?)", prdct)

conn.commit()

cursor.execute("SELECT * FROM products")
b = cursor.fetchall()

for i in b:
    print(i)

conn.close()