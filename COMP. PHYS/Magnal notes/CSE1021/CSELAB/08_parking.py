
v_type = int(input("Enter the number for your vehicle \n 1.car \n 2.motocycle \n3.truck: \n"))
hrs = int(input(f"Enter the hours your vehicle was parked for  : "))

if v_type == 1 :
    fare = 2*hrs
elif v_type == 2 :
    fare = 1.5*hrs
elif v_type == 31 :
    fare = 3*hrs
if hrs>8:
    fare = (fare - (0.1*fare))

print(f"The fare for your vehicle for {hrs} hours is ${fare}")
