# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.

def simple(p ,r ,t):
    si=p*r*t/100
    print("The simple interest is : ",si)

for x in range(2):
    print(simple) 
simple(45000, 7, 8 )       