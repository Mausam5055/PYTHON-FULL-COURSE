# 4. Function With Parameters and With Return Value
# This function takes inputs and returns a value after 
# processing.

# Eg: 1:
def add(a, b):
    return a + b  # Returns the sum of 'a' and 'b'

result = add(5, 3)  # Calls the function with 5 and 3
print(result)  # Prints the sum



#Example 2: 
def check_odd_even(a):  # Takes the number as a parameter
    if a % 2 == 0:
        return "Even"  # Returns "Even" if the number is even
    else:
        return "Odd"  # Returns "Odd" if the number is odd

# Taking input from the user and calling the function
a = int(input("Enter a number: "))
print(check_odd_even(a))  # Prints the result (print = return vlue )


