# A sample tuple
numbers = (5, 2, 9, 1, 7)

# ✅ sorted() - returns a sorted list from the tuple (does not modify the original tuple)
sorted_list = sorted(numbers)
print("Sorted list:", sorted_list)  # [1, 2, 5, 7, 9]

# ✅ index() - finds the index of the first occurrence of a value
index_of_9 = numbers.index(9)
print("Index of 9:", index_of_9)  # 2

# ✅ Iteration - loop through each item in the tuple
print("Iterating over tuple:")
for num in numbers:
    print(num)

# ✅ Deletion - you can't delete individual items in a tuple (tuples are immutable)
# But you can delete the entire tuple
temp_tuple = (1, 2, 3)
print("Before deletion:", temp_tuple)

del temp_tuple  # Deletes the entire tuple

# Trying to print after deletion will raise an error
try:
    print(temp_tuple)  # This will cause an error
except NameError:
    print("Tuple deleted successfully!")
