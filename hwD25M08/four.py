import sqlite3

conn = sqlite3.connect("all_data.db")
cursor = conn.cursor()

emp_arr = [
    ('Иван', 'Иванов', 'IT', 80000),
    ('Мария', 'Петрова', 'IT', 90000),
    ('Олег', 'Сидоров', 'HR', 60000),
    ('Юля', 'Козлова', 'HR', 55000),
    ('Петр', 'Смирнов', 'IT', 120000),
    ('Анна', 'Волкова', 'Finance', 70000)
]

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        departament TEXT,
        salary REAL
    )
""")

cursor.executemany("INSERT INTO employees (name, surname, departament, salary) VALUES (?, ?, ?, ?)", emp_arr)

# conn.commit()

cursor.execute("""
    SELECT
        departament,
        GROUP_CONCAT(name, ', ') AS arr_names,
        COUNT(*) AS total_emp,
        AVG(salary) AS salary_avg_depar
    FROM employees
    GROUP BY departament
    ORDER BY salary_avg_depar DESC
""")

db_depart = cursor.fetchall()

for row in db_depart:
    print(f"Назначение: {row[0]}\n"
          f"Имена сотрудников: {row[1]}\n"
          f"Число сотрудников: {row[2]}\n"
          f"Средняя зарплата должности: {round(row[3], 2)}\n")

conn.close()