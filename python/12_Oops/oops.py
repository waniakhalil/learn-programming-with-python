#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Object Oriented Programming Language>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# What is object Oriented programming language and depend?

#Object-Oriented Programming (OOP) is a programming method where programs are organized around objects and classes instead of only functions and procedures.
#Object Oriented first concept and base is Classes


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Classes>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Python is an object Oriented programming language.this means that almost all the code is implemented.
# using a speecial construct called classes
# in python almost all things based on classes

# programmers use classes to keep related things together this is done using the keyword "class" which is 
# grouping of blinded the related knowledge

# What is class?

#A class is a model
# A class is a blueprint (map) of anything
# A class is a template of something means example or template through create same thing
# A class may be defined as something that can be followed to create objects and nstances

# What is Object?

# object are instances of classes
# object made of classes 
# copies of classes
# Object follows the classes
# classes similar object


# relationship between class and object:
# Example of Class and Object:
#                          Class: (Car )

#                        properties of class
#   Variable:          Car has  colour
#                      Car has make
#                      Car has model

# Car obj also has a color       blue                    red                 black
# Car obj also has a make         Ford                   Toyota               Volkswegen
# Car obj also has a model       Mustang                 Prlus                 Golf


# Writing a class 

# Python uses a keyword "class" to define a class

#  Keyword  name of class
# Class     Car():
#       body of class car
# class name write in capital letter

# What actuallly class hold?

#A class may hold attributes (variables)
#A class may hold behaviours (Functions)

# Example:

#A car colour ,model and seating cacpacity are attributes of car
#A car can stop,run, speed_up and speed_down are behavoiurs of car


# Almost surrounded all things object and class 
# class made of name attributes and behavoiur form a model class

# Classes:Creating an instance

#Almost everything in python is an object,with its properties and methods
#Objects are made following its class means if an object belongs to a class it must have been following the
# requirements set by the class

# Class Car():
#      define a class body
#      attributes and properties (variable and function)

# Creating object/instance of Car Class
# object name           assign operator               Class name ()
#     car1                 =                             Car()
#    car2                 =                               Car()
# Create object name according to variable rule 
# create object you want no limit 

# now complete example of classes and object 
#  create a object we can access attributes nad behavouoir in object  from class and also change

print("Example of classes and object:",'\n')
 # initialize syntax:
 #to create a class in initialize its attributes, we commonly use the __init__() method.
 #class ClassName:
   #def __init__(self, parameters):
       # self.attribute = parameters
# self is first parameter in initialize is not must write self name you can change according to you
# self make every object make attribute and behaviour copy

class Car():
    # attributes >>>>>>>> are variables in programming
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.battery="200amp" # default attribute because he not come from intailize 

# behaviour >>>>>>>>>> are function in programming 
    def description(self):
        print(f"The make of Car:{self.make}")
        print(f"The model of Car:{self.model}")
        print(f"The year of Car:{self.year}")
    def move(self):
        print(f"{self.make} is moving with speed")
    def applyingbreak(self):
        print(f"{self.model} has appled the break")
    def descriptionbattery(self):
        print(f"The battery of car is {self.battery}")

    #Changing value attribute function:
    def setbatterysize(self,newsize):
        self.battery=newsize 
    def getbatterysize(self):
        print(f"The size of your car battery is {self.battery}")
   
# How to create object of a class:
car1=Car('Honda',"Civic",2019)
car2=Car("Suzuki","Alto",2015)

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.battery,"\n")

car1.description()
car1.move()
car1.applyingbreak()
car1.descriptionbattery()

print("\n")

print(car2.make)
print(car2.model)
print(car2.year)
print(car2.battery,"\n")

car2.description()
car2.move()
car2.applyingbreak()
car2.descriptionbattery()

print("\n")

# Output:
#Example of classes and object: 

#Honda
#Civic
#2019
#200amp

#The make of Car:Honda
#The model of Car:Civic
#The year of Car:2019
#Honda is moving with speed
#Civic has appled the break
#The battery of car is 200amp

#Suzuki
#Alto
#2015
#200amp

#The make of Car:Suzuki
#The model of Car:Alto
#The year of Car:2015
#Suzuki is moving with speed
#Alto has appled the break
#The battery of car is 200amp


# Changing an attributes value:

# There are two ways of changing an attributes value in a class:
#1.Direct hit the attribute
#2.Via function (get set)

# Object through assign new value in a attribute and update a attribute value
# Object thorough direct hit the variable change the value and also accesses

print("Example of Changing an attribute value:","\n")
car1.model="corallo"
car1.description()
car1.battery="300amp"
car1.descriptionbattery()
print("\n")

car2.year="2011"
car2.description()
print("\n")


# Output:
#Example of Changing an attribute value:

#The make of Car:Honda
#The model of Car:corallo
#The year of Car:2019
#The battery of car is 300amp

#The make of Car:Suzuki
#The model of Car:Alto
#The year of Car:2011


# Changing value of attribute through function
# not direct hite the property or attribute 
print("Example Changing value of attribute through function:","\n")

car1.getbatterysize()
car2.getbatterysize()
car2.setbatterysize("500amp")
car2.getbatterysize()

# Output:
#Example Changing value of attribute through function:

#The size of your car battery is 300amp
#The size of your car battery is 200amp
#The size of your car battery is 500amp