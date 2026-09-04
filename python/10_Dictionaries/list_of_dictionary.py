# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Creating a list of dictionaries >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#To mimic a database we can create a list of dictionary ,where list be an in memory database
#  and each dictionary object will represent a unique record
# create a list members means key value pair is dictionary 

# Example of Creating a list of dictionaries:
#Create a list membrane of a dictionary :
print("Syntax of Creating a list of dictionary:")
print("[] list square bracket then a dictionary crual bracket{key:value}")
mydic=[
       {'1.key:':'value','2.key:':'value','3.key:':'value'},
# index             0
    {'i.key:':'value','ii.key:':'value','iii.key:':'value'},\
#                    1 
    {'1,key:':'value','2,key:':'value','3,key:':'value'}
#                    2 
    ]
# index because list have index not have dictionary we create list of a dictionary
print(mydic,'\n')
print("Example of Creating a list of dictionary:")
students=[
    {'Name:':'Wania','Age:':'20','Gender:':'Female'},
    {'Name:':'Husnain','Age:':'18','Gender:':'Male'},
    {'Name:':'Sawera','Age:':'16','Gender:':'Female'}
    ]
print(students,'\n')

#Output:
#Syntax of Creating a list of dictionary:
#[] list square bracket then a dictionary crual bracket{key:value}
#[{'1.key:': 'value', '2.key:': 'value', '3.key:': 'value'},
# {'i.key:': 'value', 'ii.key:': 'value', 'iii.key:': 'value'}, 
#{'1,key:': 'value', '2,key:': 'value', '3,key:': 'value'}]

#Example of Creating a list of dictionaries:
#[{'Name:': 'Wania', 'Age:': '20', 'Gender:': 'Female'},
#{'Name:': 'Husnain', 'Age:': '18', 'Gender:': 'Male'},
#{'Name:': 'Sawera', 'Age:': '16', 'Gender:': 'Female'}]


# <<<<<<<<<<<<<<<<<<<<<<Perform list Operation on Creating a list of dictionary>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#1.Accessing list membrane from a list of dictionary:
print("1.Syntax of Accessing list membrane from a list of dictionary:")
print("list name [index of list][dictionary key name]")
print(mydic[0]['1.key:'],'\n')
print("1.Example of Accessing list membrane from a list of dictionary:")
print(students[0]['Name:'],'\n')

#Output:
#1.Syntax of Accessing list membrane from a list of dictionary:
#list name [index of list][dictionary key name]
#value

#1.Example of Accessing list membrane from a list of dictionary:
#Wania


#2.Adding a new membrane in list of  dictionary:
#There are three ways to  adds the membrane in list of dictionary
#2(i).Append Function to adds a new membrane in list of dictionary :
print("2(i).Syntax of Adding a new membrane in list of dictionary using append function:")
print("list name dot(.)append function then [adding a new key: adding a new value]")
mydic.append({"adding a new key:":"adding a new value"})
print(mydic,'\n')
print("2(i).Example of Adding a new membrane in list of dictionary using append function:")
students.append({"email:":"waniakhalilchaudhary@gmail.com"})
print(students,'\n')

#2(ii).Insert Function to adds a new membrane in list of dictionary with index :
print("2(ii).Syntax of Adding a new membrane in list of dictionary with index using insert function:")
print("list name dot(.) insert function({adds index ,membrane you want add })")
mydic.insert(4,{"adds a new key:":"adds a new value"})
print(mydic,'\n')
print("2(ii).Example of Adding a new membrane in list of dictionary with index using  insert function:")
students.insert(4,{"Phone Number:":"031234567"})
print(students,"\n")


#Output:
#2(i).Syntax of Adding a new membrane in list of dictionary using append function:
#list name dot(.)append function then [adding a new key: adding a new value]
#[{'1.key:': 'value', '2.key:': 'value', '3.key:': 'value'}, 
# {'i.key:': 'value', 'ii.key:': 'value', 'iii.key:': 'value'},
# {'1,key:': 'value', '2,key:': 'value', '3,key:': 'value'},
# {'adding a new key:': 'adding a new value'}]

#2(i).Example of Adding a new membrane in list of dictionary using append function:
#[{'Name:': 'Wania', 'Age:': '20', 'Gender:': 'Female'}, 
# {'Name:': 'Husnain', 'Age:': '18', 'Gender:': 'Male'},
#{'Name:': 'Sawera', 'Age:': '16', 'Gender:': 'Female'},
# {'email:': 'waniakhalilchaudhary@gmail.com'}]

#2(ii).Syntax of Adding a new membrane in list of dictionary  with index using insert function:
#list name dot(.) insert function({adds index ,membrane you want add })
#[{'1.key:': 'value', '2.key:': 'value', '3.key:': 'value'}, 
# {'i.key:': 'value', 'ii.key:': 'value', 'iii.key:': 'value'},
#  {'1,key:': 'value', '2,key:': 'value', '3,key:': 'value'}, 
# {'adding a new key:': 'adding a new value'}, 
# {'adds a new key:': 'adds a new value'}]

