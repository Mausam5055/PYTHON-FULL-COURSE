#Linear Search in an Array

from array import *
array1 = array('i', [10, 20,40, 30, 40,50,60])
n = int(input("Enter the number to search: "))
from array import *

array1 = array('i', [10, 20, 40, 30, 40, 50, 60])
n = int(input("Enter the number to search: "))
for i in range(len(array1)):
    if array1[i] == n:
        print("Number exists in the array")
        break
else:
    print("Number does not exist in the array")
