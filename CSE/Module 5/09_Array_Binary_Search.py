# Binary Search in an array: Iteration Method

from array import *
array1 = array('i', [10, 23, 35, 56, 82, 100])
n = int(input("Enter the number to search: "))
min = 0
max = len(array1) - 1

def binary_search(array, n, min, max):
    while min <= max:
        mid = (min + max) // 2
        if array[mid] == n:
            print("Number Exists In the Index", mid)
            return
        if n > array[mid]:
            min = mid + 1
        else:
            max = mid - 1

    print("Number does not exist in the array")

# Call the binary search function
binary_search(array1, n, min, max)

# In Binary Search, you search between the min and max indexes. 
# You keep narrowing down the range.
# ✅ If min <= max, there is still something left to search.