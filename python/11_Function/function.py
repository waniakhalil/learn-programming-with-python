# Function:
# What is function,why use ,importance and used ?

#Function are a way to achieve the modularity and reuseability in code.

# What is modularity?
# Modularity programming is the process of subdividing a computer program into separate sub-programs.
# A module can often be used in a variety of applications and functions with other components of the system.
# modularity means create module in which many functions when we need the function in module we call the function we need and used 

# What is Reuseability?
# Using of already developed code according to our requirement without writing from the sractch

# For Example of resuseability:
# If we given task perform many times we write one time in function then we need to use this function we call many times the function and the function perform task 

# Function Syntax or define:
print("Function Syntax or define:")
print("In python we define a function with a keyword def then the function name after the name of function we supply pair of  parentheses and a colon sign")

# Syntax or definition of function Example:

# def is definition of function add is a function name () small brackets or braces  : colon is indicate block of statement 
# after block is body of function start in the wirte of code in function we call function write code in function is execute
# function is slient mode then we call the function 
print("Example of definition of function:")
print("Function of Adds two number get input from user:","\n")
def add(): 
     number1=int(input('Enter a value:'))
     number2=int(input('Enter a value:'))
     print(number1+ number2)

# Note: Every Statement which is part of function body is a level indend more than the definition of function.

# How to call a function:
# to call the function we just need to write the name of function followed by parathenes 
add() # call the function of adds two number get input from user

#Output:
#Function Syntax or define:
#In python we define a function with a keyword def then the function name after the name of function we supply pair of  parentheses and a colon sign
#Example of definition of function:
#Function of Adds two number get input from user:

#Enter a value:45 
#Enter a value:67
#112


#function always same work we call the function we supply the value and perform the task
# Funtion: Passing information positional arguments or parameterised function :
#A generic function does not define any data it processes inside it hard-coded instead it accepts the data when it is
# called and processes that data 

# Syntax of passing information as arguments in function:
# def is keyword word indicates the function is start then function name (in given parameters or variable) : colon is indicate the 
# block of statement is start then start of body of function

print("Example of Passing information positional arguments in function:")
# in definition of function variable are parameter
#           paramenters
def adds(number1,number2): # parameterised function 
     print(number1+number2)

#Now to call the function we need to pass two arguments and they are matched according to the position in the function call
#Example:
#Here value 3 will be assigned in number1 while value5 will be assigned to number2 variable this will assigned according to postion

#   passing the values in function or arguments
adds(3,5) # dynamic value
# 3 and 5 in parameters variable according to assignment by a postion of parameters

# Note:
# two or more parmeter and arguments passing in function

# parmater less function
print("Example of parmaeter less function")
# in () small brackets is empty not parameter is pass is called parameter less function
def add():
     print("I am parameter less function")
add() # hard coded

# Output:
#Example of Passing information positional arguments in function:
#8

#Example of parmaeter less function
#I am parameter less function