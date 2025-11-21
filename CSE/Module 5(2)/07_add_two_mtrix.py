# Create empty 3x3 matrices
n = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
list3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Input for matrix n
print("Enter numbers for Matrix n:")
for i in range(3):
    for j in range(3):
        n[i][j] = int(input(f"Enter number for n[{i+1}][{j+1}]: "))

# Input for matrix m
print("\nEnter numbers for Matrix m:")
for i in range(3):
    for j in range(3):
        m[i][j] = int(input(f"Enter number for m[{i+1}][{j+1}]: "))

# Add the two matrices
for i in range(3):
    for j in range(3):
        list3[i][j] = n[i][j] + m[i][j]

# Show the results
print("\nMatrix n:")
for k in n:
    print(k)

print("\nMatrix m:")
for l in m:
    print(l)

print("\nSum of both matrices:")
for o in list3:
    print(o)






# n = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# list3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# num = 0
# temp_num1 = num
# temp_num2 = num + 2

# # Input for n
# for i in range(len(n)):
#     for j in range(len(n[i])):
#         n[i][j] = temp_num1
#         temp_num1 += 1  

# print("Matrix n:")
# for row in n:
#     print(row)

# # Input for m
# for i in range(len(m)):
#     for j in range(len(m[i])):
#         m[i][j] = temp_num2 
#         temp_num2 += 2  

# print("\nMatrix m:")
# for row in m:
#     print(row)

# # Adding two matrices
# for i in range(3):
#     for j in range(3):
#         list3[i][j] = n[i][j] + m[i][j]

# print("\nSum of matrices:")
# for row in list3:
#     print(row)
