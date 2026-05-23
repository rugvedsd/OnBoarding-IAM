import sqlite3 

def get_conn():
    conn = sqlite3.connect('employee.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        empId INTEGER PRIMARY KEY AUTOINCREMENT, 
        empName TEXT NOT NULL, 
        empEmail TEXT NOT NULL,
        empDept TEXT NOT NULL,
        empRole TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()