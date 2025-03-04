a = int(input("Enter the side A :"))
b = int(input("Enter the side B :"))
c = int(input("Enter the side C :"))

if (a+b)<=c :
    print("Cannot form a triangle")
elif (a+c)<=b :
    print("Cannot form a triangle")
elif (b+c)<=a :
    print("Cannot form a triangle")
else :
    print("The entered values are valid sides of a triangle")