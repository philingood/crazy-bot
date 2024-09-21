import sqlite3
import pytest
from db.db import connect_to_db, get_client_traffics, get_users


@pytest.fixture
def conn():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE client_traffics (id INTEGER PRIMARY KEY, traffic INTEGER)"""
    )
    cursor.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)""")

    cursor.execute("""INSERT INTO client_traffics (traffic) VALUES (500)""")
    cursor.execute("""INSERT INTO users (username) VALUES ('test_user')""")

    connection.commit()
    yield connection
    connection.close()


def test_connect_to_db():
    """Тестируем подключение к базе данных."""
    conn = connect_to_db(":memory:")
    assert conn is not None
    conn.close()


def test_get_client_traffics(conn):
    """Тестируем получение трафика клиентов."""
    result = get_client_traffics(conn)

    assert result == [(1, 500)]  # Ожидаемый результат


def test_get_users(conn):
    """Тестируем получение пользователей."""
    result = get_users(conn)

    assert result == [(1, "test_user")]  # Ожидаемый результат
