# The array module in Python provides a way to store a 
# collection of elements in a memory-efficient way. Think 
# of it as a list, but with a few key differences.

#          array.array(typecode, [elements]): 

# 1.typecode: A single character that defines the type of elements 
# in the array.
# 2.elements: A list or tuple of values that match the specified 
# type.



import array
numbers = array.array('i', [10, 20, 30, 40])  # 'i' means integer type
print(numbers)  # Output: array('i', [10, 20, 30, 40])

# Why Use an Array Instead of a List?

# 1.Takes Less Memory: Since all elements are of the same 
# type, arrays use less space.

# 2.Faster Access: Arrays store data more efficiently, making 
# operations like searching and modifying elements faster.

# ✅ Use lists when you need mixed data types.
# ✅ Use arrays when working with large numbers of the same 
# type (e.g., all integers or all floats) for better 
# performance.