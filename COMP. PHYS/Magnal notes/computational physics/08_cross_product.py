import math

A = [1,2,3]
B = [3,4,5]

x = A[1]*B[2] - B[1]*A[2]
y = A[2]*B[0] - B[2]*A[0]
z = A[0]*B[1] - B[0]*A[1]

cross_product = (x,y,z)

print("The cross product is :", cross_product)