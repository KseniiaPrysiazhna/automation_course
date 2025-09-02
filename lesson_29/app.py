import os
import psycopg2

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "testdb"),
    "user": os.getenv("DB_USER", "user"),
    "password": os.getenv("DB_PASS", "pass"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": 5432,
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age INT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


def insert_user(name, age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s) RETURNING id;", (name, age))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id


def update_user(user_id, new_age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET age = %s WHERE id = %s;", (new_age, user_id))
    conn.commit()
    cur.close()
    conn.close()


def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
    conn.commit()
    cur.close()
    conn.close()


def select_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


if __name__ == "__main__":
    create_table()
    print("Таблиця створена. Можна запускати тести.")