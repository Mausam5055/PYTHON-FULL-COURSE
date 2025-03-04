import numpy as np

A = [1,0,0]
B = [0,1,0]
C = [0,0,1]

cross = np.cross(A,B)
vol = np.dot(cross,C)

print("The volume of parallelogram is : ", vol)