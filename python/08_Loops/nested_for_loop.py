# Nested For loop
# One loop in one or more loop is called nested loop

# Example of Nested for loop:
print('Example of nested for loop:')
for a in range(5):
    print('Inner loops Begins:')
    for char in "China":
        print(a,char)

# Output:
#Example of Nested for loop:
#0 C
#0 h
#0 i
#0 n
#0 a
#1 C
#1 h
#1 i
#1 n
#1 a
#2 C
#2 h
#2 i
#2 n
#2 a
#3 C
#3 h
#3 i
#3 n
#3 a
#4 C
#4 h
#4 i
#4 n
#4 a

# Real world Example of for loop: (Multiplication of table)
print('Real World Example of nested for loop:')
print('Print a range of table using nested for loop and Input from user:')
tables=int(input("Enter a range of table:"))
for table in range(1, tables+1):
     for a in range(1,11):
         print(f"{table} *{a}= {table*a}")

#Output:
#Real World Example of nested for loop:
#Print a range of table using nested for loop and Input from user:
#Enter a range of table:3
#1 *1= 1
#1 *2= 2
#1 *5= 5
#1 *6= 6
#1 *7= 7
#1 *8= 8
#1 *9= 9
#2 *1= 2
#2 *2= 4
#2 *4= 8
#2 *5= 10
#2 *6= 12
#2 *7= 14
#2 *8= 16
#2 *9= 18
#2 *10= 20
#3 *1= 3
#3 *2= 6
#3 *3= 9
#3 *4= 12
#3 *5= 15
#3 *6= 18
#3 *7= 21
#3 *8= 24
#3 *9= 27
#3 *10= 30
