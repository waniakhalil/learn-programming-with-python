# Loop:
# Definition:
# Any task repeated or repeatly perform task is called loop
# if one code write many times is solution is loop
# for example : if your task is print you name 50 times you code write 50 times is time confusing and not flexiable best  and fescant way is using loop 
# loop have starting and ending point  tells how many times loop run
# loop execute task perform

# types of loop:
# In python we study two types of loops :
# 1.for loop
# 2.while loop

# for loop syntax:
# for(keyword) element or variablein( list name) :
#: indicates the block of loop
# indentation topic study in if-else statement

# loops start and end in between no stop in loop and is solution is used two ways:
# 1.break use keyword in loop for terminate and exit the loop execution and not run the loop
# 2.coutinue use keyword skip the loop after continue execution stop but loop is run

# loop syntax:
# for is keyword in loop 
# a is variable name in loop you can use any name in loop
# in is keyword in loop you can use any keyword in loop
# range is function in loop you can use any number in loop
# 5 is number of times loop 
#: indicates the block of loop and start of body of loop
# indentation is used to indicate the block of loop

# Example of syntax:
print('Example of for loop synatx and print you name 5 times using for loop:','\n')
for a in range(5):# 5 will not be included in loop (0,1,2,3,4) it start from 0 and end at 4
    print(a,"wania",'\n') # a indicates loop execution how many times loop run 

# Output:
#Example of for loop synatx and print you name 5 times using for loop:
# 0 wania 
# 1 wania 
# 2 wania 
# 3 wania 
# 4 wania 

# Example of range in single parameter  :
print('Example of range in single parameter given in for loop:','\n')
for numbers in range(10):
    print(numbers,'\n')

# Output:
#Example of range in single parameter given in for loop:
#0 
#1
#2
#3   
#4 
#5 
#6
#7
#8
#9

# Example of range start and ending point of two parameter given:
print('Example of range in which starting and ending point of two parameter given in loop:','\n')
for numbers in range(1,10):#  1 is a starting point and 10 is ending point of loop
    print(numbers,'\n')

# Output:
#Example of range in which starting and ending point of two parameter given in loop:'
#1
#2
#3   
#4 
#5 
#6
#7
#8
#9
#10

# Example of range is step in three parameter given:
print('Example of Range is step in three parameter  given in loop:','\n')
for number in range(1,10,2): # 2 indicates step third parameter 
    print(number,'\n')

# Output:
#Example of Range is step in three parameter  given in loop:
#1
#3
#5
#7
#9

# Reverse Number print Example:
print('Example of Reverse Number Print by loop','\n')
for b in range(10,1,-2):
    print(b,'\n')

# Output:
#Example of Reverse Number Print by loop
#10
#8
#6
#4
#2 

# In list used loop:
cities=['karachi','lahore','Islamabad']
print(f"The list of cities acesses using loop : {cities}",'\n')
for city in cities:
    print(f'The city is:{city}','\n')

#Output:
# The list of cities acesses using loop:['karachi','lahore','Islamabad']
# The city is:karachi
# The city is:lahore
# The city is:Islamabad 

# in list direct given:
print('Direct given list in loop:','\n')
for num in [11,22,33,44,55]:
    print(num,'\n')

# Output:
#'Direct given list in loop:'
# 11
#22
#33
#44 
#55

# Character print using loop:
print("Print Character using Loop:",'\n')
country='Pakistan' # print one character of this string element 
for char in country:
    print(char)

# Output:
# Print Character using loop
# Pakistan

# tuples using loop:
print('Tuples using loop:','\n') # in tuples store one or more element using loop print full element of character 
country='Pakistan', 'China','Japan'
for tup in country:
    print(tup)

# Output:
#Tuples using loop:
# Pakistan
# China
# Japan


# In for loop study of break and continue:
#   Example of break:
print("Using break in loop:")
print("1.Example 0 is unequal and not  divisible by 3:")
for num in range(10):
    if num%3!=0: # % modulus when use not complete divisble and have remainder 
                 # != indicies sign means not equal 
        break
    print(num,'\n')

# Output:
# Using break in loop
#1.Example 0 is unequal and not  divisible by 3 
# 0

print("2.Example 1 is equal and not  divisible by 3: ")
for num in range(10):
   if num%3==1:
    break
   print(num,'\n')

#Output:
# 2.Example 1 is unequal and not  divisible by 3 
# 0

print("3.Example 0 is equal and not divisible by 3: ")
for num in range(10):
   if num%3==0:
    break
   print(num,'\n')

#Output:
# 3.Example 0 is equal and not divisible by 3
# not print 

print("4.Example 0 is equal and not divisible by 2:")
for num in [5,7,11,90]:
    if num%2==0:
     break
    print(num,'\n')

# Output:
#4.Example 0 is equal and not divisible by 2
# 5
#7
#11

print('Using Continue in loop:')
print('Example check according given range and condition:')
for num in range(10):
    if num==7 or num==4:
        continue
    print(num,'\n')

#Output:
#Using Contine in loop
# Example check according given range and condition
#0
#1
#2
#3 
#5
#6
#8
#9
#10

# Real world Example of for loop: (Multiplication of table:)
print('Real World Example of for loop:')
print('Print table using for loop and Input from user:')
tablenumber=int(input("Enter a number for table print:"))
for a in range(1,11):
    print(f"{tablenumber} * {a} = {tablenumber*a}")

#Output:
# Real World Example of for loop:
#Print table using for loop and Input from user:
#Enter a number for table print:4
#4 * 1 = 4
#4 * 3 = 12
#4 * 4 = 16
#4 * 5 = 20
#4 * 6 = 24
#4 * 7 = 28
#4 * 8 = 32
#4 * 9 = 36
#4 * 10 = 40
