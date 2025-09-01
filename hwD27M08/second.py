import sqlite3

conn = sqlite3.connect("all_data.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS music_collection(
    author TEXT NOT NULL,
    name_song TEXT NOT NULL,
    genre TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS archive(
    author TEXT NOT NULL,
    name_song TEXT NOT NULL,
    genre TEXT
    )
""")

cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS trigger_insert
    BEFORE INSERT ON music_collection
    FOR EACH ROW
    BEGIN
        SELECT CASE WHEN NEW.genre = 'Dark Power Pop' THEN RAISE(ABORT, 'Вы ввели жанр: Dark Power Pop') END;
        SELECT CASE WHEN EXISTS(
            SELECT 1 FROM music_collection WHERE author = NEW.author AND genre = NEW.genre) THEN RAISE(ABORT, 'Нельзя добавить дубликат') END;
    END;
""")

cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS trigger_delete
    BEFORE DELETE ON music_collection
    FOR EACH ROW
    BEGIN
        INSERT INTO archive (author, name_song, genre)
        VALUES (OLD.author, OLD.name_song, OLD.genre);
    END;
""")

cursor.execute("INSERT INTO music_collection (author, name_song, genre) VALUES ('The Beatles', 'Here Comes The Sun', 'Pop')")

print("\nКоллекция")
for i in cursor.execute("SELECT * FROM music_collection"):
    print(i)

# cursor.execute("INSERT INTO music_collection (author, name_song, genre) VALUES ('The Beatles', 'Here Comes The Sun', 'Dark Power Pop')")


# cursor.execute("INSERT INTO music_collection (author, name_song, genre) VALUES ('The Beatles', 'Here Comes The Sun', 'Pop')")

cursor.execute("DELETE FROM music_collection WHERE author = 'The Beatles'")

print("\nАрхив")
for a in cursor.execute("SELECT * FROM archive"):
    print(a)

conn.close()