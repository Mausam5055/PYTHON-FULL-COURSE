import numpy as np
# Example matrices
A = np . array ([[1 , 2 , 3] ,
[4 , 5 , 6] ,
[7 , 8 , 9]])
B = np . array ([[7 , 8] ,
[10 , 11] ,
[12 , 13]])

# Ensure A and B are compatible for addition
C = A [: , :2] + B # Slicing A to ensure it has the same
                   #shape as B for element - wise addition
# Matrix multiplication
D = np . dot (A , B ) # Performing matrix multiplication using
np.dot