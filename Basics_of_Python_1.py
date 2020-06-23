# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:36:18 2020

@author: Rohith 
""

#Basics of Python

#Python object and data structure basics

#Data_Types: Numbers;Strings;Print Formmating;Lists;Dictionaries;Booleans;Tuples and Sets

#Basic arithmetic operations

2+1  #Addition

2-1 #Subtraction

2*2 #Multiplication

2/2 #Division

7//3#Floor Devision

7%3 # The % operator returns the remainder after division.

2**3 # Powers\

9**0.5 # Taking square root

2+10*10+3  #Order of Operations followed in Python

(2+10)*(10+3) # Can use parentheses to specify orders

#Variable Assignment
a=71

a+a

a+1

a-1

a*a


#Example

my_income=100
tax_rate=0.5
Tax=my_income*tax_rate
Tax

#You can check what type of object is assigned to a variable using Python's built-in type() function. Common data types include:

#int (for integer)
#float
#str (for string)
#list
#tuple
#dict (for dictionary)
#set
#bool (for Boolean True/False)

#Examples:
a=1

type(a)

a=(1,2)

type(a)

a=({'rohith':'Male','Age':29})

type(a)

# Strings

a='My name is Rohith'
a
b='I'm from India' #This line gives error.So be careful b can be written as

b='Im from India'


#Printing string 

print("Hello world")# or we can write directly as below

"Hi how are you?"

print("Hi Rohith \n how are you") # \n is used to print new line

len("Hi how are you")# len() to check the length of a string!

#String Indexing

a="Hello world"

len(a)

a[0]

a[2]

a[1:] # Grab everything past the first term all the way to the length of a which is len(a)

a[:3]# Grab everything UP TO the 3rd index

a[:]#Everything

a[:-1]# Grab everything but the last letter

a[::1]# Grab everything, but go in steps size of 1

a[::2]# Grab everything, but go in steps size of 2

a[::-1]# We can use this to print a string backwards

s='Hello'
s[0]='A'#Notice how the error tells us directly what we can't do, change the item assignment!

c=s+'world'# Concatinating 

print(c)

letter ='z'

letter*10

x="Welcome to Python world"

x.upper()# Upper casing string

x.lower()#Lower casing string

x.split()# Split a string by blank space (this is the default)

x.split('P')

#Print Formatting

'My name is :{}'.format('Rohith') 

print("I'm going to inject %s here." %'something')

print("My favourite cricketer is %s from India."%'kohli')

print("My name is %s."% 'Rohith')

print("My Mother name is %r."% 'Shobha')

print("A %s is %s earned."%('penny','penny'))

print('Floating point numbers: %1.5f' %(13.144))

#Lists :  Lists can be thought of the most general version of a sequence in Python. 
Unlike strings, they are mutable, meaning the elements inside a list can be changed!


my_list=[1,2,3]

my_list=['string',12,33,'o',44,5,6,64,3,'welcome']

my_list

len(my_list)

my_list[0]

my_list[:]

my_list[2:]

my_list[:5]

new_list=['parrot',23,'orange']

c=my_list+new_list

c

my_list*2

#append function :  append method to permanently add an item to the end of a list

list1=[1,2,3,4,5]

list1.append("Rohith")

list1

# pop function : pop to "pop off" an item from the list.
 By default pop takes off the last index, but you can also specify which index to pop off
 
 list1.pop()

list1.pop(1)

list1

list1[0]="Amith"

list1

new_list=['a','e','i','o','u']

new_list.reverse() # Use reverse to reverse order (this is permanent!)

new_list

new_list.sort()# Use sort to sort the list 
(in this case alphabetical order, but for numbers it will go ascending)

new_list

#Nested_list: A great feature of of Python data structures is that they support nesting.
 This means we can have data structures within data structur

list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]

matrix=[list1,list2,list3]

matrix

matrix[0]
matrix[0][0]


#Dictionaries: A Python dictionary consists of a key and then an associated value.

my_dec={'key1':'value1','key2':'value2'}

my_dec

a={'Name':'Rohith','Age':30,'City':'Davangere'}
a

a['Name']

b={'key1':'z','key2':'love','key3':['zebra','lion','tiger']}

b['key3']

b['key3'][0]

b['key3'][2].upper()

#Nesting in Dictionary

d={'key1':{'nestkey':{'subnestkey':'value1'}}}

a={}

a['animal']=1
a['dog']=30
a


dictionary={'key1':'value1','key2':'value2','key3':'value3'}

dictionary.items()

dictionary.keys()

dictionary.values()

#Tuples:In Python tuples are very similar to lists, however, 
unlike lists they are immutable meaning they can not be changed

t=(1,2,3,4)

type(t)

len(t)

t[0]

t[-1]

t[0]='Rohith' #This code gives error because tuples are immutable

w=(1,1,1,1,2,45,33,4,4,5,6,73,4,7,65,432,222,345,67,6,543,2)

len(w)

w.count(3)

w.count(1)

w[8]


#Sets : Sets are an unordered collection of *unique* elements.
 We can construct them by using the set() function.
 
x=set()

x.add(2)

x.add(2020)

x

list=(1,2,3,4,5,3,2,3,4,3,2,3,4,23,2,1,2,3,4,5,6,77,90)

set(list)

#Boolean

a=True

a=1
b=23

a>b
a<b


#Files
pwd# to check your notebook location, use pwd:


#Python comparision operators

2==2

1==0


2!=1


2>1

2<4

2>=4

2<=4

1<2<3


1<2 and 2<3

1 < 3 > 2

1<3 and 3>2

1==2 or 2<3

1==1 or 100==1
