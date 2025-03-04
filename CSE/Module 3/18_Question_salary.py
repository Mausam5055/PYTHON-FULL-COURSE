# write an algorithm to calculate the salary of an employee from the user to input
# basic salary. Calculate HRA 18% of basic salary, DA 45% of the basic salary and
# deduct 10% of the gross salary as a tax

def calculate_salary():
    # Get user input for basic salary
    basic_salary = float(input("Enter the basic salary: "))

    # Calculate HRA, DA
    hra = 0.18 * basic_salary
    da = 0.45 * basic_salary

    # Calculate Gross Salary
    gross_salary = basic_salary + hra + da

    # Calculate Tax Deduction
    tax = 0.10 * gross_salary

    # Calculate Net Salary
    net_salary = gross_salary - tax

    # Display the results in a simple way
    print("\nSalary Breakdown:")
    print("Basic Salary:", basic_salary)
    print("HRA:", hra)
    print("DA:", da)
    print("Gross Salary:", gross_salary)
    print("Tax Deduction:", tax)
    print("Net Salary:", net_salary)

# Call the function
calculate_salary()


# Enter the basic salary: 50000

# Salary Breakdown:
# Basic Salary: 50000.0
# HRA: 9000.0
# DA: 22500.0
# Gross Salary: 81500.0
# Tax Deduction: 8150.0
# Net Salary: 73350.0

