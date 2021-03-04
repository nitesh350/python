# def some_function(x,y,*passs):
#     print(x + y,passs )


# num = int(input("enter the number "))
# num2 = int(input("enter the number :"))
# print(some_function(num,num2,23232323))





# def some_function(*soo, **okaybye):
#     print( soo )
#     print(okaybye)
# some_function("python","java",name = "nitesh",address= "ktm")



# nested function::: 
# a = 5 # yo golvbal scope
# def fun():
#     a = 10 # yo local scope 
#     return a

# fun()
# print(a)   



# def some_function():
#     return 100


# call for execution 
# res = some_function()
# print(res)


# call by reference

# res = some_function
# print(res())  # some_function  



# def outer_fun(): # nested function 
#     print("i am outer function :")
#     def inner_fun():
#         print("i am inner function :")
#     return inner_fun

# infunc = outer_fun()
#infunc()

# outer_fun()() # another way 


#closure fucnction


# def multiplier(n):
#     def multiply(a):
#         return a * n
#     return multiply

# time = multiplier(10)

# print(time(5))



# use of  global keyword:
# a = 100
# def function():
#     global a
#     n = a *100
#     print(f"value of n : {n}")

# function()

# 
# alist = []

# def func():
#     alist.append(50)
#     print(alist)

# func()


# blist = [1,2,3,4,5,6]

# def func1():
    
#     clist = blist[0:3]
#     clist.append(20)
#     print(clist)

# func1()



# def outer():
#     a = 1000
#     def inner():
#         nonlocal a
#         a = a + 1
#         print(a)
#     inner()


# # outer()
# def smater_divison(pas):
#     def inner(x,y):
#         if y == 0:
#             return("no divison")
#         else:
#             return pas(x,y)
#     return inner

# @smater_divison
# def division(x,y):
#     return x/y

# print(division(10,0))        

# def function1():
#     x = 100
#     print("okay done")
#     def function2():
#         y = 200
#         return x +y
#     return function2

# a = function1()
# print(a())

# def function2(arg):
#     print("hellow  i am first argu")
#     def function3():
#         x = function1
#         return x +20000
#     return function3

# def smartdivison(abc):
#     def inner(a,b):
#         if b == 0:
#             return ("not divided by zero")
#         else:
#             return abc(x,y)
#     return inner

# @smartdivison
# def divison(a,b):
#     return a / b

# print(divison(10,0) )

# def upperr(func):
#     def inner():
#         abc = func()
#         return abc.upper()
#     return inner
# def split(func):
#     def inner_2():
#         abc= func()
#         return abc.split()
#     return inner_2
# @split
# @upperr     
# def simple():
#     return "i belive on u"

# print(simple())



#   touch(higher order function ):
# map
# syntax:
#map(function name, iterable object)

# def increse_by2(n):
#     return n +2
# alist = [1,2,3,4,5,6,7]  # here we craeted a list
# blist = list(map(increse_by2,alist)) # here we called map function
# print(blist)

# same soln using lambda function
# alist = [1,2,3,4,5,6,7]  # here we craeted a list
# blist = list(map(lambda n : n+2,alist)) # here we solve same qs by lambda function
# print(blist)


# filter 
#lambda  used for instance used 
    #syntax of lamnda:
   # lambda x,y here x y is parameter : x +y (x+y) is reusltt
# a = lambda x,y: x*y
# print(a(10,5))


# email = ["ram_gmail.com","hari_gmail.com","sita_gmail.com"]  # qs giviven by sir

# newmail = list(map(lambda e:e.replace("_","@"),email) )
# print(newmail)

# namelist = ["ram","hari","gita"]
# name2list = list(map(lambda y:y.capitalize(),namelist))  # qs 2 sir
# print(name2list)

# numbers = ["12","25","30"]
# #numbers2 = list(map(int,numbers)) 
# numbers2 = list(map(lambda n:int(n),numbers))
# print(numbers2)



# fliter function
# a= [1,2,3,4,5,6,7,8]
# even = list(filter(lambda n:n %2==0,a))
# print(even)



# email = ["a@gmail.com","b@gmail.com","c@hotmail","d@okaymail"]

# gmail = list(filter(lambda n:n.endswith("@gmail.com"),email))
# print(gmail)


a=list(map(lambda x,y,z : (x*y)+z,range(1,10),range(1,11),range(1,11) ))
print(a)
b = list(filter(lambda x:x<=40,a))
print(b)
c =list(map(lambda x : x+1,range(1,20)))
print(c)
d= tuple(filter(lambda x : x%2==0,c))
print(f"odd numbers {d}")
a.append(40)
print(a)


