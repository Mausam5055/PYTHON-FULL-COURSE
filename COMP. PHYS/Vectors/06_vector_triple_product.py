import numpy as np
# Define three vectors
A = np . array ([1 , 2 , 3])
B = np . array ([4 , 5 , 6])
C = np . array ([7 , 8 , 9])
# Vector Triple Product : A x (B x C)
# First compute the cross product B x C
cross_product_BC = np . cross (B , C )
# Then compute A x (B x C)
vector_triple_product = np . cross (A , cross_product_BC )
# Scalar Triple Product : A . (B x C)
scalar_triple_product = np . dot (A , cross_product_BC )
print (" Vector Triple Product (A x (B x C)):",
vector_triple_product )
print (" Scalar Triple Product (A . (B x C)):",
scalar_triple_product )