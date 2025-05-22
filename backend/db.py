import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            flagged INTEGER DEFAULT 0,
            emotion_tag TEXT,
            mood TEXT
        );
    """)
    conn.commit()
    conn.close()

def add_flagged_column():
    conn = get_db_connection()
    try:
        conn.execute('ALTER TABLE messages ADD COLUMN flagged INTEGER DEFAULT 0')
        print("Added 'flagged' column.")
    except sqlite3.OperationalError:
        print("'flagged' column already exists.")
    conn.commit()
    conn.close()
