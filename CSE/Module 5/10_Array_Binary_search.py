#BInary Search In Array: Recursive Method

from array import *

def binary(array1, n, min, max):
    if min > max:  
        print("Number not found in array")
        return

    mid = (min + max) // 2

    if array1[mid] == n:
        print("Number found at index", mid)
        return  

    elif n > array1[mid]:
        return binary(array1, n, mid + 1, max)  

    else:
        return binary(array1, n, min, mid - 1)  


array1 = array('i', [10, 20, 23, 35, 56, 82, 100])
n = int(input("Enter a number to be searched in array: "))

min = 0
max = len(array1) - 1  

binary(array1,n,min,max)