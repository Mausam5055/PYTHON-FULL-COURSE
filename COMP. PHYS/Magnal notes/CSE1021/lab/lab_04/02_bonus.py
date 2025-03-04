salary = float(input("Enter the salary of the employee: "))
sex = input("Enter the sex of the employee (Male/Female): ").strip().lower()

if sex == 'male':
    bonus = salary * 0.05
elif sex == 'female':
    bonus = salary * 0.10
else:
    print("Invalid input for sex. Please enter 'Male' or 'Female'.")

print(f"The bonus for the employee is: {bonus}")
