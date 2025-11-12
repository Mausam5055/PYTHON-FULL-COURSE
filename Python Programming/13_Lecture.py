# 1. Create an empty list to hold our numbers
odd_numbers = []

# 2. Loop through all numbers from 1 to 100
#    range(1, 101) gives us 1, 2, 3, ..., 100
for i in range(1, 101):
    
    # 3. Check if the number 'i' is odd
    #    The % (modulo) operator gives the remainder of a division.
    #    If i % 2 is not 0, the number is odd.
    if i % 2 != 0:
        
        # 4. If the number is odd, add it to our list
        odd_numbers.append(i)

# 5. Finally, print the entire list of odd numbers
print("The list of odd numbers:")
print(odd_numbers)
