import sqlite3
from config import logger


class DataBase:
    def __init__(self, db_path: str) -> None:
        """Подключение к базе данных"""
        try:
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            logger.debug("Подключение к базе данных прошло успешно")
        except sqlite3.Error as e:
            logger.error(f"Ошибка подключения к базе данных: {e}")

    def get_client_by_tgid(self, user_id):
        try:
            self.cursor.execute(
                f"SELECT * FROM inbounds WHERE settings LIKE '%\"tgId\": {user_id}%';"
            )
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(f"Ошибка выполнения запроса: {e}")
