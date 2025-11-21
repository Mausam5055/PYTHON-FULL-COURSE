#Write a program to find factorial of a number

n = int(input("Enter The Number:"))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("The factorial of", n, "is", factorial)


num = int(input("Enter a number: "))

# 0 and 1 are not prime numbers
if num <= 1:
    print(num, "is not a prime number")
else:
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

#Write a program to print multiplication table of a number using for loop
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    i = i + 1

    
#Write a program to print all th even numbers in range 1 to n (n
#value taken from user)
n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)