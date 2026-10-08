import sqlite3
from datetime import datetime


def create_table():
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    # Resume history table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resume_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            resume_name TEXT,
            ats_score REAL,
            skills_found TEXT,
            missing_skills TEXT,
            top_job TEXT,
            match_percent REAL,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False


def login_user(username, password):
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        return True
    return False


def insert_record(username, resume_name, ats_score, skills_found, missing_skills, top_job, match_percent):
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()

    created_at = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    cursor.execute("""
        INSERT INTO resume_history (username, resume_name, ats_score, skills_found, missing_skills, top_job, match_percent, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (username, resume_name, ats_score, skills_found, missing_skills, top_job, match_percent, created_at))

    conn.commit()
    conn.close()


def fetch_records(username):
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM resume_history WHERE username=? ORDER BY id DESC", (username,))
    data = cursor.fetchall()

    conn.close()
    return data

def clear_history(username):
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM resume_history WHERE username=?", (username,))

    conn.commit()
    conn.close()

def delete_record(record_id):
    conn = sqlite3.connect("resume_analyzer.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM resume_history WHERE id=?", (record_id,))

    conn.commit()
    conn.close()