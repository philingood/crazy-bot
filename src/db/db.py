import sqlite3
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

try:
    from config import DATABASE_FILE
except ImportError:
    DATABASE_FILE = "/Users/booba/Downloads/x-ui.db"
    pass


def connect_to_db(db_path):
    try:
        conn = sqlite3.connect(db_path)
        logging.info("Подключение к базе данных прошло успешно")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Ошибка подключения к базе данных: {e}")
        return None


def get_client_traffics(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM client_traffics")
        rows = cursor.fetchall()
        for row in rows:
            logging.info(row)
    except sqlite3.Error as e:
        logging.error(f"Ошибка выполнения запроса: {e}")


def get_users(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM users")
        rows = cursor.fetchall()
        for row in rows:
            logging.info(row)
    except sqlite3.Error as e:
        logging.error(f"Ошибка выполнения запроса: {e}")


def main():
    db_path = DATABASE_FILE
    conn = connect_to_db(db_path)

    if conn:
        get_client_traffics(conn)
        get_users(conn)
        conn.close()


if __name__ == "__main__":
    main()
