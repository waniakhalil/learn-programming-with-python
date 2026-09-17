#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< <<<<Function>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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
print('\n')

#Output:
#Function Syntax or define:
#In python we define a function with a keyword def then the function name after the name of function we supply pair of  parentheses and a colon sign
#Example of definition of function:
#Function of Adds two number get input from user:

#Enter a value:45 
#Enter a value:67
#112
 

 #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Methods to pass a value in a arguments of a  function >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("Methods to pass a value in a arguments of a function:","\n")

#function always same work we call the function we supply the value and perform the task ?
# 1.Funtion: Passing information positional arguments or parameterised function :
#A generic function does not define any data it processes inside it hard-coded instead it accepts the data when it is
# called and processes that data 

# Syntax of passing information as arguments in function:
# def is keyword word indicates the function is start then function name (in given parameters or variable) : colon is indicate the 
# block of statement is start then start of body of function

# Paramter definition:
# in definition of function variable are parameter the passes 
#           paramenters
print("1.Example of Passing information positional arguments in function:")
def adds(number1,number2): # parameterised function 
     print(number1+number2)

#Now to call the function we need to pass two arguments and they are matched according to the position in the function call
#Example:
#Here value 3 will be assigned in number1 while value5 will be assigned to number2 variable this will assigned according to postion

#  Arguments definition:
# passing the values in function or arguments
adds(3,5) # dynamic value or postional arguments 
# 3 and 5 in parameters variable according to assignment by a postion of parameters

print("Another Example of Passing information positional arguments in function:")
def fullName(first,middle,last):
      print(first+middle+last)
fullName("Wania","Khalil","Chaudhary")#Sequence matters in positional arguments 
print('\n')
# Note:
# two or more parmeter and arguments passing in function

# Output:
#Methods to pass a value in a function:
#1.Example of Passing information positional arguments in function:
#8

#Another Example of Passing information positional arguments in function:
#WaniaKhalilChaudhary


# 2.parmater less function
print("2.Example of parmaeter less function")
# in () small brackets is empty not parameter is pass is called parameter less function
def add():
     print("I am parameter less function")
add() # hard coded
print("\n")

# Output:
#2.Example of parmaeter less function
#I am parameter less function


# If position is disturbed we use keyword of parameter in arguments
# 3.Function: Passing information keywords arguments
#In Python, keyword arguments are used to pass information to a function by specifying the parameter name.

# Syntax of passing information keyword of parameter in argument same as assing information as arguments in function:
print("3.Example of Passing information keywords of paramter in arguments:")
def add(number1,number2):
     print(number1+number2)

# Call the function of passing information keyword arguments:
add(number1=3,number2=5)
#There is another way to call same function of adds  that we pass the arguments with the name of a variable 
#this way position does not matter but the value is assigned to matching variable in function 
# it is not assign by position like assing information as arguments in function it we assigned keyword of parameter 
# will be assigned
# Attache keyword with arguments

print("Another Example of passing information keywords of parameter:")
def fullName(first,middle,last):
     print(first+middle+last)
fullName(last="Chaudhary",first="Wania",middle="Khalil") # Keyword argument 

# Note:
# if you dont want pass all arguments keyword of parameter which argument pass keyword paramter in a last 
# beacuse positional arguments follow keyword argument:
print("Example of positional arguments follow keyword argument:")
fullName('Wania','Khalil',last='Chaudhary')
print("\n")

# Output:
#3.Example of Passing information keywords of paramter in arguments:
#8

#Another Example of passing information keywords of parameter:
#WaniaKhalilChaudhary

#Example of positional arguments follow keyword argument:
#WaniaKhalilChaudhary


#<<<<<<<<<<<<<<<<<<<<<<<<<Methods to pass a value in a parameters in a function>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("Methods to pass a value in a parameters in a function:","\n")

 
# 1.Function:Default Value parameter 
#A default parameter is a parameter that already has a value in the function definition. If the user does not provide a value, Python uses the default value.

print("1.Example of Default value parameter:")
def add(number1=0,number2=0):
     print(number1+number2)

# Call the Default Value parameter function:
add(number2=5)
# There are times when some parameter value are optional but still you need a default a value in case if someone 
# does not provide the value to any void any non deterministic behaviour 
# if a user not given arguments in a call of function if a function excute we given default value used in a parameter
# if user given arguments default parameter is not used

# Note 
# if you pass default parameters pass in last of list not first and end in definition  of function
print("Another Example of Default value parameter:")
def fullName(first,last,middle=" "):
     print(first+middle+last)
fullName("Wania",'Chaudhary')

#Output:
#Methods to pass a value in a parameters in a function:

#1.Example of Default value parameter:
#5
#Another Example of Default value parameter:
#Wania Chaudhary



