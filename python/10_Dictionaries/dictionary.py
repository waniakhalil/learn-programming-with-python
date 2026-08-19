# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Dictionary:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..>
# There are Three Ways to store different values or bunch of value to assign  one varible
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
 
 # 4.In key and valus store any datatype also store list and tuples but key and value  datatype is same is important 

# 5. Beware of the fact that the keys are case sensitive,hence the following statement will throw an expection of type keyerror 

# Syntax:
# Dictionary name= {key:value,.............}
# (key:value) is  called a pair  or element 

# Syntax Example:
print("Syntax Example of Dinctionary:")
mydict={'key':'value',' key':'value','  key':'value'}
print(mydict,'\n')

#Output:
#Syntax Example of Dinctionary:
#{'key': 'value', ' key': 'value', '  key': 'value'} 

# Example:
# if you want to store the information about a student 
print("Example of dictionary:")
student={'Name':'Wania','Age':'20','Gender':'Female'} # 
print(student)
print("Length of student Dicitionary is:") 
print(len(student),'\n') 

# Output:
#Example of dictionary:
# {'Name': 'Wania', 'Age': '20', 'Gender':'Female'}
#Length of student Dicitionary is:
# 3


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Perform Operation of Dictionary:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 1.Adding a new value in existing  dictionary:
# syntax:
# dictionary name[adding new key]="value of adding a new key"
print("Perform Operation of Dictionary:")
print("1.Syntax of Adding a new value in existing dictionary:")
mydict[' adding a new key']='value of adding a new key'
print(mydict,'\n')
print("1.Example of Adding a new value in existing dictionary:")
student["email"]="waniakhalilchaudhary@gamil.com"
print(student,'\n')


#Output:
#perform Operation of Dictionary:
#1.Syntax of Adding a new value in existing dictionary:
#{'key': 'value', ' key': 'value', '  key': 'value', ' adding a new key': 'value of adding a new key'}

#1.Example of Adding a new value in existing dictionary:
#{'Name': 'Wania', 'Age': '20', 'Gender': 'Female', 'email': 'waniakhalilchaudhary@gamil.com'}



# 2.Accessing information  from Dictionary 
# Note:
# if you try to acess any key which is not present in dictionary will rasie an exception of type Keyerror. 
print("2.Syntax of Accessing information from Dictionary:")
print("given dictionary Name and in square bracket[given key of accessing]",'\n')
print("2.Example of Accessing information from Dictionary:")
print(student['Name'])

# Output:
# 2.Syntax of Accessing information from Dictionary:
 #given dictionary Name and in square bracket[given key of accessing]

# 2.Example of Accessing information from Dictionary:
# Wania