import sqlite3
from loguru import logger

DB_NAME = "employee.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            fname         TEXT,
            mobile_number TEXT,
            email         TEXT,
            address       TEXT,
            salary        INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert_employee(fname, mobile_number, email, address, salary):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employees (name, mobile_number, email, address, salary)
        VALUES (?, ?, ?, ?, ?)
    """, (fname, mobile_number, email, address, salary))
    conn.commit()
    conn.close()
    logger.info("Employee data inserted successfully.")