# 3. Function Without Parameters but With Return Value
# This function does not take inputs, but it returns a value after 
# processing.

# No parameters → The function does not take any input.
# With return value → The function returns a result instead of just
# printing it.

def greeting():
    return "Hello, have a great day!"  # Returns a message

print(greeting())  # Calls the function and prints the result


#Example 2: 
def check_odd_even():
    if a % 2 == 0:
        return "Even"  # Returns "Even" if the number is even
    else:
        return "Odd"  # Returns "Odd" if the number is odd

a = int(input("Enter a number: "))  # Takes input
# Calling the function and printing the result
print(check_odd_even())
