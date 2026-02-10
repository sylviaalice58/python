# A for loop can also be used to iterate through a list, tuple , string or even a dictionary.

name = "Sylvia"

for letter in name:
    if letter == "l":
        print("This is letter l")
    else:
        print(letter)

print("-------------------------------------------")
# below is a list of counties
counties =["Nairobi","Mombasa","Kisumu","Nakuru","Eldoret","Kajiado","Machakos","Meru","Embu"]

print(counties)

for county in counties:
    print(county)

print("-------------------------------------------")

search =input("Enter county ")

found=False

for county in counties:
    if county== search:
        found=True
        break

if found:
    print(search," is found")
else:
    print(search," is not available")    



# print("-------------------------------------------")

player ={
    "name" : "Mbappe",
    "age" : 25,
    "team" : ["PSG","Monaco","France"],
    "nationality" : "French"
} 

for key in player:
     print(player)

# print only values of the player. We can use the values or any letter eg x
for x in player:
    print(player[x]) 

# Loop through the teams the player has played for
# print (player["team"]) 
for team in player ["team"]:
    print(team)
