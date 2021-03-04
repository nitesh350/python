# # # # # # loop
# # # # # #syntax
# # # # # #for variable in <iterable-object>:
# # # # #      # block of code 
# # # # #      # block of code
    


# # # # # # a =["php","java","python","html","css"]
# # # # # # b =["biker-world","physics- men","attendance","e-commerce"]
# # # # # # for i in a:
# # # # # #     print(i)
# # # # # # for j in b:
# # # # # #     print(j)
# # # # # # for i in b:
# # # # # #     print(i)

# # # # # # for i in range(100):
# # # # # #     print(i)


# # # # # range(start,stop,step):

# # # # # for i in range(2,50,3):
# # # # #     print(i)


# # # # #take user input 10 times and print then 

# # # # # for user in range(11):
# # # # #     n = input("enter the name")
# # # # #     print(n)

# # # # user1 =[]
# # # # for i in range(10):
# # # #     n=input("enter the value :")a
# # # #     user1.append(n)

# # +# # print(user1)

# # #wap to ask interger from user and add aalll list value
# # alist =[]
# # total_sum = 0 
# # for i in range(10):
# #     num = int(input("enter the numbers :"))
# #     alist.append(num)
# #     total_sum = total_sum+num
   
# # print(alist)
# # print(total_sum)


# # new qs task
# print(".................................................................................")
# heros=["spider man","thor","hulk","iron man","captain america"]
# a=len(heros)
# print("the lenght of the list heros is :",a)

# heros.insert(6,"black panter ") # here i inserted data black panter in list
# print("heros list after adding is = ",heros)

# heros.insert(3,heros.pop()) # sir process 
# # value = heros.pop(5)  
# # heros.insert(3,value)
# print("list after adding black panter after hulk : ",heros)

# del heros[1:3]
# heros.insert(4,"dr.strange")
# print("list after delteing angery characters ::",heros)

# heros.sort()
# print(heros)

# print("......................................................................................")

# #qs 3

# # Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
# print("..............................................................................")


# print("..............................................................................")

# # qs1 

# print("Expenses of the months are: \n1.January - 2200 \n2.February - 2350  \n3.March - 2600 \n4.April - 2130 \n5.May - 2190")
# montly_expense = [2200,2350,2600,2130,2190]

# heros = ['spider man','thor','hulk','iron man','captain america']
# print("the lenght of the lis is :",len(heros))

# heros.append("black panter ")
# print("new list after adding black panter :",heros )

# heros.insert(3,heros.pop())
# print("new list after adding black panter after hulk :",heros)

# # heros[1:3]=["dr strange"]
# # print("new list after adding dr strange :", heros)

# # heros.sort()
# # print("list in ascending order :",heros)

# # qs two 
# montly_expense = [2200,2350,2600,2130,2190]

# print("In feburary i spend ",montly_expense[2]-montly_expense[1], "more than january")
# print("my total expenses of first quater months is ",sum(montly_expense[:3]) )
# montly_expense.append(1900)
# print("list after adding expense of june is :",montly_expense)
# montly_expense[3]= montly_expense[3]-200
# print(montly_expense)

# # unknown_value = int(input("enter the expenses to known month:"))
# # if unknown_value!= montly_expense :
# #     print(" not  found ")
# # else:
# #     print("found ")

# #qs 3
# numb = int(input("enter the max number :"))
# alist =[]
# for i in range(1,numb,2):
#     alist.append(i)

# print(alist)

# #
# main_list =[]
# even_list =[]
# odd_list =[]
# dublicate = []
# for num in range(10):
#     num = int(input(" enter the numbers :") )
#     main_list.append(num)


# for num in main_list:
#     if num % 2 == 0:
#         even_list.append(num)
    
#     elif num % 2 != 0:
#         odd_list.append(num)

#     elif num in not main_list:
#         dublicate.append(num)
#     else:
#         print("not found ")

# print("this list conatain all user input numbers : ",main_list)
# print("this list contain all even numbers from list :",even_list)
# print("this list contain all odd numbers from list :", odd_list)
# print("this list contain all dublicate elments from list :",dublicate)

# sir way 
main_list =[]
even_list =[]
odd_list =[]
dublicate = []
for i in range(10):
    num = int(input("enter the numberss :"))
    if num not in main_list:
        if num % 2 == 0:
            even_list.append(num)
        else :
            odd_list.append(num)
    else :
        dublicate.append(num)
    main_list.append(num)

print(f" main list : {main_list} ")
print(f" even list : {even_list} ")
print(f" odd list : {odd_list} ")
print(f" dublicate list : {dublicate} ")




# if main_list[0]%2 == 0:
#     print("even")
# else:
#     print("odd")




# def even(num):
#     return num%2 == 0


# def odd(num):
#     return num%2 != 0

# def (num):
#     return num == num 
















    

    






















