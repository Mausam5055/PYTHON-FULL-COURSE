                    # SUBMITTED BY: Mausam Kar 
                    # REG NO: 24BAI10284
                    # DATE: 13-03-2024


# Assignment questions.
# Q.1. Write a program to perform addition of two matrices.
# a=[[1,2,3],[4,5,6],[7,8,9]] b=[[4,5,6],[7,8,9],[1,2,3]]
# Q.2. Write a Program to define a list of countries as BRICS member and check
# whether given country is a member or not.
# Q.3. Write a program that asks the user to enter a list of integers. Do the
# following:
# (a) Print the total number of items in the list.
# (b) Print the last item in the list.
# (c) Print the list in reverse order.
# (d) Print Yes if the list contains a 5 and No otherwise.
# (e) Print the number of fives in the list.
# (f) Remove the first and last items from the list, sort the remaining items,
# and print the result.
# (g) Print how many integers in the list are less than 5.
# (h) Print the average of the elements in the list.
# (i) Print the largest and smallest values in the list.
# (j) Print the second largest and second smallest entries in the list
# (k) Print how many even numbers are in the list.

#Solution:

# -------------------------------------------
# Q1. Program to perform addition of two matrices
# -------------------------------------------

# Given matrices
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = [[4, 5, 6],
     [7, 8, 9],
     [1, 2, 3]]

# Empty matrix to store result
c = []

# Loop through rows
for i in range(len(a)):
    row = []  # create a new row
    # Loop through columns
    for j in range(len(a[0])):
        row.append(a[i][j] + b[i][j])  # add corresponding elements
    c.append(row)

# Print result
print("Resultant Matrix after addition:")
for r in c:
    print(r)


# -------------------------------------------
# Q2. Program to check if a country is a BRICS member
# -------------------------------------------

# List of BRICS countries
brics = ["Brazil", "Russia", "India", "China", "South Africa"]

# Take input from user
country = input("\nEnter a country name: ")

# Check if country is in list
if country in brics:
    print(country, "is a BRICS member.")
else:
    print(country, "is NOT a BRICS member.")


# -------------------------------------------
# Q3. Program to perform various operations on a list of integers
# -------------------------------------------

# Take list input from user
nums = list(map(int, input("\nEnter integers separated by spaces: ").split()))

# (a) Print total number of items
print("\n(a) Total numbers in the list:", len(nums))

# (b) Print the last item
print("(b) Last item in the list:", nums[-1])

# (c) Print the list in reverse order
print("(c) List in reverse order:", nums[::-1])

# (d) Print Yes if the list contains 5, otherwise No
if 5 in nums:
    print("(d) Yes, list contains 5")
else:
    print("(d) No, list does not contain 5")

# (e) Print number of 5s in the list
print("(e) Number of 5s in the list:", nums.count(5))

# (f) Remove first and last items, sort the rest, and print
if len(nums) > 2:
    new_list = nums[1:-1]   # remove first and last
    new_list.sort()         # sort the remaining items
    print("(f) After removing first & last, sorted list:", new_list)
else:
    print("(f) List too small to remove first and last")

# (g) Print how many integers are less than 5
count_less_5 = len([x for x in nums if x < 5])
print("(g) Numbers less than 5:", count_less_5)

# (h) Print average of elements
avg = sum(nums) / len(nums)
print("(h) Average of numbers:", avg)

# (i) Print largest and smallest values
print("(i) Largest number:", max(nums))
print("(i) Smallest number:", min(nums))

# (j) Print second largest and second smallest entries
unique_nums = sorted(list(set(nums)))  # remove duplicates
if len(unique_nums) >= 2:
    print("(j) Second largest:", unique_nums[-2])
    print("(j) Second smallest:", unique_nums[1])
else:
    print("(j) Not enough unique numbers for second largest/smallest")

# (k) Print how many even numbers are in the list
even_count = len([x for x in nums if x % 2 == 0])
print("(k) Count of even numbers:", even_count)

