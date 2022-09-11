# fruits = ["Apples", "Bananas", "Mangoes"] # First way with variable
# me = fruits[1][:-3]
# print(me)

# fruits = ["Apples", "Bananas", "Mangoes"]
# for ele in (fruits):
#     print (ele)

# fruits = ["Apples", "Bananas", "Mangoes", "Apri"] # List2 append method

# for ele in fruits:
#     list2 = []
#     list2.append(fruits[1])
# print(str(list2))


# fruits = ["Apples", "Bananas", "Mangoes", "Apri"] # List2 append method

# for ele in fruits:
#     list2 = []
#     list2.append(fruits)
# print(str(list2))


# list3 = [fruits for ele in fruits] # List comprehension
# print(list3)     






# for i in range(0, 26): # Use continue and break command
#     x = (i + i)
#     if x == 42: continue
#     #if x != 42: continue 
#     print(x)


#for i in range(0, 26): # Use continue and break command
#     x = (i + i)
#     if x == 42: continue
#     #if x != 42: continue 
#     print(x)

# i = list(range(0, 25))
# list3 = [ele + ele for ele in i]    # List comprehension != If statement 
# print(list3)

    

# for num in range(0, 101):
#     print(num)







# y = []
# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for ele in num:
#     y.append(num) 
# print(y)



# start = 2
# end = 100

# for x in range(start, end+1):
#     # if x>1:
#         for y in range(2, x):
#             if (x % y==0):
#                 break
#         else: 
#             print(x)


# start = 2
# end  = 100

# for x in range(start, end+1):
#     if x>1:
#         for y in range(2, x):
#             if (x % y==0):
#                 break
#         else:
#             print(x)



# for x in range(0, 100): # 2nd method to calculate Primzahlen
#     if x>1:
#         for y in range(2, x):
#             if (x % y==0):
#                 break
#         else:
#             print(x)


start = 2
end = 100

list3 = [(x % y==0) for x in range(start, end+1) for y in range(2, x)] 

print(list3)



























