# Loops Assignment 
# 1. Using a while Loop Print from 2000 to 2024 -

year= 2000
while year <=2024:
    print(year)
    year=year+4

print("--------------------------------------------")
# 2. Create a List of Colors Blue, Green, Red, Pink , Black- Using a for Loop, Loop through the Colors 

colors=["Blue","Green","Red","Pink","Black"]
for color in colors:
    print(color)

print("-----------------------------------------")    
 
#  3.Using a While Loop Print from 20 to 1

number = 20
while number >=1:
    print(number)
    number=number-1

# Research on python functions. Both with parameters and without parameters
# Python Functions
# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# A function helps avoiding code repetition.
# In Python, a function is defined using the def keyword, followed by a function name and parentheses:
# To call a function, write its name followed by parentheses:

def my_function():
  print("Hello from a function")

my_function()
# You can call the same function multiple times:
# The code inside the function must be indented. Python uses indentation to define code blocks.

# Function names follow the same rules as variable names in Python:

# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)

# Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program. Without functions, you would have to write the same calculation code repeatedly:

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

print("----------------------------------------")
# With functions, you write the code once and reuse it:
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# Return Values
# Functions can send data back to the code that called them using the return statement.
# When a function reaches a return statement, it stops executing and sends the result back

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

# Using the return value directly:
def get_greeting():
  return "Hello from a function"

print(get_greeting())

# If a function doesn't have a return statement, it returns None by default.
def my_function():
  pass

# The pass statement is often used when developing, allowing you to define the structure first and implement details later.
print("------------------------------------------------")
# Python Function Arguments
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# A function with one argument:

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Parameters vs Arguments
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the actual value that is sent to the function when it is called.

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

# Number of Arguments
# By default, a function must be called with the correct number of arguments.

# If your function expects 2 arguments, you must call it with exactly 2 arguments.
#This function expects 2 arguments, and gets 2 arguments::

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
 
print("---------------------------------------")
# Default Parameter Values
# You can assign default values to parameters. If the function is called without an argument, it uses the default value:

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

print("-------------------------------------")
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print("-------------------------------------------")
# Keyword Arguments
# The phrase Keyword Arguments is often shortened to kwargs in Python documentation.
# You can send arguments with the key = value syntax.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# This way, with keyword arguments, the order of the arguments does not matter.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

print("---------------------------------------")
# Positional Arguments
# When you call a function with arguments without using keywords, they are called positional arguments.

# Positional arguments must be in the correct order:
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

print("-------------------------------------")
# Switching the order changes the result:

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")

print("----------------------------------------------")
# Mixing Positional and Keyword Arguments
# You can mix positional and keyword arguments in a function call.

# However, positional arguments must come before keyword arguments:
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

print("--------------------------------------------")

# Passing Different Data Types
# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).

# The data type will be preserved inside the function:
#  Sending a list as an argument:

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

print("--------------------------------------------")

# Sending a dictionary as an argument:

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {
  "name": "Emil", "age": 25
  }
my_function(my_person)

print("--------------------------------------------")

# Functions can return values using the return statement:

# Example

def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

print("--------------------------------------------")
# Functions can return any data type, including lists, tuples, dictionaries, and more.

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

print("--------------------------------------------")
# A function that returns a tuple:

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y )

print("--------------------------------------------")
# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments.

# To specify positional-only arguments, add , / after the arguments:
def my_function(name, /):
  print("Hello", name)

my_function("Emil")

print("--------------------------------------------")

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(name):
  print("Hello", name)

my_function(name = "Emil")

# With , /, you will get an error if you try to use keyword arguments:
# def my_function(name, /):
#   print("Hello", name)

# my_function(name = "Emil")

print("--------------------------------------------")

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

print("--------------------------------------------")


# Combining Positional-Only and Keyword-Only
# You can combine both argument types in the same function.

# Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

print("------------------------------------------------")

# Python *args and **kwargs
# *args and **kwargs allow functions to accept a unknown number of arguments.

