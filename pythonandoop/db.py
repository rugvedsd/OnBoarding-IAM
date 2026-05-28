import sqlite3

# conn = sqlite3.connect(':memory:')
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE users(name TEXT, age INTEGER)')
# cursor.execute("INSERT INTO users VALUES('Rugved', 22)")
# conn.commit()

# cursor.execute('SELECT * FROM users')
# result = cursor.fetchone()
# print(f'User: {result[0]}, Age: {result[1]}')


# import sqlite3

# conn = sqlite3.connect(':memory:')
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE users (name TEXT, age INTEGER)')
# cursor.execute("INSERT INTO users VALUES ('Tobias', 28)")
# conn.commit()

# cursor.execute('SELECT * FROM users')
# result = cursor.fetchone()
# print(f'User: {result[0]}, Age: {result[1]}')

from fastapi import FastAPI
from pydantic import BaseModel

import sqlite3
from loguru import logger


app = FastAPI()

DATABASE_NAME = "employees.db"


# -----------------------------
# DATABASE CONNECTION
# -----------------------------
def create_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


# -----------------------------
# CREATE TABLE
# -----------------------------
def create_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fname TEXT NOT NULL,
        mobile_number TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        salary INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()

    logger.info("Employees table created successfully")


# -----------------------------
# INSERT EMPLOYEE
# -----------------------------
def insert_employee(fname, mobile_number, email, address, salary):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO employees (
        fname,
        mobile_number,
        email,
        address,
        salary
    )
    VALUES (?, ?, ?, ?, ?)
    """, (fname, mobile_number, email, address, salary))

    conn.commit()
    conn.close()

    logger.info("Employee inserted successfully")


# -----------------------------
# FETCH EMPLOYEES
# -----------------------------
def fetch_all_employees():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    conn.close()

    return employees


# -----------------------------
# PYDANTIC MODEL
# -----------------------------
class Employee(BaseModel):
    fname: str
    mobile_number: str
    email: str
    address: str
    salary: int


# -----------------------------
# CREATE TABLE ON STARTUP
# -----------------------------
create_table()


# -----------------------------
# ADD EMPLOYEE API
# -----------------------------
# @app.post("/add/employee")
# def add_employee(emp: Employee):

#     insert_employee(
#         emp.fname,
#         emp.mobile_number,
#         emp.email,
#         emp.address,
#         emp.salary
#     )

#     return {
#         "message": "Employee added successfully",
#         "employee": emp
#     }


# # -----------------------------
# # GET ALL EMPLOYEES API
# # -----------------------------
# @app.get("/employees")
# def get_all_employees():

#     employees = fetch_all_employees()

#     return {
#         "employees": employees
#     }