# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Creating a list of dictionaries >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#To mimic a database we can create a list of dictionary ,where list be an in memory database
#  and each dictionary object will represent a unique record 
# create a list members means key value pair is dictionary 

# Example of Creating a list of dictionaries
#Create a list membrane of a dictionary 
print("Syntax of Creating a list of dictionary:")
print("[] list square bracket then a dictionary crual bracket{key:value}")
mydic=[{'1.key:':'value','2.key:':'value','3.key:':'value'}]
print(mydic,'\n')
print("Example of Creating a list of dictionary:")
students=[{'Name:':'Wania','Age:':'20','Gender:':'Female'}]
print(students,'\n')

#Output:
#Syntax of Creating a list of dictionary:
#[] list square bracket then a dictionary crual bracket{key:value}
#[{'1.key:value', '2.key:value', '3.key:value'}]

#Example of Creating a list of dictionaries:
#[{'Name:': 'Wania', 'Age:': '20', 'Gender:': 'Female'}]

# <<<<<<<<<<<<<<<<<<<<<<Perform list Operation on Creating a list of dictionary>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#1.Accessing list membrane from a list of dictionary
print("1.Syntax of Accessing list membrane from a list of dictionary")
print("list name [index of list][dictionary key name]")
print(mydic[0]['1.key:'],'\n')
print("1.Example of Accessing list membrane from a list of dictionary")
print(students[0]['Name:'],'\n')

#Output:
#1.Syntax of Accessing list membrane from a list of dictionary
#list name [index of list][dictionary key name]
#value

#1.Example of Accessing list membrane from a list of dictionary
#Wania


#2.Adding a new membrane in list of  dictionary
print("2.Syntax of Adding a new membrane in list of dictionary")
print("list name dot(.)append function then [adding a new key: adding a new value]")
mydic.append({"adding a new key:":"adding a new value"})
print(mydic,'\n')
print("2.Example of Adding a new membrane in list of dictionary")
students.append({"email:":"waniakhalilchaudhary@gmail.com"})
print(students,'\n')

#Output:
#2.Syntax of Adding a new membrane in list of dictionary
#list name dot(.)append function then [adding a new key: adding a new value]
#[{'1.key:': 'value', '2.key:': 'value', '3.key:': 'value'}, {'adding a new key:': 'adding a new value'}]

#2.Example of Adding a new membrane in list of dictionary
#[{'Name:': 'Wania', 'Age:': '20', 'Gender:': 'Female'}, {'email:': 'waniakhalilchaudhary@gmail.com'}]
