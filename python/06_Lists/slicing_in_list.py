#if you a particular value or element you use list you do a slicing in a list 
# one or more value to get from list is called slicing 
#slicing in a list 
#index    -5         -4        -3     -2      -1
students=["Ayesha","Javeria","Saher","Maria","Maha"]
#index     0         1         2       3       4

print(students[2]) # get value by index
print(students[0])
print(students[-5]) #negative indexing 

# slice value in  a list
#syntax => listname[start index of value: end index of value+1}.
# start value of index is called inclusive and end value of index is called exclusive 
# : indicates the slicing of list 
# In slicing of list output is also in a list 
print(students[1:2+1])

#negative indexing slicing 
print(students[-5:-3+1])

# not given start and end  of index value in list in a slicing of a list 
print(students[:]) # given list

# given start and not given end  of index  value in a slicing of a list 
print(students[2:])

#given not start and given end of index value in a slicing of a list
print(students[:3])

#given postive and negative indexing value in a slcing of a list 
print(students[2:-5]) # empty list
#In a slicing is wrong is empty not generate any error or none

#step parameter
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(num[0:16:1]) # 1 indicates single step of value
print(num[0:16:2])
print(num[0:16:5])
print(num[::5])