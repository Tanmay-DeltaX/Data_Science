import numpy as np#numerical python, multi-dimensional
#print(np)

'''
lst=[1,2,3,4,5,6,7,8,9,10]
print(lst)


# Creatiion of the array
arr = np.array(lst,dtype=int)
print(len(arr))
print(arr.ndim)
print(arr.shape)


# Reshaping the array(arr)

array2= arr.reshape(5,2)
print(array2)
print(array2.shape)

array3=arr.reshape(5,-1)      # '-1' represents that the mentioned dimension will automatically be calculated
print(array3)
print(array3.ndim)
'''

# creation of array from multiple lists

lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]
lst3=[11,12,13,14,15]
marray=np.array([lst1,lst2,lst3])
# print(marray)
# print(marray.shape)
# #marray2= marray.reshape(5,3)
# #print(marray2)
# marray.shape=(5,3)
# print(marray)


# range_array = np.arange(25)
# print(range_array)
# print(range_array.ndim)
# range_array.shape=(5,5,1)
# print(range_array)
# print(range_array.ndim)



# x = np.array([1,3,4,5],dtype=int)
# y = np.array([6,7,8,9],dtype=int)
# print(np.add(x,y))
# print(np.subtract(x,y))
# # other are --- np.multiple , np.divide  , np.dot()(to get the dot product)


#format = np.sum(array,axis)
print(np.sum(marray))#axis in this case is none therefor it calculates the sum of all valy\ues
print(np.sum(marray,axis=0))#sum of values of same column
print(np.sum(marray,axis=1)) #sum of values of same row

