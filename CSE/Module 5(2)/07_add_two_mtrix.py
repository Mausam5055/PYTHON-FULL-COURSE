n = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
list3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

num = 0
temp_num1 = num
temp_num2 = num + 2

# Input for n
for i in range(len(n)):
    for j in range(len(n[i])):
        n[i][j] = temp_num1
        temp_num1 += 1  

print("Matrix n:")
for row in n:
    print(row)

# Input for m
for i in range(len(m)):
    for j in range(len(m[i])):
        m[i][j] = temp_num2 
        temp_num2 += 2  

print("\nMatrix m:")
for row in m:
    print(row)

# Adding two matrices
for i in range(3):
    for j in range(3):
        list3[i][j] = n[i][j] + m[i][j]

print("\nSum of matrices:")
for row in list3:
    print(row)
