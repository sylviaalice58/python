# Loops -> Sometimes we may need to do a piece of work a number of repeated in time such cases we may use loops.
#  a loop is a control structure that allows us to execute a block of code respectively until a certain condition is met
# There are two types of loopd for loop and while loop

# Below is the syntax of a for loop in python:
"""
for variable in range(n):
#    block of code to be executed
"""
# print("Hello Moses")
# print("Hello Moses")
# print("Hello Moses")
# print("Hello Moses")
# print("Hello Moses")

for greeting in range(5):
    print("Hello Moses", greeting)

print("______________________________________________________________________")    

for number in range (10, 20):
    print(number)

print("______________________________________________________________________") 
#  Find the even numbers in the range of 50 to 71
for number in range(50,71, 2):
    print(number)

print("______________________________________________________________________") 
# Create a python program that prints the odd numbers from 100 to 150
for number in range(100 ,150):
    if number % 2 !=0:
     print(number)

print("______________________________________________________________________") 
 # create a program that prints the multiples of 3 starting from 201 to 250
for number in range(201, 149, -3):
   print(number)

print("______________________________________________________________________") 
# Create a python program that prints the leap years between 2000 and 2024
for year in range(2000 ,2024 ):
   if year % 4 ==0:
    print(year)
