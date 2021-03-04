# def welcome(name):
#     print(f"welocme home {name}")

# def bye(name):
#     print(f"bye bye {name}")

# def function(abc):
#     abc("nitesh")  # refreence 

# function(welcome)
# function(bye)


# # example two :
# def welcome(name):
#     print(f"welocme home {name}")

# def bye(name):
#     print(f"bye bye {name}")

# def function(abc, name):
#     abc(name) 

# function(welcome,"hari")
# function(bye,"shyam")


# 

# def decorater_function(abc):
#     def wrapper():
#         print("this is first function")
#         abc()
#         print("this is end function ")
#     return wrapper


# @decorater_function
# def deco_function():
#     print("this is midddle function ")

# deco_function()

#use of decorater function 

def smart_divison(func):
    def wrapper(a,b):
        if b <= 0 and a>b:
            return ("could not divide")
        else:
            return func(a,b)
    return wrapper

@smart_divison
def divison(a , b):
    return a / b


print(divison(10,0))

print(divison(10,5))
print(divison(10,-1))


#








