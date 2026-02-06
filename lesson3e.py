# Below is a grading system based on what a student will have gotten
marks = int(input("Enter students marks: "))
# print("Entered marks is ", marks)
if marks > 0 and marks < 90:
    print("Below avarage")
elif marks >=30 and marks < 40:
    print(Average)
elif marks >= 40 and marks < 70:
    print("Above Avarage")
elif marks >= 70 and marks <= 100:
    print("Excellent")
else:
    print("invalid input")
