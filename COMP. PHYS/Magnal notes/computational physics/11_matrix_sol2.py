import numpy as np

A = np.array([[1,3,-2], [2,1,4], [6,1,-3]])
B = np.array([[5], [8], [5]])


print("Matrix A is:", A)
print("Matrix B is:", B)

det_A = np.linalg.det(A)
print("Determinant of A is :", det_A)

inv_A = np.linalg.inv(A)

X = np.dot(inv_A, B)

print("The solve of the matrix is : ", X)