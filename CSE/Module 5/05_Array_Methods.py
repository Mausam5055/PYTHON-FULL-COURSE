#Append :inserts the data in the array at the end
#insert: inserts the data in the array at the specified position
#Example: Append and Insert Data in an Array



import array
array1 = array.array('i', [10, 20, 30, 40])
print("Original Array:", array1)

#Insert Data
array1.insert(1,60) #inserts 60 at index 1
print("Array after inserting 60 at index 1:", array1)
#Output: Original Array: array('i', [10, 20, 30, 40])
#Array after inserting 60 at index 1: array('i', [10, 60, 20, 30, 40])

#Append Data
array1.append(50) #appends 50 at the end
print("Array after appending 50:", array1)
#output: Array after appending 50: array('i', [10, 60, 20, 30, 40, 50])