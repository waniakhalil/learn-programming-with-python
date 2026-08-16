# A list is a data type in Python used to store multiple values in one variable.
#Lists are written using square brackets [].
#A list can store numbers, strings, or different data types.
# Lists are ordered and changeable (mutable).
# list concept like array of other language 
# each element or value that is inside of a list is called an item 
# every value separate in list by comma 

name=['Wania','Sawera','Husnain','Ubaidullah','Merub']
print(name)


# operation on list 
# Accessing list element operation 
# to get a inderx or position of a value or element or item that store in list 
# first item in list by default index is 0 in every language

arr=['1','Pakistan','True','3.5','False','3Hello','World','Dyson','bmw']
print(arr[0])
print(arr[7])
print(arr[8])
print(arr[3])

#Adding Values in a list 
# Adding  Value in a lsit using Append () FUNCTION
# In append  function value pass by function is also called arugments
# Append functions addimg value at the end of a list
# syntax is list name and dot .append function in small brackets pass value a arguments
arr.append('skincare')
print(arr[9])
print (arr)


# Finding a value in a list 
# there a two ways to find a value in a list
# First way is  get value from index and return the value index it is confirm that value is exit in a list
arr.index('Pakistan')
# second way is the in operator is used to check whether a value exists in a list. It returns True if the value is found and False if it is not.
# syntax (value in list_name)
# it is commonly used in if statement
print('3Hello'in arr) 
print('3.5' in arr)

# Removing and Deleting the value 
# There are 2 ways to Deleting the value in a list 
# First way is del function for this function must used index for delete value
# syntax is del function and list name and provide in square bracket the delete value index
# it is delete permenent not get 
del arr[2]
print(arr)
# delete value like sliceing 
del arr[2:4]
print (arr)
# second way is the remove function in this we not provide index we provide actual value we want  delete and remove
# it also delete value  permenant 
# syntax list name  .remove() and small bracket given actual value want delete 

arr.remove('Pakistan')
print(arr)

#Popping elements from list 
# last element is pop means last value is exit by default and also return
# in pop function last element of list is pop by default if you given index no of element the exit index element is pop
# in pop function element is reuse and store  the  pop element in a variable not use in delete and romove function
arr.pop() # pop last element of list by default 
print(arr)
arr.pop(2) # pop index 2 element of list 
print(arr)
y=arr.pop(2)
print(y)
# return of pop value and dtore in a variable
number=[20,30,40]
x=number.pop()
print("Removed item:",x)
print(number)