import sqlite3
from datetime import datetime

DB_NAME = "game.db"


def get_connection():
    """Возвращает соединение с БД."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row   # чтобы строки были как словари
    return conn


def init_db():
    """Создаёт таблицы, если их нет."""
    conn = get_connection()
    cur = conn.cursor()

    # Таблица партий
    cur.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            player      TEXT    NOT NULL,
            length      INTEGER NOT NULL,
            secret      TEXT    NOT NULL,
            attempts    INTEGER NOT NULL,
            won         INTEGER NOT NULL,   -- 1 = победа, 0 = сдался/не доиграл
            played_at   TEXT    NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_game(player, length, secret, attempts, won):
    """Сохраняет результат партии."""
    conn = get_connection()
    conn.execute(
        "INSERT INTO games (player, length, secret, attempts, won, played_at) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (player, length, secret, attempts, int(won), datetime.now().isoformat(timespec="seconds"))
    )
    conn.commit()
    conn.close()


def get_history(limit=50):
    """Возвращает последние партии."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT player, length, attempts, won, played_at "
        "FROM games ORDER BY id DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return rows


def get_best_result(length):
    """Лучший результат (минимум попыток) для данной длины среди побед."""
    conn = get_connection()
    row = conn.execute(
        "SELECT player, MIN(attempts) AS best FROM games "
        "WHERE length = ? AND won = 1", (length,)
    ).fetchone()
    conn.close()
    return row


def get_stats():
    """Общая статистика: всего игр, побед, среднее число попыток."""
    conn = get_connection()
    row = conn.execute(
        "SELECT COUNT(*) AS total, "
        "       SUM(won) AS wins, "
        "       AVG(CASE WHEN won = 1 THEN attempts END) AS avg_attempts "
        "FROM games"
    ).fetchone()
    conn.close()
    return row
