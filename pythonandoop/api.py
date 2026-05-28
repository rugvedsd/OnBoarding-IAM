from fastapi import FastAPI
from uvicorn import run
from module import Employee, get_all_data, name, mobile_number, salary, email, address

app = FastAPI()

@app.get("/")
def read_root():
    return {"Welcome to Employee Management System"}

@app.get("/edit/employee")
def read_empData():
    # get_all_data()
    return {"Please enter your details": f"{name()}, {mobile_number()}, {email()}, {address()}, {salary()}"}

@app.post("/add/employee")
def add_employee():
    
    employee_data = get_all_data()

    emp = Employee(
        employee_data["fname"],
        employee_data["mobile_number"],
        employee_data["email"],
        employee_data["address"],
        employee_data["salary"]
    )

    return {
        "Employee added successfully":
        emp.display_employee_info()
    }

# @app.post("/add/employee")
# def add_employee():

#     employee_data = get_all_data()

#     emp = Employee(
#         employee_data["name"],
#         employee_data["mobile_number"],
#         employee_data["email"],
#         employee_data["address"],
#         employee_data["salary"]
#     )

#     return {
#         "Employee added successfully":
#         emp.display_employee_info()
#     }
