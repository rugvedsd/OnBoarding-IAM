from fastapi import FastAPI
from pydantic import BaseModel
from module import Employee          #   imported
from db import insert_employee       #   imported

app = FastAPI()

class EmployeeRequest(BaseModel):
    fname:         str
    mobile_number: str
    email:         str
    address:       str
    salary:        int

@app.post("/add/employee")
def add_employee(data: EmployeeRequest):
    emp = Employee(
        data.fname,
        data.mobile_number,
        data.email,
        data.address,
        data.salary
    )
    insert_employee(
        data.fname,           #   fixed from data.name
        data.mobile_number,
        data.email,
        data.address,
        data.salary
    )
    return {"message": "Employee added successfully", "name": emp.name}

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
