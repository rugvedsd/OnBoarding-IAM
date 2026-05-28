# def greet():
#     name = input()
#     print(f"Hello,{name}")

# greet()

# def page(x):
#     page  = str(input("Please enter the employee code: "))
#     if page == "HR":
#         print("Welcome to the HR page")
#     elif page == "IT":
#         print("Welcome to the IT page")
#     elif page == "Finance":
#         print("Welcome to the Finance page")
#     else:
#         print("Invalid employee code")



# def get_page():
#     page  = str(input("Please enter the employee code: "))
#     if page == "HR":
#         print("Welcome to the HR page")
#     elif page == "IT":
#         print("Welcome to the IT page")
#     elif page == "Finance":
#         print("Welcome to the Finance page")
#     else:
#         print("Invalid employee code")


# get_page()
# 
# import sys
# print(sys.getrecursionlimit()) 

# def my_generator():
#   yield 1
#   yield 2
#   yield 3
# 
# for value in my_generator():
#   print(value) 

# def count_up_to(n):
#   count = 1
#   while count <= n:
    # yield count
    # count += 1
# 
# for num in count_up_to(5):
#   print(num)


# range(start, stop, step)
# 
# for i in range(1, 10, 2):
    # print(i)
    # 

# x = range(1, 10)
# print(x)
# 
# for i in range(1, 10):
    # print(i)

# r = range(1, 10)
# print(r[2])
# print(r[:3])

# cars = ["Ford", "BMW", "Volvo"]
# x = cars[0]
# cars[0] = "Toyota"
# print(cars[0])
# 
# cars.append("Honda")
# print(cars)

from uvicorn import run
from db import create_table
from module import get_all_data


if __name__ == "__main__":
    create_table()
    # get_all_data()
    run("api:app",host="0.0.0.0",port=8000,reload=True)