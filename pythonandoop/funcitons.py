from db import create_table
from module import get_all_data
from loguru import logger
from uvicorn import run

if __name__ == "__main__":
    create_table()                   #   ensure table exists first
    employee = get_all_data()
    if employee:                     #   guard against None
        employee.display_employee_info()
    else:
        logger.error("Employee creation failed.")
    run("api:app", host="0.0.0.0", port=8000, reload=True)