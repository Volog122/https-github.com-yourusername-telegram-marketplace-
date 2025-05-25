import sqlite3


def init_db():
    with sqlite3.connect("marketplace.db") as conn:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                price REAL,
                category TEXT,
                seller_username TEXT
            )
        """
        )

        cur.execute("SELECT COUNT(*) FROM items")
        count = cur.fetchone()[0]

        if count == 0:
            cur.executemany(
                "INSERT INTO items (title, description, price, category, seller_username) VALUES (?, ?, ?, ?, ?)",
                [
                    ("AI Бот", "Парсинг новостей", 100, "bot", "cooldev"),
                    ("Мем-чат", "Самые смешные мемы", 50, "chat", "memelord"),
                ],
            )

        conn.commit()


if __name__ == "__main__":
    init_db()
    print("База данных готова!")
