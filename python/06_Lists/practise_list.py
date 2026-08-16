# list is bunch or set of  a elements store in a single variable
# list access in a index

name=['wania','husnain','sawera','ubaidullah','merub'] # list assign by square bracket or equal to sign is assign a value 
#index  0      1             2       3          4
print(name)

# if list not have make many variable
city1="karachi"
city2="lahore"
city3="islamabad"
city4="multan"
# list define in a single variable
cities=["karachi","lahore","islamabad","multan"]
# index   0         1         2         3 
print(cities)


# how to access Value in  alist 
# Access value through index 
# get a particular value from list 
print(name[1])
print(cities[3])


# Check the lenght of cities
fruits=[] # no value or elements in a list 
print(len(fruits))
print(len(cities))


# adding a element or value in a list  {append & insert two mwthods}
# append function use for add element or value last of a list by default
fruits.append("watermelon")
print(fruits)
fruits.append("mango")
print(fruits)
# insert function also work like append function but you adding value or element which index you want adding
fruits.insert(1,"stawberry")
print(fruits)
# but append and insert function you only add one value or element in a list not more than one
# extend function do this work adding one or more value in function or iterable (loop) and also adding value in end of the list like append fucntion
fruits.extend(["blueberry","orange","apple","cherry","watermelon","mango","orange"])
print(fruits)


# count the same values in a list used count function 
print(fruits.count("orange"))


# index function used for find a value of index in a list
print(fruits.index("orange")) # if repeat value index function given of repeat first value
print(fruits.index("cherry"))

# clear function in a index remove the all value or elements in a list 
# it remove permanent value of a list
print(fruits.clear())

fruits=["apple","mango","orange","bananana","grapes"]
#Copy Function
# Copy the list and store in another variable
fruits2=fruits.copy() # by value copy it is the new copy not refernce not point each other

fruits3=fruits # by reference copy  refernce lsit fruit3 point to  list fruits or  connected to a with list of fruit change in a list also changed in  a reference list 

fruits.append("stawberry")
print(fruits3)
print(fruits2)

# removing value from the list {del,remove (),pop}
# del is a statement 
# del delete a permanent value from list 
del fruits2[2] # delete by pass the index
print("fruit2 list delete the value of access in index 2:",fruits2)

#remove function
# remove is a function
fruits2.remove("mango") # remove by value
print("Remove function remove value in fhr fruits2 is mango:","\n",fruits)

# pop function
# pop function also roemve value in a list by index like del statement
# return remove and delete value and store a value in variable and reuse
# pop del and remove from end vakue of the list by default 
poppedcities=cities.pop()
print(f"The city is popped from cities list {poppedcities}")
#f stands for formatted string literal (f-string). It is used to insert variables or expressions directly inside a string by enclosing them in curly braces {}.
print(f"The remaining cities in the cities list {cities}")

# pop also by pass index and value in a pop function
poppedcities=cities.pop(1)
print(f"The pop value from the cities list access value in index 2:{poppedcities}")
print(f"The remaining cities in the cities list {cities}")

# sort function
# sort means sort value in  ascsending and descending order
# in Ascending order sort 
name.sort()
print(name)
# in descending order sort 
name.sort(reverse=True)
print(name)


# reverse function 
# list order reverse
name.reverse()
print(name)