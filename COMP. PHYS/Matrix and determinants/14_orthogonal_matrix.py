import numpy as np
# Creating an Orthogonal Matrix
orthogonal_matrix = np . array ([[1/ np . sqrt (2) , 1/ np . sqrt (2) ] ,
[ -1/ np . sqrt (2) , 1/ np . sqrt (2) ]])
# Check orthogonality by verifying A^T * A = I
orthogonality_check = np . allclose ( np . dot ( orthogonal_matrix .T
, orthogonal_matrix ) , np . eye (2) )
print (" Orthogonal Matrix :\n", orthogonal_matrix )
print ("Is the matrix orthogonal ?", orthogonality_check )