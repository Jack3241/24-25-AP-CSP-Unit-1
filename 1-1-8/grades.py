my_courses = ["English", "Math", "CS"]

redo = "y"
while (redo == "y"):
 for course in my_courses:
    print()
    print("Enter your points for " + course)

    points = int(input("Points -> "))

    if (points >= 90):
        print("A")
    elif (points >= 80):
        print("B")
    elif (points >= 70):
        print("C")
    elif (points >= 60):
        print("D")
    else:
        print("F")


redo = "y"
while (redo == "y"):
    redo = input("Do you need to re-do these grades? (y/n)")
