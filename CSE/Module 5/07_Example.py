#Print all the Unique elemts from the given array:


import array

array1 = array.array('i', [10, 20, 30, 20, 40, 50, 60, 40])

for x in array1:  
    is_unique = True  # Assume x is unique
    
    for y in array1:  
        if x == y and array1.index(x) != array1.index(y):  # Check for duplicates at different positions
            is_unique = False  # Mark as not unique
            break  

    if is_unique:
        print(x)

