# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:36:51 2020

@author: Rohith
"""
#Python : Pandas is an open source library built on top of Numpy
#It allows for fast data analysis ,data cleaning and preparation
#It excels is performance and productivity
#It also has a built in vizualization features
#It can work with data from a wide variety of sources

#Series : Series is very similar to numpy array ,built on top of numpy array object

import numpy as np
import pandas as pd

labels=['a','b','c']
my_data=[10,20,30]

arr=np.array(my_data)
d={'a':10,'b':20,'c':30}

pd.Series(my_data,labels)# Syntax : pd.Series(Data,Index)

pd.Series(arr)

pd.Series(arr,labels)

pd.Series(d)

pd.Series(data=labels)

Ser1=pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
Ser1

Ser2=pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
Ser2

Ser1['USA']


Ser3=pd.Series(data=labels)
Ser3

#Pandas Data Frame:

import pandas as pd
import numpy as np
from numpy.random import randn

df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z']) #Syntax: pd.DataFrames(Data,Index,Columns)
df

df['W']#To select one particular column

type(df['W'])

df['X']

df[['W','X']] #To select combined columns

df["New"]=pd.DataFrame(df['W']+df['Y'])
df["New"]
df=pd.concat([df,df["New"]],axis=1)
df
df.shape

df.loc['A']#Label based Index
df.iloc[0]#Numerical based Index
df.loc['B','Y']
df.loc[['A','B'],['W','Y']]

df>0

df_new=df.drop('New',axis=1)
df_new

df_new>0

df['W']>0

df_new[df_new>0]

df_new['Z']<0

df[(df['W']>0)&(df['Y'])] #& and operation 

df.reset_index()#Index is reset to a column and we get actual index and then numarical


df

#Multi-Index and Hier-Index Keys

outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]

hier_index=list(zip(outside,inside))
hier_index

pd.MultiIndex.from_tuples(hier_index)

df=pd.DataFrame(randn(6,2),hier_index,['A','B'])
df

d={'A':[1,2,np.nan],'B':[3,np.nan,np.nan],'C':[1,2,3]}

df=pd.DataFrame(d)
df

df.dropna()

df.dropna(axis=1)

df.dropna(thresh=2)

df['A'].fillna(value=df['A'].mean())

#Group_by: Allows you to group together rows based off of a column and perform an aggregate function on them

data={'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],'Person':['A','B','C','D','E','F'],'Sales':[200,120,340,124,243,350]}

df=pd.DataFrame(data)
df

by_company=df.groupby('Company')
by_company.mean()
by_company.sum()
by_company.std()
by_company.sum()
by_company.sum().loc['FB']


df.groupby('Company').count()
df.groupby('Company').max()
df.groupby('Company').describe()

#Concatination:It basically glues together dataframe.Dimensions should match
df1=pd.DataFrame({'A':[200],'B':[400]})
df2=pd.DataFrame({'C':[543],'D':[234]})
df3=pd.DataFrame({'E':[2456],'F':[9865]})

pd.concat([df1,df2,df3],axis=0)

#Merging:The merge function allows you to merge Data Frames together as merging SQL Tables together.

left=pd.DataFrame({'Key':['k0','k1','k2','k3'],'A':['A0','A1','A2','A3'],'B':['B1','B2','B3','B4']}) 
right=pd.DataFrame({'Key':['k0','k1','k2','k3'],'C':['C0','C1','C2','C3'],'D':['D1','D2','D3','D4']})

pd.merge(left,right,how='inner',on='Key')

pd.merge(left,right,on=['Key1','Key2'])

#Joining:Joining is convinient method for combining the columns of two potentially differentially index Dataframes 
#into a single resultant frame.
left=pd.DataFrame({'A':['A0','A1','A2','A3'],'B':['B1','B2','B3','B4']}) 
right=pd.DataFrame({'C':['C0','C1','C2','C3'],'D':['D1','D2','D3','D4']})

left.join(right,how='outer')

left.join(right)

#Operations:

df=pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})

df.head()

df['col1'].unique()

len(df['col1'].unique()) #or

df['col1'].nunique()

df['col2'].value_counts()

df[df['col1']>2]

df['col1']>2

#Apply Method:

df['col3'].apply(len)

df['col2'].apply(lambda x:x**2)

#Removing columns:

df=pd.DataFrame({'Key':['k0','k1','k2','k3'],'A':['A0','A1','A2','A3'],'B':['B1','B2','B3','B4']}) 
df

df.drop('Key',axis=1,inplace=True)
df

df.index
df.isnull()

df.sort_values(by='A')

#Data input and output: Data Sources :{CSV,Excel,HTML,SQL}





