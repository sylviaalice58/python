# Assignment
# 1.Write a python program that is able to calculate the BMI of a person whose weight is 78kg and height is 1.75meters. BMI=(weight)/(height squared)
weight = 78
height = 1.75
BMI = (weight)/(height**2)
print("This is the BMI", BMI)

# 2.Find the area and perimeter of a rectangle whose length is 48 cm and width is 25 cm
length = 48
width = 25
area =length * width
perimeter = (length+width)*2
print("this is the area", area)
print("this is the perimeter", perimeter)
#  Research on python list ,tuple and Dictionary Data types.
# examples of list
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# len(list)- Determines the number of items in the list
thislist = ["apple", "banana", "cherry","apple"]
print( "This is the total number of items:",len(thislist))

# list()-it uses (()) same with the list made from []
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# access an item
# a list always starts from 0 meaning the first fruit is presented bt 0
# example lets find the fruit in the second position
thislist = ["apple", "banana", "cherry","apple"]
print( "This is the second  item:",thislist[1])

# we can also find the types of items in a specific range of numbers bt the last number on the range wont be indicated
# we get fruits thats on the third, fourth and fifth place
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

# we can also change items in a list
# lets change the second and third items and see what the third item displays
mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']  #changing range items in a list
print(mylist[2])

# we can also access the last item 
mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])

# we can also display items of a range 
# eg range from the first item to the third item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# or from a particular value to the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# we can also use negative ranges. remember negative interger represent the itesa from the last meaning last value is -1
# here the value in -1 wont be displaced
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# check if item is in the list
# we can use the in keyword for this kind of process
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# we can also change the range of value of items by ADDING some items 
  thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# we can also insert items in an existing list, insert(index,item)
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist)

# we can add a single item to the end of the list. we use append. append(item)
# To add an item to the end of the list, use the append() method:
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)


# we can combine two list by using extend. 
# To append elements from another list to the current list, use the extend() method.
fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)
print(fruits)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# we can also remove an item from a list by use of remove. this is used for a specific item
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

# we can also use pop to remove items at a particular position. pop(index)
# example banana is in index 1 meaning its in the second position thus by use of pop it will be removed
# The pop() method removes the specified index.
mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist) #this will cause an error because you have succsesfully deleted "thislist".

# The clear() method empties the list.
# The list still remains, but it has no content.
mylist = ['apple', 'banana', 'cherry']
mylist.clear()
print(mylist)

# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
mylist = ["apple", "banana", "cherry"]
for i in range(len(mylist)):
  print(mylist[i])

#   List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The condition is like a filter that only accepts the items that evaluate to True.
# Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)
# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".and if the condition {if x !="apple"} is ommited all the items will be displayed

# You can use the range() function to create an iterable: with no condition

newlist = [x for x in range(10)]
print(newlist)

# Same example, but with a condition:
newlist = [x for x in range(10) if x < 5]

print(newlist)

# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
# Set the values in the new list to upper case:
# the displays in upper case
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits] 
print(newlist)
# The expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):
# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# question:whats abs and def

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
# Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:
# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# Use the copy() method
# You can use the built-in List method copy() to copy a list.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Use the list() method
# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Use the slice Operator
# You can also make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Or you can use the extend() method, where the purpose is to add elements from one list to another list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# Python Tuples
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)





