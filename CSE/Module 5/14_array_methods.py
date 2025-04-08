#splitting in 3 parts of array (M-1)
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
splitedarray = np.array_split(arr, 3)

print(splitedarray)
print(splitedarray[0])
print(splitedarray[1])
print(splitedarray[2])

# Output:
# [array([1, 2]), array([3, 4]), array([5, 6])]
# [1, 2]
# [3, 4]
# [5, 6]

#splitting in 3 parts of array (M-2)
import numpy as np
# input array
in_arr = np.array([ 2, 0, 1, 5, 4, 9])
print ("Input array : ", in_arr)
out_arr = np.partition(in_arr, 3)
print ("Output partitioned array : ", out_arr)