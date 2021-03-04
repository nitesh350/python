# # class and object
    # noun -> object
    # adjective -> attribute(property)(stat)
    # verb/action -> behaviour(method)

# inheritances
# encapsulation (data hiding procees)
# polymorphisum
# abstrcation
# acess modifier
# accessor and mutator(function)


# 1.class and object

# class car:
#     #initializer function 
#     def __init__(self,color,model):
#         self.color = color
#         self.model = model
    
#     def start(self):
#         print("car started.")

# bmw = car("black","BMW0001N")
# print(bmw.__dict__)  # gives output in dictinary from
# bmw.start()


# audi = car("red","AUDI201")
# print(audi.__dict__)
# audi.start()

# mercides = car("white/grey","MER2122")
# print(mercides.__dict__)
# audi.start()


# class product():
#     def __init__ (self,name,price,qty):
#         self.name = name
#         self.__price = price # name managling
#         self.qty = qty
#     @property 
#     def price(self):
#         return self.__price
    
#     @price.setter
#     def price(self,price):
#         if price >0:
#             self.__price = price
#         else:
#             raise ValueError("price can be less than zero ")
    
#     def __str__(self):
#         return f"{self.name}  / {self.price}"
    
#     def __eq__(self,obj):
#         return self.qty == obj.qty


# tshirt = product("T-shirt",10000,5)
# pant = product ("pant",2000,5)
# print(tshirt == pant)
# print(tshirt)
# print(pant)

#print("price before:",tshirt.price)
# # print(tshirt.__dict__)
# try:
#     tshirt.price = -1
# except ValueError as err:
#     print(err)
# tshirt.price = 500
# print("price after :",tshirt.price)

# class student():  #statics variable topics 
#     #static or class variable 
#     collage_name = "abc colllage"
#     def __init__(self,_id,name):
#         #instances varibale
#         self.identification = _id 
#         self.name_of_student = name
    
# st = student(1,"ram")
# st2= student(2,"hari")
# print(st2.collage_name)

# class caculator():
#     def __init__(self,number,number2):
#         self.num1= number
#         self.num2= number2
    
#     def add(self):
#         return self.num1+self.num2
#     def subtract(self):
#         return self.num1-self.num2
#     @staticmethod
#     def square_root(num):
#         return num**0.5

# c = caculator(20,30)
# print(c.add())
# print(c.subtract())
# print(caculator.square_root(25)) # here we can call with class name caculator  and also with with c also




#..........................................................................................................

