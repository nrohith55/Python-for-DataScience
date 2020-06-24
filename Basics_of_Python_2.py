# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:17:17 2020

@author: User
"""

#Introduction to Python statement

#1)if, elif, else Statements

marks = 60

if marks>= 85:
    print("distinction")
    
elif marks>= 40:
    print("pass")
    
else:
    print("not pass")
    
Location ="Bank"

if Location=="Bank":
    print("Im in Bank")
elif Location=="Stadium":
    print("Im watching cricket")
else:
    print("Where are you?")
    
    
person="Johny"

if person=="Sammy":
    print("Welcome Sammy")
else:
    print("Welcome! Your good name please?")
    
    
#2)for loops
    
list=[1,1,2,3,4,55,5]

for num in list:
    print(num)
    
    
z=[1,2,3,4,5,6,7,8,9,10]

for num in z:
    if num%2==0:
        print("Even_Number")
    else:
        print("Odd_Number")
    
# Program to find even or odd
List=[11,22,33,44,55,66,77,88,99]

for num in List:
    if num%2==0:
        print(num)
    else:
        print('odd_number')
        
        
for i in range(10):
    print(i)
    
for i in range(6):
    print(i)
    
for i in range(13,1,-3):
    print(i)   
    
for letter in "My name is Rohith":
    print(letter)
    

tuple=(1,2,3,4,5)

for t in tuple:
    print(t)
    

list2=[(1,2),(3,4),(5,6)]

for tuple in list2:
    print(tuple)
    
    
for (t1,t2) in list2:
    print(t1)
    

dic={'key1':1,'key2':2,'key3':3}

for items in dic:
    print(items)
    
    
  
dic={'key1':1,'key2':2,'key3':3}

for key in dic:
    print(key)  

for i in range(20,2,-2):
    if i ==6:
        break
    if i==10:
        continue
    print(i)
        

# while loop:
    
x=0
while x<10:
    print('Currently the x value is :',x)
    print('x is still less than 10,adding 1 to x')
    x+=1
else:
    print("All done")
    
    
#USEFUL OPERATORS:
    #1)RANGE operator:The range function allows you to quickly generate a list of integers
   
range(0,10)

list(range(1,10))

list(range(0,50,2))

#2)ZIP operator: use the zip() function to quickly create a list of tuples by "zipping" up together two lists.

list1=[1,2,3,4]
list2=[5,6,7,8]

zip(list1,list2)

list(zip(list1,list2))

#3)IN Operator:use it to quickly check if an object is in a list

list=[1,2,3,45,89]

1 in list

'x' in list    


#)MAX and MIN operator:Quickly check the minimum or maximum of a list with these functions.

y=[11,1,2,3,4,5,57,6,7,8,9,87,65,4,23,56,7,6,54,5,678,76,54,56,76,543,456,75]    

max(y)    
min(y)


#RANDOM operator

from random import shuffle

list=[1,2,3,4,5,6,7,8,9]
shuffle(list)
list

from random import randint

s=randint(1,45)
s


#Input operator:

input("My name is:")

input('Enter Something into this box: ')



#List comprehension:List comprehensions allow us to build out lists using a different notation

list1=[x for x in 'word']
list1
list2=[x for x in range (1,12)]
list2
list3=[x**2 for x in range(1,10) ]
list3
list4=[x for x in range (1,35) if x%2==0]
list4
list5=[ x**2 for x in [x**2 for x in range(11)]]
list5
