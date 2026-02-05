# A dictionary is a data type that stores data in terms of key- value pair
# It is introduced by the use of curly brace{}
# The values stored inside of a dictionary van be of any data type.
# to access the values in a dictionary we use the keys

phonebook ={
    "Benson" : "2547431233",
    "Mary" : "25476413130",
    "stephen" : "2547451133"
}
# showing the entire phone book
print(phonebook)
print(type(phonebook))

# printing out bensons number
print(phonebook["Benson"])

print('===================================')

player ={
    "name" : "Messi",
    "age" : 40 ,
    "teams" : ["PSG","Bercelona","Argentina"]
}

print(player["teams"][1])

