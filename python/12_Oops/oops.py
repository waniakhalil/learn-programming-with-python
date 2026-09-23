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

print("Example of classes and object:")
class Car():
 # attributes >>>>>>>> are variables in programming
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

# behaviour >>>>>>>>>> are function in programming 
    def description(self):
        print(f"The make of Car:{self.make}")
        print(f"The model of Car:{self.model}")
        print(f"The year of Car:{self.year}")
    def move(self):
        print(f"{self.make} is moving with speed")
    def applyingbreak(self):
        print(f"{self.model} has appled the break")
