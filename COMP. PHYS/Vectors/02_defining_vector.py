# Vectors can be defined using lists, tuples, or NumPy arrays. 
# Using NumPy is preferable for mathematical operations due to
#  its efficiency and built-in functionality.

import numpy as np # Import the NumPy library for
                   #numerical operations
# Define vectors A and B using NumPy arrays
# Each vector is represented as a 1 - dimensional array of 
# components
A = np . array ([1 , 2 , 3]) # Vector A with components A_x =1 ,A_y =2 , A_z =3
B = np . array ([4 , 5 , 6]) # Vector B with components B_x =4 B_y =5 , B_z =6
# Print the defined vectors to the console
print (" Vector A:", A ) # Output : Vector A: [1 2 3]
print (" Vector B:", B ) # Output : Vector B: [4 5 6]