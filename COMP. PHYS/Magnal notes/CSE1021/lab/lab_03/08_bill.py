def calculate_electricity_bill(units):
    if units <= 150:
        bill = units * 5

    elif 151 <= units <= 350:
        bill = 100 + (units - 150) * 5.75

    elif 351 <= units <= 450:
        bill = 250 + (units - 350) * 6

    elif 451 <= units <= 600:
        bill = 300 + (units - 450) * 6.25

    else:
        bill = 400 + (units - 600) * 7

    return bill

units = float(input("Enter the number of units consumed: "))
bill_amount = calculate_electricity_bill(units)
print(f"The total electricity bill for {units} units is Rs. {bill_amount:.2f}")
