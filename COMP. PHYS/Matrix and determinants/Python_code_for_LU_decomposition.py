from scipy.linalg import lu
import numpy as np 
A = np.array([[1, 2,3] ,[4,5,6],[7,8,9]])
P, L, U = lu(A)
print("permutation_matrix:\n",P)        #print("permutation_matrix:")
                                        #print(P)

print("L(Lower Triangual Matrix):\n",L)
print("U(Upper Triangual Matrix):\n",U)
det_A = np.linalg.det(A)  #linalg = "linear algebra"
