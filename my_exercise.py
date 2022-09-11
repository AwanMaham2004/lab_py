#! /usr/bin/env python

"""
1) Write a Python function to find the Max of three numbers. # if condition
2) Write a Python function to sum all the numbers in a list. # for condition #addition
3) Write a Python function to multiply all the numbers in a list. # for condition #multiplication
4) Write a Python program to reverse a string. # while condition
5) Write a Python function to calculate the factorial of a number
(a non-negative integer). The function accepts the number as an argument. # if/else statement, factorial(n-1) 
6) Write a Python function to check whether a number falls in a given range. # if/else statement
7) Write a Python function that accepts a string and calculate the number of upper case letters and lower 
case letters. # if/else statement, for loop
8) Write a Python function that takes a list and returns a new list with unique elements of 
the first list. # for loop, if statement, append method
9) Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors
 other than 1 and itself. # if statement, for loop
10) Write a Python program to print the even numbers from a given list. # for loop, if statement, append method
11) Write a Python function to check whether a number is perfect or not. # if condition, range method
12) 
"""


from operator import truediv
import sys
from tkinter import N

"""
factorial(n-1) # mathematic algotrith in factorials

"""

# Ex.1)

# def max_of_two(x, y):
#     if x>y:
#         return x
#     return y
# def max_of_three(x, y, z):
#     return max_of_two(x, max_of_two(y, z))
# print(max_of_three(2, 5, 17))


# Ex.2)

# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((2, 5, 7, 8, 3, 5)))


# Ex.3)
# def mult(numbers): # Mathematical comparison # Another variant with value defined  
#    total = 1
#    for x in numbers:
#        total *= x
#    return total
# print(mult((7, 6, 5, 4, 3, 2, 1)))


# Ex.4)
# def string_reverse(str1):
#     rstr1 = ''
#     index = len(str1)
#     while index > 0:
#         rstr1 += str1 [index - 1]
#         index = index - 1
#     return rstr1
# print(string_reverse('abcdefg'))


# Ex.5)
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Give an argument : "))
# print(factorial(n))



# x = (7*6*5*4*3*2*1) # Regular mathematical comparison
# print (x)


# Ex.6)
# def test_range(n):
#     if n in range(3,9):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(2)


# Ex.7 

# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])

# string_test('The Quick Brown Fox')


# Ex.8

# def unique_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x

# print(unique_list([1,2,3,3,3,3,4,5])) 


# Ex.9

# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True             
# print(test_prime(9))


#Ex. 10

# def is_even_num(l):
#     enum = []
#     for n in l:
#         if n % 2 == 0:
#             enum.append(n)
#     return enum
# print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# Ex.11

# def perfect_number(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     return sum == n
# print(perfect_number(6))













