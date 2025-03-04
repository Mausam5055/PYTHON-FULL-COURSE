# import math

# # Input from user
# lower = int(input("Enter lower limit: "))
# upper = int(input("Enter upper limit: "))

# # Loop through each number in the range
# for num in range(lower, upper + 1):
#     if num > 1:  # Check if the number is greater than 1
#         is_prime = True
#         for i in range(2, int(math.sqrt(num)) + 1):  # Check for factors
#             if num % i == 0:
#                 is_prime = False
#                 break  # Break if a factor is found
#         if is_prime:
#             print(num, end=" ")  # Print the prime number








def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    # Print the triangle
    for row in triangle:
        print(" ".join(map(str, row)))

# Input from user
n = int(input("Enter the number of rows: "))
generate_pascals_triangle(n)
