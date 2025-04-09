def binary_search(array, min, max, n):
    while min <= max:
        mid = (min + max) // 2
        if array[mid] == n:
            print("The number exists at index", mid)
            return
        elif n < array[mid]:  # ✅ Fix: compare with array[mid]
            max = mid - 1
        else:
            min = mid + 1
    print("Number doesn't exist in the array")

# Main Program
import array
n = int(input("Enter the number to search: "))
array1 = [20, 30, 40, 56, 78, 90]
min = 0
max = len(array1) - 1

binary_search(array1, min, max, n)


       
