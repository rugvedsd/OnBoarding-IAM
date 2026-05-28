from loguru import logger


def name():
    fname = str(input("Please enter your name: "))
    if fname.isalpha():
        logger.info(f"Your name is: {fname}")
        return fname
    else:
        logger.error("Invalid input for name. Please enter a valid name consisting of alphabetic characters only.")

def mobile_number():
    mobile_number = input("Please enter your mobile number: ")
    if mobile_number.isdigit() and len(mobile_number) == 10:
        logger.info(f"Your mobile number is: {mobile_number}")
        return mobile_number
    else: 
        logger.error("Invalid input for mobile number. Please enter a 10-digit numeric value.")

def email():
    email = input("Please enter your email address: ")
    if email + "@gmail.com":
        logger.info(f"Your email address is: {email}")
        return email
    else:
        logger.error("Invalid input for email. Please enter a valid email address.")

def address():
    if True:
        address = input("Please enter your address: ")
        logger.info(f"Your address is: {address}")
        return address
    else:
        logger.error("Invalid input for address. Please enter a valid address.")

def salary():
    salary = input("Please enter your salary: ")
    if salary.isdigit():
        salary = int(salary)
        logger.info(f"Your salary is: {salary}")
        return salary
    else:
        logger.error("Invalid input for salary. Please enter a numeric value.")

def get_all_data():
    fname = name()
    mobile_number()
    email()
    address()
    salary()


class Employee:
    def __init__(self, fname, mobile_number, email, address, salary):
        self.name = fname
        self.mobile_number = mobile_number
        self.email = email
        self.address = address
        self.salary = salary
        
    def display_employee_info(self):
        print(f"Name: {self.fname}")
        print(f"Mobile Number: {self.mobile_number}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print(f"Salary: {self.salary}")