import numpy as np
# Define two vectors
A = np . array ([1 , 2 , 3])
B = np . array ([4 , 5 , 6])
# Calculate dot product
dot_product = np . dot (A , B )
# Calculate magnitudes of the vectors
magnitude_A = np . linalg . norm ( A )
magnitude_B = np . linalg . norm ( B )
# Calculate the cosine of the angle
cos_theta = dot_product / ( magnitude_A * magnitude_B )
# Calculate the angle in radians
angle_radians = np . arccos ( cos_theta )
# Convert the angle to degrees ( optional )
angle_degrees = np . degrees ( angle_radians )
print ("Dot Product :", dot_product )
print (" Magnitude of A:", magnitude_A )
print (" Magnitude of B:", magnitude_B )
print (" Cosine of the angle :", cos_theta )
print (" Angle in radians :", angle_radians )
print (" Angle in degrees :", angle_degrees )
