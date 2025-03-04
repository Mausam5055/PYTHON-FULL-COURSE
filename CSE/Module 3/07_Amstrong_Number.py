#Check Amstrong Number By taking user input :

#the number whose cube of each term and the sum 
#the cubed term gives the number itself is called
#amstrong Number :
#Example: 153 = 1^3 + 5^3 + 3^3

# Method 1 : using normal :
n = int(input("Enter The Number: "))

# Extract individual digits
d1 = n % 10
d2 = (n // 10) % 10
d3 = (n // 100) % 10

# Calculate the sum of cubes of digits
s = (d1 ** 3) + (d2 ** 3) + (d3 ** 3)

# Check if the sum is equal to the original number
if s == n:
    print("The Number Is Armstrong")
else:
    print("The Number Is Not Armstrong")

#Method 3 : using while Loop

n = int(input("Enter The Number: "))
i = n  # Store original number in i
s = 0  # Initialize sum

while n > 0:
    d = n % 10  # Get last digit
    s = s + d ** 3  # Cube the digit and add to sum
    n = n // 10  # Remove last digit and the loop continues with this number

# Check if the sum is equal to the original number
if s == i:
    print("The Number Is Armstrong")
else:
    print("The Number Is Not Armstrong")


#Notes: 
# 1.In Python, // is the floor division operator. It divides two 
# numbers and rounds the result down to the nearest whole number 
# (integer).

# Example:

# print(10 // 3)   # Output: 3
# print(10.5 // 3) # Output: 3.0
# print(-10 // 3)  # Output: -4
# 
# 

# 2. No, // in Python does not remove the last digit; it performs 
# floor division, meaning it divides two numbers and rounds the result
#  down to the nearest integer.

# If you're looking to remove the last digit of a number, you can use 
# integer division by 10, like this:

# Removing the Last Digit from an Integer

#         num = 12345
#         new_num = num // 10  # Removes the last digit
#         print(new_num)  # Output: 1234
# This works because integer division by 10 shifts the decimal point 
# left and truncates the decimal part.

