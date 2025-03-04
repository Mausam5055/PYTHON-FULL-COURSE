import numpy as np
# Define two vectors
A = np . array ([1 , 2 , 3])
B = np . array ([4 , 5 , 6])
# Vector Addition
addition = A + B
print (" Addition :", addition )
# Vector Subtraction
subtraction = A - B
print (" Subtraction :", subtraction )
# Dot Product
dot_product = np . dot (A , B )
print ("Dot Product :", dot_product )
# Cross Product
cross_product = np . cross (A , B )
print (" Cross Product :", cross_product )
# Scalar Multiplication
scalar_multiplication = 2 * A
print (" Scalar Multiplication :", scalar_multiplication )
# Magnitude of a vector
magnitude_A = np . linalg . norm ( A )
print (" Magnitude of A:", magnitude_A )