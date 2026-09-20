#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<While loop>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Definition and why use and importance of loop in for loop folder 

#We have studied loops in earier ways like (nested and for loop). There is another type of loops called while loop
# Defintion:
#They are similar to for loops but differ in the sense that it allows user to terminate loop  setting flags
# While loop also used iterate or repeadly any task 
# functionality same of for and while loop 

# Difference between for and while loop:

# for loop start and end of sudden point of during excution
# While loop  provide chocie to user loop terminate any sudden point or end of excution of loop

# For termination using flags is variable we set a condition in while loop if condition come true or fale terminate


#Syntax of While loop:

#  keyword
# While     Conditon:
#        statemtent

print("Syntax of While loop:") 
print('while loop key word while then condition (:) colon start of block of statement or body of loop then given one or more statemnent',"\n")

print("Example of While loop:")

a=0
while a<10: # While loop condition is false is terminate when condition is true is excute 
    print(a,"This is a while loop printing ") 
    a+=1
print("\n")

# Output:
#Syntax of While loop:
#while loop key word while then condition (:) colon start of block of statement or body of loop then given one or more statemnent 

#Example of While loop:
#0 This is a while loop printing 
#1 This is a while loop printing 
#2 This is a while loop printing 
#3 This is a while loop printing 
#4 This is a while loop printing 
#5 This is a while loop printing 
#6 This is a while loop printing 
#7 This is a while loop printing 
#8 This is a while loop printing 
#9 This is a while loop printing 

print("Example of  user input using while loop:")
a=0
while a<10:
    userinput=input("Enter your Favourite car:")
    a+=1

# Ouput:

#Example of  user input using while loop:
#Enter your Favourite car:bwm
#Enter your Favourite car:toyota
#Enter your Favourite car:civic
#Enter your Favourite car:alto
#Enter your Favourite car:supra
#Enter your Favourite car:ferria
#Enter your Favourite car:corolla
#Enter your Favourite car:audi
#Enter your Favourite car:Tesla
