#An array in Python is a data structure that stores multiple
#values of the same type in a single variable. Arrays are
#useful when you need to work with a collection of 
# elements efficiently.

# Python does not have a built-in array type like C or 
# Java, but we can use:

#1. Lists (built-in, flexible, can store different data types)
#2. array Module (stores only the same data type)
#3. NumPy Arrays (faster and better for large data)

#Creating an array:

#1. Using Lists:
#You can create an array using a list of values enclosed in
#square brackets []. Here is an example of an array of

#Example: Create an array of integers using a list.
#Array of integers
integers = [1, 2, 3, 4, 5]
print(integers)

#Example: Create an array of strings using a list.
#Array of strings
names = ["Alice", "Bob", "Charlie"]
print(names)

#Example: Create an array of mixed data types using a list.
#Array of mixed data types:
mixed = [1, "Alice", 3.5, True]
print(mixed)


#Array Indexing:

numbers = [10, 20, 30, 40, 50]

print(numbers[0])  # First element (10)
print(numbers[2])  # Third element (30)
print(numbers[-1])  # Last element (50)
print(numbers[-2])  # Second last element (40)
