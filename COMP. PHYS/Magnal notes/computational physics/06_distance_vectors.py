import math as m
import numpy as np

A = [1,1,1]
B = [3,3,3]

dist_vector = np.subtract(B,A)

print("Distance : ", dist_vector)


# Another way to calculate using loop
# S = [0,0,0]

# for i in range(len(A)):
#     S[i] = B[i] - A[i]

# print(S)


