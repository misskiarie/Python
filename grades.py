marks=int(input("Enter student's score"))
if marks > 80 and marks <= 100:
    print("You scored an A")
elif marks > 60 and marks <= 80:
    print("You scored an B")
elif marks >40 and marks <= 60:
    print("You scored an C")
elif marks > 30 and marks <= 40:
    print("You scored an D")
elif marks > 0 and marks <= 30:
    print("Sorry you failed :(")
else:
    print("Wrong input")