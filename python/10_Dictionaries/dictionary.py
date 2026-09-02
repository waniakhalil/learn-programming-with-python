# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Dictionary:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..>
# Why we need Dictionary or list or tuples?
# if we store one or more types of  value we made many varible it is time confumse and no of lines codes increase and not efficient way and access it is also not efficient
# to solve this problem we use Dictionary or list or tuples in we store different values or elements in one variable or not in many variable 

# There are Three Ways to store different values or bunch of value or elements  to assign  one varible
# 1.list [] it is way to verify this types 
# 2.Tuples ()
# 3.Dictionary {}

# Definition:
# Python provides a data structure Dictionary for such cases.Dictionary in simple words is a data structure which
# stores the keyvalues pairs

#Note:
# 1.Please note that keys must be between single or double quotation.if they are string type ,every pair is separated from 
# other pairs by a comma and every pair of key value is separated by colon

# 2. if get value from dictionay get from key

# 3. In dictionary not indexing but it key against work also pick random value also in loop 
 
 # 4.In key and value store any datatype also store list and tuples but key and value  datatype is same is important 

# 5. Beware of the fact that the keys are case sensitive,hence the following statement will throw an expection of type keyerror 

# Syntax:
# Dictionary name= {key:value,.............}
# (key:value) is  called a pair  or element or key value pair

# Syntax Example:
print("Syntax Example of Dinctionary:")
mydict={'1.key':'value','2.key':'value','3.key':'value'}
print(mydict,'\n')

#Output:
#Syntax Example of Dinctionary:
#{'1.key': 'value', '2.key': 'value', '3.key': 'value'} 

# Example:
# if you want to store the information about a student 
print("Example of dictionary:")
student={'Name':'Wania','Age':'20','Gender':'Female'}  
print(student,'\n')
print("Length of student Dicitionary is:") 
print(len(student),'\n') 

# Output:
#Example of dictionary:
# {'Name': 'Wania', 'Age': '20', 'Gender':'Female'}
#Length of student Dicitionary is:
# 3


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Perform Operation of Dictionary:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 1.Adding a new value and key in existing  dictionary:
# Note:
# When we assigning a value in a key which does not exists,python creates the key and assigns the value in the key
# if key already present the value is overwritten 
# Adding value and key in dictionary thoungh key value pair 
# adding key and value in random add  start and end and between because dictionary have not index 

# syntax:
# dictionary name[adding new key]="value of adding a new key"
print("Perform Operation of Dictionary:")
print("1.Syntax of Adding a new value in existing dictionary:")
mydict['adding a new key']='value of adding a new key'
print(mydict,'\n')
print("1.Example of Adding a new value in existing dictionary:")
student["email"]="waniakhalilchaudhary@gamil.com"
print(student,'\n')
print("Example of key already present the value is overwritten:")
student["Name"]="Wania Khalil Chaudhary"
print(student,'\n')
print("Example key and value is also different data type is also possible not must same data type like string and integer")
student["Phone Number"]="03123456789"
print(student,'\n')


#Output:
#perform Operation of Dictionary:
#1.Syntax of Adding a new value in existing dictionary:
#{'key': 'value', ' key': 'value', '  key': 'value', ' adding a new key': 'value of adding a new key'}

#1.Example of Adding a new value in existing dictionary:
#{'Name': 'Wania ', 'Age': '20', 'Gender': 'Female', 'email': 'waniakhalilchaudhary@gamil.com'}
# Example of key already present the value is overwritten:
# {'Name': 'Wania Khalil Chaudhary', 'Age': '20', 'Gender': 'Female', 'email': 'waniakhalilchaudhary@gamil.com'}
# Example key and value is also different data type is also possible not must same data type like string and integer
# {'Name': 'Wania Khalil Chaudhary', 'Age': '20', 'Gender': 'Female', 'email': 'waniakhalilchaudhary@gamil.com', 'Phone Number': '03123456789'}


# 2.Accessing information  from Dictionary 
# Note:
# if you try to acess any key which is not present in dictionary will rasie an exception of type Keyerror. 
print("2.Syntax of Accessing information from Dictionary:")
print("given dictionary Name and in square bracket[given key of accessing]")
print(mydict['3.key'],'\n')
print("2.Example of Accessing information from  Dictionary:")
print(student['Name'])
print(student['Phone Number'],'\n')

# Output:
# 2.Syntax of Accessing information from Dictionary:
 #given dictionary Name and in square bracket[given key of accessing]
 # value 

# 2.Example of Accessing information from Dictionary:
# Wania
# 03123456789


# 3.Deleting a key and value from Dictionary:
print("3.Syntax of Deleting a key and value in a  Dictionary:")
print("given del key word and round bracket(dictionary Name) then given in square bracket [want delete a key]")
del(mydict['2.key'])
print(mydict,'\n')
print("3.Example of Deleting a key and value in a  Dictionary")
del(student['Gender'])
print(student,'\n')

# Output:
#3.Syntax of Deleting a key and value in a Dictionary:
#given del key word and round bracket(dictionary Name) then given in square bracket [want delete a key]
#{'1.key': 'value', '3.key': 'value', 'adding a new key': 'value of adding a new key'}

#"3.Example of Deleting a key and value in a Dictionary"
#{'Name': 'Wania Khalil Chaudhary', 'Age': '20', 'email': 'waniakhalilchaudhary@gamil.com', 'Phone Number': '03123456789'}    


#4.Updating the key and value from dictionary
#4.Syntax of Updating a key and value from Dictionary:
print("4.Syntax of Updating the key and value in a Dictionary")
print("Dictionary  name in square bracket[key name ] assign operator and value of update in a key")
mydict["3.key"]="value 2"
print(mydict,'\n')
print("Updating the key and value in a dictionary")
student["email"]="waniakhalilgujjar@gmail.com"
print(student,'\n')


# Output:
#4.Updating the key and value from dictionary
#Dictionary  name in square bracket[key name ] assign operator and value of update in a key
#{'1.key': 'value', '3.key': 'value 2', 'adding a new key': 'value of adding a new key'}

#Updating the key and value in a dictionary
#{'Name': 'Wania Khalil Chaudhary', 'Age': '20', 'email': 'waniakhalilgujjar@gmail.com', 'Phone Number': '03123456789'}
