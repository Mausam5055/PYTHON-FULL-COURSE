# Normal formula
speed = int(input("Enter the speed in km/hr :"))
miles = speed/1.6
print("Speed in miles/hr using normal formula is : ", miles, "miles/hr")

# Using Function
def convt_miles(speed): 
    speed = speed/1.6
    print("Speed in miles/hr using function is : ", speed, "miles/hr")

convt_miles(speed)