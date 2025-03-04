#write  a python code to print the following pattern:
#   1
#   2 3
#   4 5 6
#   7 8 9 10
#HINT: this can be done by nested loops
row = 4  # Number of rows
num = 1  # Initialize counter

for i in range(1, row + 1):  # Outer loop for rows
    for j in range(i):  # Inner loop for columns
        print(num, end=" ")  # Print the current number
        num = num + 1
                     # Increment the counter
    print()  # Move to the next line after printing a row


# We initialize the counter (num = 1) because we need to maintain 
# a continuous sequence of numbers across all rows.

# Why Initialize num = 1?
# In normal nested loops (like the previous pattern), we print the 
# row number repeatedly. However, in this case, each row should 
# continue from the last number printed in the previous row.

# How the counter works:
# 1.Starts with num = 1 before the loops begin.
# 2.Each time we print num, we increment it (num += 1).
# 3.Since the counter is global across all rows, it ensures that the
# next row starts with the new incremented number.

# Breakdown of Execution:
# First iteration (i = 1)
#         Prints 1
#         num becomes 2

# Second iteration (i = 2)
#         Prints 2 3
#         num becomes 4

# Third iteration (i = 3)
#         Prints 4 5 6
#         num becomes 7

# Fourth iteration (i = 4)
#         Prints 7 8 9 10
#         num becomes 11, but we stop since the pattern is complete.

