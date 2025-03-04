def find_hcf(a, b):
    while b != 0:
        a, b = b, a % b
    print("The HCF of two numbers is : ", a)

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

find_hcf(a,b)
