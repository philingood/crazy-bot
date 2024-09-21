import sqlite3
from config import logger


try:
    from config import DATABASE_FILE
except ImportError:
    DATABASE_FILE = "/Users/booba/Downloads/x-ui.db"
    pass


def connect_to_db(db_path):
    try:
        conn = sqlite3.connect(db_path)
        logger.info("Подключение к базе данных прошло успешно")
        return conn
    except sqlite3.Error as e:
        logger.error(f"Ошибка подключения к базе данных: {e}")
        return None


def get_client_traffics(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM client_traffics")
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        logger.error(f"Ошибка выполнения запроса: {e}")


def get_users(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM users")
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        logger.error(f"Ошибка выполнения запроса: {e}")


def main():
    db_path = DATABASE_FILE
    conn = connect_to_db(db_path)

    if conn:
        print(get_client_traffics(conn))
        get_users(conn)
        conn.close()


if __name__ == "__main__":
    main()
