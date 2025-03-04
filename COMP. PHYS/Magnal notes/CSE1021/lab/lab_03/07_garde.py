grade = input("Enter a grade (O, A, B, C, F): ")
grade = grade.upper()

if grade == 'O':
    print("Outstanding")
elif grade == 'A':
    print("Very Good")
elif grade == 'B':
    print("Good")
elif grade == 'C':
    print("Average")
elif grade == 'F':
    print("Fail")
else:
    print("Invalid input! Please enter one of the following grades: O, A, B, C, F.")
