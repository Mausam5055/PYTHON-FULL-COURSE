#Linear Search in an Array

from array import *
array1 = array('i', [10, 20,40, 30, 40,50,60])
n = int(input("Enter the number to search: "))
for x in array1:
    if(x==n):
        print("Number Exists In the Array")
        break

else:
    print("Number does not exist in the array")
# Output: Enter the number to search: 40