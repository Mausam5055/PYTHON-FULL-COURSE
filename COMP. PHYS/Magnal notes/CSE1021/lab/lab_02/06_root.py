import math as m 
a = float(input("Enter the coefficient of x^2 : "))
b = float(input("Enter the coefficient of x : "))
c = float(input("Enter the constant term : "))

d = pow(b,2) - 4*a*c
root_1 = (-b + m.sqrt(d))/(2*a)
root_2 = (-b - m.sqrt(d))/(2*a)

if d < 0 :
    print("No real Roots")
elif d > 0 :
    print("Roots are equal and they are : ", root_1,"and", root_2)
else :
    print("Roots are real and unequal and they are : ", root_1, "and", root_2) 