#2(ii).Example of Adding a new membrane in list of dictionary with index using insert function:
#[{'Name:': 'Wania', 'Age:': '20', 'Gender:': 'Female'},
#  {'Name:': 'Husnain', 'Age:': '18', 'Gender:': 'Male'},
#  {'Name:': 'Sawera', 'Age:': '16', 'Gender:': 'Female'}, 
# {'email:': 'waniakhalilchaudhary@gmail.com'}, 
# {'Phone Number:': '031234567'}]


#3.Deleting the membrane in list of a dictionary:
# There are three ways of deleting the membrane in list of a dictionary
# Three ways delete a permenent membrane in list of a dictionary
#3(i).Delete the membrane in list of a dictionary:
print("3(i).Syntax of Delete the membrane in list of a dictionary using delete function:")
print('delete fucntion (list of a dictionary name[given index of membrane want delete])')
del(mydic[3])
print(mydic,'\n')
print("3(i).Example of Delete the membrane in list of a dictionary using delete function:")
del(students[3])
print(students,'\n')

#3.(ii)Remove the membrane in list of a dictionary:
print("3(ii).Syntax of Remove the membrane in list of a dictionary using Remove function:")
print("list of dictionary name . dot remove function(given membrane you want to remove)")
mydic.remove({'1.key:': 'value', '2.key:': 'value', '3.key:': 'value'})
print(mydic,"\n")
print("3(ii).Example of Remove the membrane in list of a dictionary using Remove function:")
students.remove({'Name:': 'Husnain', 'Age:': '18', 'Gender:': 'Male'})
print(students,"\n")

# 3(iii).Popping the membrane of list of a dictionary:
print("3(iii).Syntax of Popping the membrane of list of a dictionary using pop function:")
print("list of dictionary name . dot pop function(if empty by default it last membrane or you given index remove that membrane  you given index )")
print("Pop last membrane of list of dictionary by default:")
mydic.pop()
print(mydic)
print("Pop by index of list of dictionary:")
popping=mydic.pop(0)
print(popping,"\n")
print("3(iii).Example of Popping the membrane of list of a dictionary using pop function:")
print("Pop last membrane of list of dictionary by default:")
students.pop()
print(students)
print("Pop by index of list of dictionary:")
y=students.pop(0)
print(y,"\n")

# Output:
#3(i).Syntax of Delete the membrane in list of a dictionary using delete function:
#delete fucntion (list of a dictionary name[given index of membrane want delete])
#[{'1.key:': 'value', '2.key:': 'value', '3.key:': 'value'}
#{'i.key:': 'value', 'ii.key:': 'value', 'iii.key:': 'value'}, 
#{'1,key:': 'value', '2,key:': 'value', '3,key:': 'value'}
# {'adds a new key:': 'adds a new value'}]

#3(i).Example of Delete the membrane in list of a dictionary using delete function:
#[{'Name:': 'Wania', 'Age:': '20', 'Gender:': 'Female'}
#{'Name:': 'Husnain', 'Age:': '18', 'Gender:': 'Male'}
#{'Name:': 'Sawera', 'Age:': '16', 'Gender:': 'Female'}
 #{'Phone Number:': '031234567'}]

#3(ii).Syntax of Remove the membrane in list of a dictionary using Remove function:
#list of dictionary name . dot remove function(given membrane you want to remove)
#[{'i.key:': 'value', 'ii.key:': 'value', 'iii.key:': 'value'}, 
# {'1,key:': 'value', '2,key:': 'value', '3,key:': 'value'} 
# {'adds a new key:': 'adds a new value'}]


#3(ii).Example of Remove the membrane in list of a dictionary using Remove function:
#[{'Name:': 'Wania', 'Age:': '20', 'Gender:': 'Female'},
# {'Name:': 'Sawera', 'Age:': '16', 'Gender:': 'Female'}
#{'Phone Number:': '031234567'}]


#3(iii).Syntax of Popping the membrane of list of a dictionary using pop function:
#list of dictionary name . dot pop function(if empty by default it last membrane or you given index remove that membrane  you given index )
#Pop last membrane of list of dictionary by default:
#[{'i.key:': 'value', 'ii.key:': 'value', 'iii.key:': 'value'}
#{'1,key:': 'value', '2,key:': 'value', '3,key:': 'value'}]       

#Pop by index of list of dictionary:
#{'i.key:': 'value', 'ii.key:': 'value', 'iii.key:': 'value'}

#3(iii).Example of Popping the membrane of list of a dictionary using pop function:
#Pop last membrane of list of dictionary by default:
#[{'Name:': 'Wania', 'Age:': '20', 'Gender:': 'Female'}
#{'Name:': 'Sawera', 'Age:': '16', 'Gender:': 'Female'}]
#Pop by index of list of dictionary:
#{'Name:': 'Wania', 'Age:': '20', 'Gender:': 'Female'}


