#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Data File>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# In all the coding so far in this book,none of the data has been perserved .we created variables,list ,dictionaries,loops,range through number,while loop
# and class instance that contain information,but as soon as the computer or program was turned off ,all of it disappeared
# All Coding in python generate a value During programming and execution of programming  all avlues is finish when program is off
# Generate Variable or number   are not stored permanent 

# we save document working on ms word,ms excel etc save document  then we reopen exact save things we see
# we store python code or code file permenent write in data file if program finish store in datafile permenant 
#you known  how to save a word processing document or spreadsheet ,but how do you save data processing by python ?
# we see external file program transfer to another file

# External file is not coding file 
# How write in external file from coding file?
# Reading Writing in an external file from python code 

# We can write in a text file by using a python function:

# Syntax:
# With open("file_name.txt,"mode")

# mode decided three this things in external file 
# There are three modes:
# Read,Write and append

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Mode>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 1.Writing to a text file:(write mode) or also create a file

# Syntax:
#   file oepn             file name  wirting mode  handler name (own ) handler is file we handle
# with open ("myFile.text","w")          as file:
#    file.write ("This is my file")

#Note:if file does not exist "w" mode will create and write in it 
# if you not file exist create file "w" mode create file and write in it 



# 2. Reading from a text file:

# Syntax:
#                         read mode 
# with open("myFile.txt","r") as file:
#    varivale store a file content 
#    contents_of_file=                file.read()
# print(content_of_file)

# Note:if file does not exist "r" mode will throw file not found error


# 3.Writing a file in append mode:

# Syntax:
#                      append mode 
# with open("myFile.txt,"a") as file:
#    file.write("This text is written in append mode")

# Note:in "w" mode if we write in same file all previous work will be overwrite but append mode allows to write further 
# we indent of function or block of statemnt is finished or exist automatically file is closed  we open again the file with open
# write a data perivious data is finished or over write if closed file we open again file write txt for not remove data then we use
# append mode not removed perivous data add further data 
# not create file in append mode 

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Basic mode updated version mode >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#1. r+  mode allows read and write in file (reading mode) not create a file  or error 
#2. w+  mode allows read and write in file (writing mode) also create a file 
#                               both function write in updated version mode 

print("1.Example of Reading Mode in datafile")
# open function return handler function
with open("python/13_Datafiles/testingdatafile.txt","r") as file:
    content=file.read()
print(content)

#Output:

#1.Example of Reading Mode in datafile
#this is a test file .we will read the file from python code