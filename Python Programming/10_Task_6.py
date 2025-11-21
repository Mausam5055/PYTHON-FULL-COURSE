                    # SUBMITTED BY: Mausam Kar 
                    # REG NO: 24BAI10284
                    # DATE: 13-04-2024



#  1. Factorial using Function
def fact():
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

n = int(input("Enter a number: "))
print("Factorial =", fact())


#  2. Area of Circle using Function (default pi=3.14, radius=1)
def area(r=1, pi=3.14):
    return pi * r * r

r = float(input("Enter radius: "))
print("Area of circle =", area(r))



#  3. Distance between Two Points
# Formula: √((x2−x1)² + (y2−y1)²)
def distance(x1, y1, x2, y2):
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return d

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
print("Distance =", distance(x1, y1, x2, y2))




# 4. Discriminant of Quadratic Equation
# Equation: ax² + bx + c
# Discriminant: D = b² − 4ac
def check_roots(a, b, c):
    D = b*b - 4*a*c
    if D > 0:
        print("Two Real Roots")
    elif D == 0:
        print("One Real Root")
    else:
        print("Two Complex Roots")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
check_roots(a, b, c)

