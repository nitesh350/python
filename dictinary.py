# # # dictinary

# # # student = {"name":"nitesh","address":"nepal","number":"1234"} where name is hasable object
# # # print(student)

# # # # print(student["address"] )  # 


# # # # dictinary:
# # # # mappable obkject
# # # #hasable object
# # # print(hash('a') )

# student = {"name":"nitesh","address":"nepal","number":"1234"}
# print(student.get("name") )
# print(student.get("nam","ram"))
# print(student.items())
# print(student.keys())
# print(student.values())

# for val in student.values():
#     print(val)

# for keyy in student.keys():
#     print(keyy)

# for key , value in student.items():
#     print(key , value)


# print(key)


# student = {"name":"nitesh","address":"nepal","number":"1234"}


# student["gender :"]= "male"
# print(student)

# student.pop("address")
# print(student)

# student["name"]= "nitesh shrestha "
# print(student)


#day2 dictinary 


# a = {}

# p = a.fromkeys(["name", "address "],"unknown")
# print(p)


student = {"name":"nitesh","address":"rato bhalay","number":1212121}
# print(student.get("email","unknown") )  # here get will not create email in dicictinary  (get)
# print(student.setdefault("email","unknown ")) # here email will be assigend to dictinary permanetly  (setdefault)
# print(student)

# in pop we should pass arugement 
# in pop iteam  lay sidhai last ko remove garcha 


# pp = student.pop("name")
# print(pp)
# ppp= student.popitem()
# print(ppp)
# print(student)



student.update({"email":"sita@1gmail","age":12})
print(student)