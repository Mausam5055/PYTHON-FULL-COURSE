import numpy as np

A = np.array([[1,1,-1],[3,-2,1],[1,3,-2]])
B = np.array([[6],[-5],[14]])

inv_A = np.linalg.inv(A)

X = np.dot(inv_A,B)

print("The solution of the matrix is : \n", X)