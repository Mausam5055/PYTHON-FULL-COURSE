# Reversing an array using different methods

import array

# Method 1: Using list reverse()
new_arr = [1, 2, 3, 4, 5]
new_arr.reverse()  # Call reverse() on the list directly
print("Reversed array (Method 1):", new_arr)

# Method 2: Using array and reversed()
arr = array.array('i', [1, 2, 3, 4, 5])
res_arr = array.array('i', reversed(arr))
print("Reversed array (Method 2):", res_arr)

# Method 3: Using NumPy
import numpy as np
np_arr = np.array([1, 2, 3, 4, 5])
reversed_arr = np.flip(np_arr)  # Use np.flip() with array argument
print("Reversed array (Method 3):", reversed_arr)

# Method 4: Using NumPy flipud()
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
res_arr = np.flipud(arr)  # Use arr instead of new_arr
print("Reversed array (Method 4):", res_arr)