# Check If a number is even or odd
n = int(input("Enter a number: "))
if (n % 2) == 0:
    print(n, "is Even")
else:
    print(n, "is Odd")



# which of the three numbers is the largest
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2   
else:
   largest = num3
print("The largest number is", largest)



#chcek if a given character is a vowel or not using if else:
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print(char, "is a Vowel")
else:
    print(char, "is not a Vowel")



#Find Smallest of Two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if (num1 <= num2):
    smallest = num1
else:
    smallest = num2
print("The smallest number is", smallest)


#write a proram to take age of a person and determine whether they are eligible to vote or not
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")