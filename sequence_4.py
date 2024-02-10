'''
string methods(methods are functions called on objects)
the methods are:
capitalize
casefold
title
swapcase
find
count
replace
isalnum

'''
"""
STR METHODS
"""
# str2 = 'hello python world.'
# str1= 'The'
# print(str2.capitalize())
# print(str2.casefold())
# print(str2.title())
# print(str2.swapcase())
# print(str2.find('o'))
# print(str2.count('o'))
# print(str2.replace('python','C++'))
# print(str2.isalnum())

# name= '{} *{}'.format(str2,str1)
# print(name)

# print(dir(str))
# print(help(str))




# INT METHODS,DICT,SET 
 #len-str,list,tuple,array,dictionary,set
 #tuple and set cannot be appended as they are immutable but  set can be added.(add takes only one parameter)
 
tup = (1,2,3,4)
lst = [1,2,3,4,5]
#lst.reverse()
#print(lst) 
#lst.clear()
#print(lst)
lst.append(6)
#print(len(lst))
#print(lst)

  # UPDATE function - takes single argument (it can be a list , tuple , dictionary)(used for set and dictionaries or non sequential data)

# st = {1,2,3,4,5}
# st.add(6)
# st.update([7,8])
# print(st)

dict = {1:'first',2:'second',3:'third'}
# dict['four'] =4
dict.update(five=5)
# print(dict)
# print(len(dict))
# print(list(dict))   # gives all the keys of the dictionary
# print(dict.get(1))
# dict.keys()  # return the list of keys
# dict.items()   # returns the values and keys as a tuple pair
dict.pop('five')
print(dict)



# insert() supports list and arrays
from array import *
arr = array('i',[1,2,3,4,5])
arr.insert(1,3)  
arr.insert(7,10)      # inserts an item at a particular position as in this case it is 2 nd position and the value is 3
print(arr)





# pop() is used to delete an element
# default value is -1
# datatypes  - array, list, set , dictionary(generally not used in set because it is unordered)
#the above is same for remove()(but insted of index it uses the value)
#discard() is same as remove() but does not giving an error while giving a non listed value
arr.pop(1)
arr.remove(4)
# print(arr)
#del arr   #deletes any mentioned datatypes
#del arr[:]
arr.extend((2,3,4,5)) #adds any iterable at the end of the specified datatype


arr.fromlist([3,4])    #add value from a list
b=arr.tolist()
print(arr)
print(b)






'''
ON SETS
'''
a={1,2,3,4,5,6,7,8}
b={4,8,2,7,0}
print(a | b)           # gives the common values and uncommon values for both the datatypes
print(a.union(b)) # gives the common values and uncommon values for both the datatypes
print(a & b)          #common values
print(a.intersection(b))



