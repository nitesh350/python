# to find sub strin in a string 
str=input("enter the whole sentences :")
str1=str
sub_str=input("enter words to find from sentences :")
if (str1.find(sub_str) == -1):
    print("enter word",sub_str,"is not found")
else:
    print("enter word",sub_str,"is found")


## to find sub strin in a string using function
def str() :
    if (str1.find(sub_str) == -1):
        print("enter word",sub_str,"is not found")
    else:
        print("enter word",sub_str,"is found")

str1=input("enter the whole sentecnces :")
sub_str=input("enter the word to find :")
str()

## to find multipcation using function
def multiplication(num) :
    for i in range(1,20):
        print(num,"*",i,"=>",num*i )

aa=int(input("enter the number for multiplication table ::"))
multiplication(aa)

# to find odd even and postive negavtive number s

def pos_neg(number_1):
    if number_1>= 0:
        print("enter number",number_1,"is postivenumber")
    else:
        print("enter number",number_1,"is negative number")

def odd_even(number_2):
    if number_2%2 == 0:
        print("enter number",number_2,"is even")
    else:
        print("enter number",number_2,"is odd")

aa=int(input("enter the number ::") )
pos_neg(aa)
odd_even(aa)

# finding sub string in string 
def string(stringg_2):
    string_1 =("my name is nitesh ")
    if (string_1,find(string_2)==-1):
        print("no word matched")
    else:
        print("word matsched ")

string_2 =input("enter the word :")
string(string_2)

# qs 
def string():
    string_1 =("my name is nitesh ")
    if (string_1.find(string_2)==-1):
        print("no word matched")
    else:
        print("word matched ")

string_2 =input("enter the word :")
string()
