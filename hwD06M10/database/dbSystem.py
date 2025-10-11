import sqlite3

class DBUser:
    def __init__(self, path="user.db"):
        self.path = path
        self.createDB()

    def createDB(self):
        with sqlite3.connect(self.path) as connect:
            cursor = connect.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT,
                    tg_id INTEGER UNIQ,
                    username TEXT,
                    timestamp TEXT
                )
            """)
            connect.commit()
            self.createTrigger()

    def createTrigger(self):
        with sqlite3.connect(self.path) as connect:
            cursor = connect.cursor()
            cursor.execute("""CREATE TRIGGER IF NOT EXISTS check_same_user
                BEFORE INSERT ON user
                FOR EACH ROW
                WHEN EXISTS (SELECT 1 FROM user WHERE tg_id = NEW.tg_id)
                BEGIN
                SELECT RAISE(IGNORE);
                END
            """)
            connect.commit()

    def add_user(self, tplInfo):
        with sqlite3.connect(self.path) as connect:
            cursor = connect.cursor()
            cursor.executemany("INSERT INTO user(full_name, tg_id, username, timestamp) VALUES(?, ?, ?, ?)", [tplInfo])
            connect.commit()

    def get_info(self):
        with sqlite3.connect(self.path) as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM user")
            print(cursor.fetchall())
