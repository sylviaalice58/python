# functions with parameters
# They are values that get passed as arguments give to a function inside of the parenthesis

def greetings(name):
    print(f"{name} How are you? Hope everything is fine.")

greetings("Sylvia") 
greetings("Alice")   


print("=======================")
def message(names):
    print(f"Hello {names} , We shall be having a geeneral meeting on date..... Please avail Yourself")

message("Joy")
message("Steven")

# Create function that accepts parameters to add two numbers
def addition(x , y):
    sum= x + y
    print("The sum of the numbers is: ",sum)

addition(45,69)   
addition(60 , 78) 
 
    
    