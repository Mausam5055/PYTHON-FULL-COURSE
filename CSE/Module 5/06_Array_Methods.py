# Difference Between remove() and pop() in Python Arrays
# In the array module, you can remove elements using two methods:

#1. remove(value) → Deletes the first occurrence of the specified value.
#2. pop(index) → Deletes the element at the given index 
# (default: last element).
#3.The del statement in Python can be used to delete elements from an array 
# by index or delete the entire array.

# 1. remove(value) – Removes a Specific Value
# Removes only the first occurrence of the given value.
# If the value is not found, it raises an error.

import array
arr = array.array('i', [10, 20, 30, 20, 40])
arr.remove(20)  # Removes the first 20
print(arr)  # Output: array('i', [10, 30, 20, 40])

# 2. pop(index) – Removes an Element at a Specific Index
# If no index is given, it removes the last element.
# If the index is out of range, it raises an error.

arr.pop(1)  # Removes element at index 1 (30)
print(arr)  # Output: array('i', [10, 20, 40])
arr.pop()  # Removes last element (40)
print(arr)  # Output: array('i', [10, 20])


# 1. Deleting an Element by Index
# You can remove a specific element from an array using its index.
# Example:
import array
arr = array.array('i', [10, 20, 30, 40, 50])
del arr[2]  # Deletes element at index 2 (30)
print(arr)  # Output: array('i', [10, 20, 40, 50])
del arr[10]  # IndexError: array assignment index out of range

