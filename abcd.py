def string():
    string_1 =("my name is nitesh ")
    if (string_1.find(string_2)==-1):
        print("no word matched")
    else:
        print("word matched ")

string_2 =input("enter the word :")
string()

print("....................................................")


def string():
    string_1 =("my name is nitesh ")
    if (string_1.find(string_2)==-1):
        print("no word matched")
    elif (string_1.find(string_2)==0):
        print("no word entred")
    else:
        print("word matched ")

string_2 =input("enter the words:")
string()

print("..............................................")


def persanal_info(name,address,contact_no,country,salary):
    print("employer name is : ",name)
    print("employer contact is :",contact_no)
    print("employer country is: ",country)
    print("employer address is :",address)
    print("empoyer salary is: ",salary)

aa=input("name:")
bb=input("contact number:")
cc=input("salary :")
dd=input("country :")
ee=input("address :")

persanal_info(aa,contact_no=bb,salary=cc,country=dd,address=ee)

print("..............................................................")

def divi(num):
    if num%5 == 0 and num%10 == 0 :
        print("number is divisble by 5 and 10 ")
    else:
        print("number is not divisble by 5 and 10")

number=int(input("enter the number :"))
divi(number)
string()
persanal_info()


print(".................................................................")



