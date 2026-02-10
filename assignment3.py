gross_income = int(input("Enter Gross income "))

if gross_income > 0 and gross_income <= 5999:
    print("Monthly contribution is", 150.00)
elif gross_income <= 7999:
    print("Monthly contribution is", 300.00)
elif gross_income <= 11999:
    print("Monthly contribution is", 400.00)
elif gross_income <= 14999:
    print("Monthly contribution is", 500.00)
elif gross_income <= 19999:
    print("Monthly contribution is", 600.00)
elif gross_income <= 24999:
    print("Monthly contribution is", 750.00)
elif gross_income <= 29999:
    print("Monthly contribution is", 850.00)
elif gross_income <= 49999:
    print("Monthly contribution is", 1000.00)
elif gross_income <= 99999:
    print("Monthly contribution is", 1500.00)
else:
    print("Monthly contribution is", 2000.00)
    