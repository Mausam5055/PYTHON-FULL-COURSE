import numpy as np
# Creating smaller matrices for block construction
A = np . array ([[1 , 2] , [3 , 4]])
B = np . array ([[5 , 6] , [7 , 8]])
C = np . array ([[9 , 10] , [11 , 12]])
D = np . array ([[13 , 14] , [15 , 16]])
# Combining them into a block matrix
block_matrix = np . block ([[ A , B ] , [C , D ]])
print (" Block Matrix :\n", block_matrix )