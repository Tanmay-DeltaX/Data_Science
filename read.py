import os
import pandas as pd

#data = pd.read_csv('test.csv') #creates a  index column
data = pd.read_csv('test.csv',index_col=0, na_values=["??","###"]) #stating that column 0 should be treated as index column

#print(data)  #blank values read as 'nan'



'''Junk values can be converted to missing calies by pasing them as a list to the parameter
"na-values"
na_values=["??"] ---- this shows that ??,### is going to be considered as na_values
5th line
'''




#Importing data form excel sheet
# data = pd.read_excel('file.xlsx',sheet_name='')


#importing data for txt file
data_txt = pd.read_table("test1", delimiter=",", index_col=0)
print(data_txt)#we use parameters like sep or delimiter to display the data in appropriate rows and columns
print(type(data_txt))

'''text file can also be read by 
read_csv function'''
