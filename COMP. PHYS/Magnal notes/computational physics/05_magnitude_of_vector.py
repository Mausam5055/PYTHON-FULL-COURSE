
import math

A =  [1,1,1]

sum = 0

for component in A:
    sum += component**2


mag = math.sqrt(sum)

print("Mangnitude of Vector is ", mag)


import numpy as np
import math as m

A = [2,3,5,4]
B = [8,5,9,1]

res = np.add(A,B)

print("The resultant vectors is : ",res)
print("The magnitude of resultant vector is : ", )