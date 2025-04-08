n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Adding two matrices
for i in range(len(n)):
    for j in range(len(n[i])):  
        list3[i][j] = n[i][j] + m[i][j]

# Printing the result
for i in range(len(list3)):
    for j in range(len(list3[i])):  
        print(list3[i][j], end=" ")
    print()

# We’re looping over the structure of matrix n, but we are still 
# accessing both n[i][j] and m[i][j] — so even though the loop runs 
# based on n, the operation applies to both since both have same size