import math

def vector_magnitude(vector):
    sum_of_squares = 0
    
    # Loop through each component of the vector
    for component in vector:
        sum_of_squares += component ** 2
    
    # Compute the square root of the sum of squares
    magnitude = math.sqrt(sum_of_squares)
    
    return magnitude

# Example usage
vector = [3, 4, 12]  # You can change this to any vector you want
magnitude = vector_magnitude(vector)
print("Magnitude of the vector:", magnitude)
