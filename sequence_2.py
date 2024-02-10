'''
Indexing
It just mean to access elements for data.
For:
str
list
tuple
array
range

We cannot use index for searching a element in dictionary but we 
can certainly use the value pairs to access elements.

It does not work set
'''
# str = 'learning'
# print(str.index('earn'))
# lst = [1,2,3,4,4,5]
# print(lst.index(1))
# from array import *
# arr= array('i',[1,2,4,5])
# for i in arr:
#     print(i)
# print(arr[-3])    
r = range(1,12,4)
for i in r:
    print(i)
print(r.index(5))
print(r[2])    