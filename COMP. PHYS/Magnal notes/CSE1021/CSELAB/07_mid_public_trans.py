
age = int(input("Enter the age : "))
time = int(input("Enter the time in 24hr format : "))

if (0<= time <24):     # Or you can use if(time>=0 and time<24)
    if (age<12):
        fare = 2
        per = "Children"
    elif (age>=12 and age<60):
        fare = 3
        per = "Adult"
    elif (age>=60):
        fare = 5 
        per = "Senior Citizen"
    if (time>9) and (time<17):
        fare = fare/2
    print(f"The fare for {per} is ${fare}")      
else:
    print("INVALID TIME!!")