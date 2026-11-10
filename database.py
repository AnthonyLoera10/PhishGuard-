
import sqlite3

DATABASE = "phishguard.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            subject TEXT NOT NULL,
            risk_score INTEGER NOT NULL,
            risk_level TEXT NOT NULL,
            scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_scan(sender, subject, risk_score, risk_level):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO scans (sender, subject, risk_score, risk_level)
        VALUES (?, ?, ?, ?)
    """, (sender, subject, risk_score, risk_level))

    conn.commit()
    conn.close()


def get_scans():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, sender, subject, risk_score,
               risk_level, scan_date
        FROM scans
        ORDER BY scan_date DESC, id DESC
    """)

    scans = cursor.fetchall()

    conn.close()

    return scans
