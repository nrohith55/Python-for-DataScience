# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:49:33 2020

@author: Rohith
"""

#Numpy : Numpy is a linear algebra library for Python.It is one of the building block components .

#Numpy arrays essentially comes in two flavours 1)Vector 2)Matrices

#Vectors are 1-Dimensional arrays and Matrices are 2-Dimensional arrays

#Numpy array by using Python object such as lisy

my_list=[1,2,3]

import numpy as np 

np.array(my_list) #output is 1 dimensional array

x=[[1,2,3],[4,5,6],[7,8,9]]

np.array(x)#output is 2 dimensional array

np.arange(0,10)

np.arange(0,10,2)

np.zeros(3)

np.zeros([5,5])

np.zeros([2,3])

np.ones(2)

np.ones([10,10])

np.zeros([13,4])

np.linspace(0,5,100)

#Identity Matrix:(It is 2 dimensional square Matrix)

np.eye(4)

np.random.rand(5) #It basically takes values from uniform distribution from 0 to 1

np.random.rand(5,5)

np.random.rand(2)

np.random.randint(1,100)#lower limit is 1 ,upper limit is 100 ,it select 1 random value between 1 to 100

np.random.randint(1,100,10)#lower limit is 1 ,upper limit is 100 ,it select 10 random value between 1 to 100

np.arange(25)# display 0 to 24 numbers

arr=np.arange(25)

arr.reshape(5,5)#Reshape method

a=np.random.randint(0,50,10)
a

a.max()
a.min()
a.argmax() #argmax() indicates the location of maximum number
a.argmin()#argmin() indicates the location of minimum number


a.dtype

a.shape

arr= np.arange(0,11)
arr
arr[8]
arr[1:5]
arr[0:5]
arr[:6]
arr[5:]
arr[0:5]

arr_2d=np.array([[5,10,15],[20,25,30],[35,40,45]])
arr_2d

arr_2d[0][0]
arr_2d[1][1]
arr_2d[2,1]
arr_2d[:2,1:]
arr_2d[:2]


s=np.arange(0,10)
s
s>5
s<6

s[s<3]

arr_2d=np.arange(50).reshape(5,10)
arr_2d

arr_2d[1:3]

arr_2d[1:3,3:5]

#Numpy Operations:

#Array with array operation :

arr=np.arange(0,11)
arr

arr+arr
arr-arr
arr*arr

#Array with scalars:

arr+100
arr-100
arr*100
arr/arr
1/arr
arr*2


#Universal array function:

np.sqrt(arr)
np.exp(arr)
np.max(arr)
np.sin(arr)
np.log(arr)


x=[1,2,3,4,5,6,5,4,3,2,1,1,2,22,4,3,4,5,]
x=np.array(x)
x

type(x)
x[0:10]
x.shape
x>4
x[x>10]


x**2
x+1
x[x%2!=0]

x = [1,2,3,4,5,6]
y = [7,8,9,10,11,12]

#np.array(y).shape


z = np.array([x,y])
z
z = z.reshape(4,3)
z
z[0,1]
z.shape

z[:,1:]

# Statistics on numpy array 
np.mean(z)
np.median(z)
np.mean(z[1,:])
np.mean(z[:,1])
np.std(z)
np.var(z)




# Few functions in numpy 
np.round(1.21212,2)

temp1 = np.random.normal(10,2,5)

temp2 = np.random.normal(-10,2,5)
help(np.random.normal)
temp2
temp1
temp3 = np.column_stack((temp1,temp2))
temp3
m1 = np.random.random((2,3))
m2 = np.random.random((2,3))

m1+m2





















