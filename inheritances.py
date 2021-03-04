# class bird:
#     def __init__(self,name,colour):
#         self.name= name
#         self.colour = colour

#     def beautiful(self):
#         print(f"{self.name} is beautifull .")

# class pigeon(bird):
#     def __init__(self,name,colour):
#         #
#         super().__init__(name,colour)

#     def beautiful(self):
#         super().beautiful()
#         print(f"{self.name} of {self.colour}colour is beautiful..")

# class parrots(bird):
#     def __init__(self,name,colour):
#         super().__init__(name,colour)
    
#     def fly(self):
#         print(f"{self.name} is awsome beautiful..")


# p = pigeon("saugat","white")
# p.beautiful()
# #print("pigeon",p.name,p.colour)

# pp = parrots("chetan","black")
# pp.beautiful()
# #print("parrots",pp.name,pp.colour)

# #..............................................................................


class user:
    def __init__(self,_id,username,password):
    self._id = _id
    self.username = username
    self.password = password

    def login(self,username,password):
        if self.username == username and self.password == password:
            print("loggin succesful..")
        else:
            print("login invalid..")

class person(user):
    def __init__(self,_id,username,password,name,contact,address):
        super().__init__(_id,username,password,)
        self.name = name
        self.contact = contact
        self.address = address

    def display_profile(self):
            """
            _id,user-name,password,name,conatct,address
            if object is student- also print course
            if object is taecher - alos print desgination

            """
            print(f"_id{self._id}")
            print(f"username :"{self.username})
            print(f"name: {self.name}")
            print(f"contact :{self.contact}")
            print(f"address: {self.address}")

class student(person):
    def __init__(self,_id,username,password,name,contact,address,course):
        supersuper().__init__(_id,username,password,name,contact,course)
        self.course = course
    
    def display_profile(self):
        super().display_profile()
        print(f"{self.course}")
        

class teacher(person):
    def __init__(self,_id,username,password,name,contact,address,designation):
        super().__init__(_id,username,password,name,contact,address)
        self.designation= designation
    
    
    def display_profile(self):
        super().display_profile()
        print(f"{self.desgination}")
        