# Arbitrary Arguments - *args
# If you do not know how many arguments will be passed into your function, add a * before the parameter name.
# This way, the function will receive a tuple of arguments and can access the items accordingly:
# Using *args to accept any number of arguments:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

print("------------------------------------------------")
# What is *args?
# The *args parameter allows a function to accept any number of positional arguments.

# Accessing individual arguments from *args:

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

print("------------------------------------------------")

# Using *args with Regular Arguments
# You can combine regular parameters with *args.

# Regular parameters must come before *args:
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

print("------------------------------------------------")

# A function that calculates the sum of any number of values:

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

print("---------------------------------------------")

# Finding the maximum value:

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))

# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

# This way, the function will receive a dictionary of arguments and can access the items accordingly:
# Using **kwargs to accept any number of keyword arguments:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# What is **kwargs?
# The **kwargs parameter allows a function to accept any number of keyword arguments.

# Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")


print("-------------------------------------------")

# Using **kwargs with Regular Arguments
# You can combine regular parameters with **kwargs.

# Regular parameters must come before **kwargs:
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

print("-------------------------------------------")

# Combining *args and **kwargs
# You can use both *args and **kwargs in the same function.

# The order must be:

# regular parameters
# *args
# **kwargs

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

print("------------------------------------")

# Unpacking Arguments
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
# Unpacking Lists with *
# If you have values stored in a list, you can use * to unpack them into individual arguments:

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

print("----------------------------------------")

# Unpacking Dictionaries with **
# If you have keyword arguments stored in a dictionary, you can use ** to unpack them:

# Using ** to unpack a dictionary into keyword arguments:

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

print("--------------------------------------------")
# Python Scope
# A variable is only available from inside the region it is created. This is called scope.
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
# A variable created inside a function is available inside that function:

def myfunc():
  x = 300
  print(x)

myfunc()

print("---------------------------")

# Function Inside Function
# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

# The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

print("---------------------------------------")

# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

# A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

print("_-----------------------------------------")
# Naming Variables
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

# The function will print the local x, and then the code will print the global x:
x = 300 #global

def myfunc():
  x = 200
  print(x) #local

myfunc()

print(x)

print("----------------------------------------")

# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# The global keyword makes the variable global.
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 300

myfunc()

print(x)

print("----------------------------------------------")
# Also, use the global keyword if you want to make a change to a global variable inside a function.
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

print("-------------------------------------------------")

# Nonlocal Keyword
# The nonlocal keyword is used to work with variables inside nested functions.

# The nonlocal keyword makes the variable belong to the outer function.
#If you use the nonlocal keyword, the variable will belong to the outer function:

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

print("----------------------------------------------")
# The LEGB Rule
# Python follows the LEGB rule when looking up variable names, and searches for them in this order:

# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace

# Understanding the LEGB rule:

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

print("-----------------------------------------")

# Python Decorators
# Decorators let you add extra behavior to a function, without changing the function's code.

# A decorator is a function that takes another function as input and returns a new function.
# Define the decorator first, then apply it with @decorator_name above the function.

# A basic decorator that uppercases the return value of the decorated function.

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

# By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.

# The function changecase is the decorator.

# The function myfunction is the function that gets decorated.
print("-------------------------------------------")
# Multiple Decorator Calls
# A decorator can be called multiple times. Just place the decorator above the function you want to decorate.
# Using the @changecase decorator on two functions:
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

print("-----------------------------------------")

# Functions that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function:

def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

print("-------------------------------------------")

# Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.

# Secure the function with *args and **kwargs arguments:

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

print("-----------------------------------------")

# Decorators can accept their own arguments by adding another wrapper level.
# A decorator factory that takes an argument and transforms the casing based on the argument value.

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

print("----------------------------------------")

# Multiple Decorators
# You can use multiple decorators on one function.

# This is done by placing the decorator calls on top of each other.

# Decorators are called in the reverse order, starting with the one closest to the function.

# One decorator for upper case, and one for adding a greeting:

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

print("-------------------------")
# Preserving Function Metadata
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

# Normally, a function's name can be returned with the __name__ attribute:

def myfunction():
  return "Have a great day!"

print(myfunction.__name__)