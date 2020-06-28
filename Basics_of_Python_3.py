# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:08:36 2020

@author: User
"""

#METHODS:Methods perform specific actions on an object and can also take arguments, just like a function.
#The methods for a list are:append,count,extend,insert,pop,remove,reverse,sort
#Below are few examples for method

list=[1,2,3,4]
list.append(5)
list

list.count(2)

list.pop()
list

list.sort()
list

list.remove(2)
list

list.insert(2,5)
list

list.reverse()
list

#Functions:"groups together a set of statements so they can be run more than once. 
#They can also let us specify parameters that can serve as inputs to the functions.

def name_of_function (arg1,arg2):#Function syntax in Python
==========================================================================================================
#Program to print greetings
def greeting(name):
    print("Hello %s"%(name))
    
greeting("Rohith")
==================================================================================================================
#Program to add two numbers
def add(num1,num2):
    return num1+num2
add(3,5)
================================================================================================================
#Program to find number is prime or not

def is_prime(num):
    for n in range(2,num):
        if num%n==0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")
            
is_prime(23)

is_prime(2343)

==================================================================================================================================
#Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

def num(a,b):
    if a%2==0 and b%2==0:
        print(min(a,b))
    else:
        print(max(a,b))
    pass

num(3,6)

==================================================================================================================================
#Write a function takes a two-word string and returns True if both words begin with same letter

def string(text):
    wordsplit=text.split()
    return wordsplit[0][0]==wordsplit[1][0]

string('Rohith Rio')
=================================================================================================================================

#Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def num(a,b):
    return a+b==20 or a==20 or b==20
    pass

num(20,2)

====================================================================================================================================================
# To check the number is perfect square or not

number = 64

sqrt=number**(1/2)
if sqrt%1==0:
    print("Number is perfect square")
else:
    print("Number is not perfect")

=======================================================================================================================================
#Same program can be written as below:

def perfect_square(num):
    sqrt=num**(1/2)
    if sqrt%1==0:
        return True
    else:
        return False
    
perfect_square(64)
================================================================================================================================================================================

#To print prfect square between 1 to 1000

def is_perfect_square(num):
    sqrt=num**(1/2)
    if sqrt%1==0:
        return True
    else:
        return False
for i in range(1,1000):
    if is_perfect_square(i):
        print(i)
=============================================================================================================================================================================================================
#Program to double number
def double(a):
    return a*2

double(2)
===========================================================================================================================================================================
#program to add numbers

def add_numbers(num1,num2):
    return num1+num2
add_numbers(3,5)

def add(a,b,c):
    return a+b+c
add(1,2,3)

def add(*args):
    total=0
    for i in args:
        total+=i
    return total

add(1,2,3,4,4)

add(29249,3245,4353,35546)
============================================================================================================================================================================================================
#To find the factorial of number

def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1)

factorial(4)

def factorial(num):
    total=1
    for i in range(1,1+num):
        total*=i
    return total

factorial(4)
==================================================================================================================================================================================================================================
#map function : The map function allows you to "map" a function to an iterable object

def square(num):
    return num**2
my_nums=[1,2,3,4,5]
map(square,my_nums)
list(map(square,my_nums))
=================================================================================================================================================================================================================================
nums=[1,2,3,4,5,6,7,8,9]
list(filter(lambda n: n % 2 == 0,nums))
====================================================================================================================================================================================================================

[X**2 for X in range(1,11)] #square of nubers in range 1 to 10 (Map Reduction)
#Map    -> map a collection to values to another collection of values
======================================================================================================================================================================================================================

[x for x in range(1,21) if x%2==0]# Fitering 
#Filter  -> select only some elements in collection of values
==========================================================================================================================================================================================================================================
#To find unique values in array 0r 
#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique(array):
    total=[]
    for i in array:
        if i not in total:
            total.append(i)
    return total

unique([1,2,1,2,1,2,1,2,3,4,5,6,78,9])

#OR


def unique1(array):
    return list(set(array))


=============================================================================================================================================================================================================================
#To find square of array

def square(array):
    total=[]
    for i in array:
        total.append(i**2)
    return total

square([1,2,3,4])
==============================================================================================================================================================================================================================================================

#args:The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function.
 #It is used to pass a non-keyworded, variable-length argument list.
 
 
 def add(*args):
    total=0
    for i in args:
        total+=i
    return total

add(1,2,3,4,4)
 =======================================================================================================================================================================================================================================================================================

 #kwargs :The special syntax **kwargs in function definitions in python is used to pass a keyworded, 
 #variable-length argument list. We use the name kwargs with the double star.
# The reason is because the double star allows us to pass through keyword arguments
# (and any number of them).

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
    else:
        print("I don't like fruit")
        
myfunc(fruit='pineapple')
=======================================================================================================================================================================================================================================================================================
#Combined *args and **kwargs

def myFun(*args,**kwargs): 
    print("args: ", args) 
    print("kwargs: ", kwargs) 
  
  
# Now we can use both *args ,**kwargs to pass arguments to this function : 
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")
=============================================================================================================================================================================================================================================================================================================


#Lambda functions : lambda keyword is used to create anonymous functions

square = lambda num : num**2 

square(5)
=============================================================================================================================================================================================================================================================================================================

#Write a function that computes the volume of a sphere given its radius.

def volume(radius):
    return (4/3)*3.142*radius**3

volume(3)
=============================================================================================================================================================================================================================================================================================================
#Write a function that checks whether a number is in a given range (inclusive of high and low)


def range_check(num,low,high):
    if num in range(low,high+1):
        print("{} is in the range {} and {}".format(num,low,high))
    else:
        print("Num is out of range")
        
range_check(5,2,7)
=============================================================================================================================================================================================================================================================================================================
#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(list):
    total=[]
    for i in list:
        if i not in list:
            total.append(i)
        return list
    
unique_list([1,2,1,2,3,2,3,4,53,3,1])
 =============================================================================================================================================================================================================================================================================================================
#Write a Python function to multiply all the numbers in a list.        

def multiply(*args):
    total=1
    for i in args:
        total*=i
    return total
    
multiply(3,4,-5,2)
=============================================================================================================================================================================================================================================================================================================
#Write a Python function that checks whether a passed string is palindrome or not

def palindrome(s):
    s==s.replace('','')
    return s==s[::-1]

palindrome('nurses run')

palindrome('abcba')
=============================================================================================================================================================================================================================================================================================================


