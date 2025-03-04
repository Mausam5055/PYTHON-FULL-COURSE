a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

larger = max(a, b)

while True:
    if larger % a == 0 and larger % b == 0:
        lcm = larger
        break
    larger += 1

print("The LCM of two numbers is : ", lcm)