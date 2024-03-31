'''
Provides high-performance ,easy
 to use data structures and 
 analysis tools for the python
   programming language



Open source python library providing high performance data manipulation and
analysis tool using its powerful data structures


Pandas- panel data(multi frame data)
2 dimensional dakta structure
'''
import os
import pandas as pd
import numpy  as np


school_data = pd.read_csv('test.csv',index_col=0)

# print(school_data)


'''two ways to create copy of the 
data 
--shallow copy----any changes made in
the shallow copy will be reflected in 
 the original copy.
 And it only creates a new variable
 that sharesw the refrence of the original
 copy,It does not create an new object at all



---deep copy----it creates a new object with no refrence to 
the original copy and any changes in it doed not affect the 
original data'''

copy_shallow = school_data.copy(deep=False)
#print(copy_shallow)\

copy_deep = school_data.copy(deep=True)
#print(copy_deep)


# Attributes of the data

# print(school_data.index)# gets all the index of the table 
# print(school_data.columns)# gets all the column of the table

# print(school_data.size)# gives the total no. of elements
#print(school_data.shape)# gives the no. of index and columns just like numpy.shape function

# DataFrame.memory_usage([index,deep])
# print(school_data.memory_usage())
# print(school_data.ndim)




'''Indexing and selecting data'''

print(school_data.head(2))# head function returns the information of the first n rows(by default it is 5)
print(school_data.tail(2))# returns the information of the last n rows(by default it is 5)

# print(school_data.at[4,'stream'])# at function takes column label and row index as input and returns the particular in formation matching the input\
# print(school_data.iat[3,0])# iat function takes row and column index as input and returns the information that matches the input


#.loc function of rows and columns byu labels 
print(school_data.loc[:,"stream"])