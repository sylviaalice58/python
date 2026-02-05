# Tuple
# Is an immutable type of a list (it can not change)
# To introduce a tuple , we use the parenthesis()

counties =("Nairobi", "Mombasa", "Nakuru","Eldoret","Kajiado","Kisii")
print(counties)
print(type(counties))

# slicing of tuple
print(counties[3:])

# accessing items of a tuple by use of the indexes
print(counties[5])

# Note: Below will generate an error
# Attribute error
counties.append("Machakos")
print(counties)