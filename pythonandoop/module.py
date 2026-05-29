from loguru import logger
from db import insert_employee   #   imported

class Employee:                  #   defined BEFORE get_all_data()
    def __init__(self, fname, mobile_number, email, address, salary):
        self.name          = fname
        self.mobile_number = mobile_number
        self.email         = email
        self.address       = address
        self.salary        = salary

    def display_employee_info(self):   #   uncommented
        print(f"Name:          {self.name}")
        print(f"Mobile Number: {self.mobile_number}")
        print(f"Email:         {self.email}")
        print(f"Address:       {self.address}")
        print(f"Salary:        {self.salary}")


def name():
    fname = input("Please enter your name: ").strip()
    if fname.isalpha():
        logger.info(f"Your name is: {fname}")
        return fname
    else:
        logger.error("Invalid name. Alphabetic characters only.")
        return None

def mobile_number():
    mobile = input("Please enter your mobile number: ").strip()
    if mobile.isdigit() and len(mobile) == 10:
        logger.info(f"Your mobile number is: {mobile}")
        return mobile
    else:
        logger.error("Invalid mobile. Must be 10 digits.")
        return None

def email():
    email_input = input("Please enter your email address: ").strip()
    if "@" in email_input and "." in email_input:   #   real validation
        logger.info(f"Your email: {email_input}")
        return email_input
    else:
        logger.error("Invalid email address.")
        return None

def address():
    addr = input("Please enter your address: ").strip()
    if addr:
        logger.info(f"Your address: {addr}")
        return addr
    else:
        logger.error("Address cannot be empty.")
        return None

def salary():
    sal = input("Please enter your salary: ").strip()
    if sal.isdigit():
        logger.info(f"Your salary: {sal}")
        return int(sal)
    else:
        logger.error("Invalid salary. Must be numeric.")
        return None

def get_all_data():
    fname        = name()
    mobile       = mobile_number()
    email_id     = email()
    addr         = address()
    salary_value = salary()

    if not all([fname, mobile, email_id, addr, salary_value]):
        logger.error("Employee creation failed due to invalid input.")
        return None

    employee = Employee(fname, mobile, email_id, addr, salary_value)  #   once only

    try:
        insert_employee(
            employee.name,
            employee.mobile_number,
            employee.email,
            employee.address,
            employee.salary
        )
    except Exception as e:
        logger.error(f"Database insertion failed: {e}")
        return None

    return employee