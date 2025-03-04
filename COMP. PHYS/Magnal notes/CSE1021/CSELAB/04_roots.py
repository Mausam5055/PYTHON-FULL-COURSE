
a = int(input("Enter coefficient a : "))
b = int(input("Enter coefficient b : "))
c = int(input("Enter coefficient c : "))
d = b**2-4*a*c
if d<0 :
    print("The roots are not real")
else :
    r1 = (-b+d**(0.5))/(2*a)
    r2 = (-b-d**(0.5))/(2*a)
    print("The first root is : ", r1)
    print("The second root is : ", r2)