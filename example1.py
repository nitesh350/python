def simple_calulator(num_1,numb_2):
    if output == "multiply":
        multi=(num_1*numb_2)
        print("the multipy of ",num_1,"and",numb_2,"is",multi)
    elif  output =="addtinal":
        add=(num_1+numb_2)
        print("the addtinal of ",num_1,"and",numb_2,"is",add)
    elif output =="subtraction":
        sub=(num_1-numb_2)
        print("the subtraction of ",num_1,"and",numb_2,"is",sub)
    elif output =="division":
        divi=(num_1/numb_2)
        print("the divison of ",num_1,"and",numb_2,"is",divi)
    else:
        print(" no operation found ")

    return()


number = int(input("enter first number :"))
number_2 = int(input("enter the second number :"))
output = input("which operation you want: multiply or addtinal or subtraction or division   : =  ")
print("user want",output,"operation")

simple_calulator(number, number_2)

# simple calculator

def addtion(x,y):
    return x + y

def subtraction(x,y):
    return x -y

def division(x,y):
    return x/y

def multipication(x,y):
    return x*y

num =   int(input("enter the first number :"))
num_2 = int(input("enter the second number :"))
print("1.addtion \n2.subtraction \n3.division \n4.multiplication")
choice=input("enter your choice :")

if choice =="1":
    print("sum",addtion(num,num_2))
elif choice =="2":
    print("subtraction",subtraction(num,num_2))
elif choice=="3":
    print("division",division(num,num_2))
elif choice =="4":
    print("multiplication",multipication(num,num_2))
else:
    print("not matched..")


# odd even and postive and negative 

def odd(numm):
    return(numm%2!= 0)

def even(numm):
    return(numm%2== 0)
def postive(numm):
    return(numm >= 0)
def negative(numm):
    return(numm >= -1)


numbers=int(input("enter the number :"))
print("which operation you want :odd or even or postive or negative ") 
operation=(input('entrt your choice of operation :'))

if operation =="odd" :
    print("odd number is :",odd(numbers))

elif operation =="even":
    print("even number is :",even(numbers) )
elif operation =="postive":
    print("postive number is :",postive(numbers) )
elif operation =="negative":
    print("negative number is :",negative(numbers) )
else:
    print("not matched...")












