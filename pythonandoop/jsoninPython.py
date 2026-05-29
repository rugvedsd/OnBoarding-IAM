# import json 

# x = '{ "name":"John", "age":30, "city":"New York"}'

# y = json.loads(x)

# print(y["age"])


# import json 

# x = {
#     "name": "Rugved",
#     "age": 22,
#     "city": "Pune"
# }

# y = json.dumps(x)

# print(y)

# import json 

# x ={
#     "id": 1 ,
#     "temprature": 28.0,
#     "humidity": 43,
#     "PM2p5": 3,
#     "hcho": 3,
#     "tvoc": 3,
#     "co2": 1225
# }

# y = json.dumps(x, indent=2, separators=(",", "="))

# print(y)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello my name is {self.name} and my age is {self.age}")

# p1 = Person("Rugved", 21)    

# p1.greet()

# from jsondata import brandName, brandClothType, brandQuantity
# from loguru import logger

# class Brand:
#     def __init__(self, name, type, quantity):
#         self.name = name
#         self.type = type
#         self.quantity = quantity

#     def brandData(self):
#         print(f"Brand delivery recived is {self.name}, which has {self.quantity} and the the cloths are {self.type}")

# b1 = Brand(brandName, brandClothType, brandQuantity)
# b1.brandData
# logger.info(b1.brandData)

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def displayinfo(self):
        print(f"This is {self.model} by {self.brand} built in {self.year}")

c1 = Car("Toyota", "Corola", 2025) # the arguments are arranged as per the paramters defined by method 
c1.displayinfo()


class Reactangle: 
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

r1 = Reactangle(5, 2)
print(r1.area())