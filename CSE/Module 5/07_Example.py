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

for i in range(len(array1)):
    is_unique = True
    for j in range(len(array1)):
        if i != j and array1[i] == array1[j]:  # Compare values at different positions
            is_unique = False
            break
    if is_unique:
        print(array1[i])

