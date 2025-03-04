grade = input("Enter your grade (o, a, b, c, f): ").strip().lower()

if grade == 'o':
    print("Outstanding")
elif grade == 'a':
    print("Very Good")
elif grade == 'b':
    print("Good")
elif grade == 'c':
    print("Average")
elif grade == 'f':
    print("Fail")
else:
    print("Invalid grade entered. Please enter one of the following: o, a, b, c, f.")
