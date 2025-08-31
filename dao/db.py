import sqlite3
from config import Config
import os

os.makedirs("instance", exist_ok=True)

def get_connection():
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    );
    """)

    cursor.execute("INSERT OR IGNORE INTO usuarios (id, email, senha) VALUES (1, 'teste@ifro.edu', '1234')")
    conn.commit()
    conn.close()
