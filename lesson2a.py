# python list
# Alist in python is a collection of items that ordered in a certain way.
# A list is introduced by the use of square brackets[]
# Items of a list are stored inside of indexes .
# IN PROGRAMMING WE START COUNTING FROM INDEX ZERO(0). bmw, benze, hiance, ..
# A list is mutable ie the contents of a list can be changed

car =["BMW","Benze","Hiance","Prado","Probox","Mclarel","Range"]
print(car)
print(type(car))

# Accessing items og a list
print(car[2])
print( "The car on index four is:", car[4])

# list slicing - This is creating a list from a given bigger list
print(car[4:])

# print from start to prado
print(car[ :4])

# print from hiance to probox
print(car[2:5])

# list mutability
# we use the function append to add an item at the end of a list
car.append("Mercedees")
print(car)

car.append("subaru")
print(car)

# we use the pop function to remove an item at end og list
car.pop()
print(car)

# we can use an index to add item to a list
car[5] = "Pajero"
print(car)

# we can use the sort function in alphabetical order
car.sort()
print(car)