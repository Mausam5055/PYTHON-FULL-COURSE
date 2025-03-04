import numpy as np
# Define two vectors
A = np . array ([1 , 2 , 3])
B = np . array ([4 , 5 , 6])
# Calculate the cross product
cross_product = np . cross (A , B )
# Calculate the magnitudes of the vectors
magnitude_A = np . linalg . norm ( A )
magnitude_B = np . linalg . norm ( B )
# Calculate the angle using the magnitude of the cross product
magnitude_cross_product = np . linalg . norm ( cross_product )
# Calculate the sine of the angle
sin_angle = magnitude_cross_product / ( magnitude_A *
magnitude_B )
# Calculate the angle in radians and then convert to degrees
angle_radians = np . arcsin ( sin_angle )
angle_degrees = np . degrees ( angle_radians )
# Print results
print (" Cross Product (A x B):", cross_product )
print (" Angle between A and B (in radians ):", angle_radians )
print (" Angle between A and B (in degrees ):", angle_degrees )