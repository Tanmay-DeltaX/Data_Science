import pandas as pd 

data = pd.read_csv('test.csv',index_col=0)


data['class']=data['class'].astype('object')# changes the datatype of the field
print(data.info())

#nbytes check the bytes used by a field
print(data['class'].nbytes)
print(data['class'].astype('category').nbytes)

#replace() used to change the datatype,,,, syntax - dataframe.replace(original value, new value,inplace=True)

# isnull().sum() checks the count of missing values in each column
print(data.isnull().sum())
