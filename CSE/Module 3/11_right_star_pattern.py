# write  a python code to print the following pattern:

            # *
            # * *
            # * * *
            # * * * *          

        
row = 4  # Number of rows

for i in range(1, row + 1):  # Outer loop for rows
    for j in range(i):       # Inner loop for columns
        print("*", end=" ")  # Print a star
    print()                  # Move to the next line after printing a row
