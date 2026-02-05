# Create a Tuple of 8bDifferent Planets
# print all the planets
# Print the planet from index 2 to 6

planets=("Earth","Sartun","Mars","Mercury","Venus","Jupiter","Neptune","Uranus")
print(planets)
print(planets[2:7])


# research on if.....else statements 

# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.
# An "if statement" is written by using the if keyword.
a = 33
b = 200
if b > a:
  print("b is greater than a")

#   The if statement evaluates a condition (an expression that results in True or False). If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.
# Checking if a number is positive:

number = 15
if number > 0:
  print("The number is positive")

#   Multiple Statements in If Block
# You can have multiple statements inside an if block. All statements must be indented at the same level.
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

# Boolean variables can be used directly in if statements without comparison operators.
# Using a boolean variable:

is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#   Python can evaluate many types of values as True or False in an if statement.
# Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True.
# This includes positive numbers (5), negative numbers (-3), and any non-empty string (even "False" is treated as True because it's a non-empty string).

# Python Elif Statement
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#   You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
#   When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.
# Important: Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.

# Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

#   Python Else Statement
# The else keyword catches anything which isn't caught by the preceding conditions.
# The else statement is executed when the if condition (and any elif conditions) evaluate to False.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#   You can also have an else without the elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#   Note: The else statement must come last. You cannot have an elif after an else.

# Checking even or odd numbers:

number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

# he else statement acts as a fallback that executes when none of the preceding conditions are true. This makes it useful for error handling, validation, and providing default values.
# Example
# Validating user input:

username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

# Python Shorthand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
a = 5
b = 2
if a > b: print("a is greater than b")

# Short Hand If ... Else
# If you have one statement for if and one for else, you can put them on the same line using a conditional expression:
a = 2
b = 330
print("A") if a > b else print("B")

# You can also use a one-line if/else to choose a value and assign it to a variable:
# Example

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
# The syntax follows this pattern:
# variable = value_if_true if condition else value_if_false

# You can chain conditional expressions, but keep it short so it stays readable:
# Example
# One line, three outcomes:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# Important: While shorthand if statements can make code more concise, avoid overusing them for complex conditions. For readability, use regular if-else statements when dealing with multiple lines of code or complex logic.


# Python Logical Operators
# Logical operators are used to combine conditional statements. Python has three logical operators:
# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true

# The and Operator
# The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.
# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#   The or Operator
# The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.
# Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#   The not Operator
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement.
# Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#   You can combine multiple logical operators in a single expression. Python evaluates not first, then and, then or.
# Combining and, or, and not:

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

#   Using Parentheses for Clarity
# When combining multiple logical operators, use parentheses to make your intentions clear and control the order of evaluation.
# Using parentheses for complex conditions:

temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")


#   User authentication check:
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")