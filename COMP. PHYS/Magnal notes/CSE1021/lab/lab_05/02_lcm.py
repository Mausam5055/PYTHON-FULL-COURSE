import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = abs(num2*num1)/math.gcd(num1,num2)

print("The LCM of two numbers is : ",lcm)