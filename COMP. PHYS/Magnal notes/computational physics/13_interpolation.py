

x1 = int(input("Enter x1 :"))
x2 = int(input("Enter x2 :"))
y1 = int(input("Enter y1 :"))
y2 = int(input("Enter y2 :"))
x = int(input("Enter x :"))


y = y2+((y2-y1)/(x2-x1))*(x-x2)

print(f"The y co-ordinate of the point is: {y:.2f}")