# Print all the unique elements from the given array

from array import array

# Create the array
array2 = array('i', [10, 20, 30, 20, 40, 50, 60, 40])

# Method 1: Using count() method
print("Unique elements:")
for x in array2:
    if array2.count(x) == 1:
        print(x)

#M-2: 
import array

array1 = array.array('i', [10, 20, 30, 20, 40, 50, 60, 40])

for x in array1:  
    is_unique = True  # Assume x is unique
    
    for y in array1:  
        if x == y and array1.index(x) != array1.index(y):  # Check for duplicates at different positions
            is_unique = False
            break  

    if is_unique:
        print(x)
