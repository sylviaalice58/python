# python function
# They are a block of code/ statements that perform a given task/functions. They can be reused  through out the program to perfon different tasks
# Functions are defined using the def keyword,(define)
# We have two main types of the functions ie
# 1- In-buit functions-> They come preinstalled with the interpreter ie print(), pop(), range() ,append()
# 2. user defined finctions=> They are created by a programmer to solve a given task.
# To define a function you need to give it a name followed by paranthesis
# For the functions, it is usaualy indented and to invoke a function we use the function name,

def greetings():
    print("Hello, how are you?")

    # below we call the function by use of its name
greetings()   

print("_-------------------------------------------------------------")
# Addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is:",sum)

addition()    

print("------------------------------------")
# create a function that is able to multiply 3 values

def multiply():
    numb1 = 3
    numb2 =  5
    numb3 =  2
    mult = numb1*numb2*numb3
    print("The product of the numbers is: ",mult)

multiply()

print("------------------------------------")

# Below is a division function
def divide():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    quotient = number1/number2
    print("The answer is: ",quotient)
    print("-------")

for function in range(3):
     divide()    