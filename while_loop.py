# # # # # # type sof loop :
# # # # # # bounded loop : starting point and ending point is fix 
# # # # # # unbounded loop: not fix how may times program runs untill the code is run 

# # # # # syntax:
# # # # # while <condition>:
# # # # #     #bloack code 
# # # # #     #bloack code 

# # # # # qs 2
choice = "y"
while choice == "y":
    num1 = int(input("enter any numbers :") )
    num2 = int(input("enter any numbers :") )
    print(f"sum of {num1} and {num2} is {num1+num2}.")
    choice = input("do you want futher calculation (y/n) :")


# # # # # qs 2
# # # # ask user password untill user input(abcde)
# # # # if pasword is coreect print sucess


# password = input("enter the passwordssss :")
# while password != "abcde123":
#     password = input("enter the passwordssss :")
# print("sucessful")



# #   2.break 
# #   1.continue


# for i in range(1,10):
#     print(f"before break : {i} ")
#     if i%2 == 0:
#         break
#     print(f"after break {i} ")

# print("..."*20)

# for i in range(1,10):
#     print(f"before continue : {i} ")
#     if i%2 == 0:
#         continue 
#     print(f"after continue:{i} ")


# # for 
# # else 
for i in range(1,10):
    if i % 3 == 0:
        break
    print(i)
else:
      print("loop completed..")

# # while 
# # else 

