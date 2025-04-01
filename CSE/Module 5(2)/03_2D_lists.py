# Creating a 2D list (list of lists)
list2d = [
    [1, 2, 3],
    [4, 5, 6]
]

# First loop: Printing each row of the 2D list
for i in range(2):  # Loop through the two rows
    print(list2d[i])  # Prints the entire row (sub-list)

# Second loop: Accessing and printing each element individually
for i in range(2):  # Loop through rows
    for j in range(3):  # Loop through columns (each row has 3 elements)
        print(list2d[i][j])  # Prints each element separately on a new line

# Third loop: Printing each row's elements in the same line
for i in range(2):  # Loop through rows
    for j in range(3):  # Loop through columns
        print(list2d[i][j], end="")  # Prints elements in the same line without spaces
    print()  # Moves to the next line after printing a row
