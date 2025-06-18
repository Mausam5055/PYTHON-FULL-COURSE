# Simple examples of any(), all(), sorted(), and tuple() using a tuple

# Define a basic tuple
numbers = (0, 5, 10)

# any() - checks if any value is True (non-zero)
print("any():", any(numbers))  # True because 5 and 10 are non-zero

# all() - checks if all values are True (non-zero)
print("all():", all(numbers))  # False because 0 is False

# sorted() - returns a sorted list (not a tuple)
print("sorted():", sorted(numbers))  # [0, 5, 10]

# Convert sorted list back to tuple using tuple()
sorted_tuple = tuple(sorted(numbers))
print("sorted tuple:", sorted_tuple)  # (0, 5, 10)

# tuple() - convert a list to tuple
my_list = [1, 2, 3]
converted = tuple(my_list)
print("tuple() from list:", converted)  # (1, 2, 3)


# any(): True
# all(): False
# sorted(): [0, 5, 10]
# sorted tuple: (0, 5, 10)
# tuple() from list: (1, 2, 3)
