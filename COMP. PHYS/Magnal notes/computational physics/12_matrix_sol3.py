import numpy as np

A = np.array([[4,10,30], [10,30,100], [30,100,354]])
B = np.array([[62],[190],[644]])

print("The matrix A is : ", A)
print("The matrix B is : ", B)

det_A = np.linalg.det(A)

if det_A == 0 :
    print("The matrix is singular,so you have to use Gauss Jordan method ")
else :
    print("The matrix is not singular and you can solve by matrix method")

    print("Determinant of A is :", det_A)

inv_A = np.linalg.inv(A)

X = np.dot(inv_A, B)

print("The solve of the matrix is : ", X)