# Write a program to generate electricity bill amount based on the following
# constraints:
#For <100units - Rs. 1.60/unit
#For 100-200 units - Rs. 2.35/unit
#For 200-300 units - Rs. 3.40/unit
#For >400 units - Rs. 5.25/unit

units = float(input("Enter the number of electricity units consumed: "))
if units < 100:
    bill = units * 1.60
elif units <= 200:
    bill = units * 2.35
elif units <= 300:
    bill = units * 3.40
else:
    bill = units * 5.25
print("The electricity bill amount is: Rs.", bill)  
