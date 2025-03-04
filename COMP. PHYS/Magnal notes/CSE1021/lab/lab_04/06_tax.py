def calculate_tax(salary):
    if salary <= 250000:
        return 0 
    elif salary <= 500000:
        return (salary - 250000) * 0.05
    elif salary <= 1000000:
        return (250000) * 0.05 + (salary - 500000) * 0.20
    else:
        return (250000) * 0.05 + (500000) * 0.20 + (salary - 1000000) * 0.30

try:
    salary = float(input("Enter the salary of the employee: ₹"))

    tax = calculate_tax(salary)

    print(f"The income tax to be paid by the employee is: ₹{tax}")
except ValueError:
    print("Invalid input! Please enter a valid numerical value for the salary.")
