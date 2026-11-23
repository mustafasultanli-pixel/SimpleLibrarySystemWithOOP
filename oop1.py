# product1Name = "Laptop"
# product1Price = 1500
# product1Stock = 5

# product2Name = "Mouse"
# product2Price = 100
# product2Stock = 10

# def showProduct(name,price,stock,productColor):
#     print(f"Name: {name}")
#     print(f"Price: {price}")
#     print(f"Stock: {stock}\n")
#     print(f"Color: {productColor}\n")


# # # OOP - OBJECT ORIENTED PROGRAMMING
# class Student:
#     name = "Arif" # field or property
#     age = 5

# s1 = Student() # object or instance)
# s2 = Student() # object or instance)

# print(s1.name, s1.age)
# print(s2.name, s2.age)


# class Student:
#     # cpnstructor (_init_) - object yaradilarken chagirilan methoddur
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age

#     def showInfo(self):
#         return f"Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}"


# s1 = Student("Eli", "Xasiyev", 18)
# s2 = Student("Adem", "Hesenzade", 16)

# for i in s1,s2:
#     print(i.showInfo())


'''
Car class'i yaradin.

properties: brand, model, year, color, price

'''

# class Car:
#     def __init__(self, brand, model, year, color, price, speed):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color
#         self.price = price
#         self.speed = speed

#     def showInfo(self):
#         return f"Brand: {self.brand}\Model: {self.model}\nYear: {self.year}\nColor: {self.color}\nPrice: {self.price}\nSpeed: {self.speed}"

#     def increaseSpeed(self, speedAmount):
#         self.speed+= speedAmount

# c1 = Car("BMW","F30",2014,"Black",28000,200)
# c2 = Car("Lamborghini","aventador",2015,"Red",1000000,300)
# c3 = Car("Buggati","W16",2010,"Blue",1500000,350)

# for i in c1,c2,c3:
#     print(i.showInfo())