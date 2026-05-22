import sqlite3
from datetime import date

DB_NAME = "bot.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS sent (
            day TEXT PRIMARY KEY
        )
    """)
    conn.commit()
    conn.close()

def already_sent():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    today = str(date.today())
    c.execute("SELECT day FROM sent WHERE day=?", (today,))
    result = c.fetchone()
    conn.close()
    return result is not None

def mark_sent():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO sent (day) VALUES (?)", (str(date.today()),))
    conn.commit()
    conn.close()
