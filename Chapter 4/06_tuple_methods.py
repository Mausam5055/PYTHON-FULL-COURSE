# Here are some common methods and operations you can use 
# with tuples in Python:

#1. count(x): Returns the number of times x appears in the tuple.
# my_tuple = (1, 2, 3, 2, 2, 4)
# print(my_tuple.count(2))  # Output: 3

#2. index(x): Returns the index of the first occurrence of x 
# in the tuple. Raises a ValueError if x is not found.
# my_tuple = (1, 2, 3, 4)
# print(my_tuple.index(3))  # Output: 2

#3.len(): Returns the length of the tuple.
# my_tuple = (1, 2, 3, 4)
# print(len(my_tuple))  # Output: 4

#4. max(): Returns the largest item in the tuple.
 my_tuple = (1, 2, 3, 4)
 print(max(my_tuple))  # Output: 4

#5. min(): Returns the smallest item in the tuple.
# my_tuple = (1, 2, 3, 4)
# print(min(my_tuple))  # Output: 1

#6. sum(): Returns the sum of all elements in the tuple 
# (works with numeric tuples).
# my_tuple = (1, 2, 3, 4)
# print(sum(my_tuple))  # Output: 10

#7. in: Checks if an item exists in the tuple.
# my_tuple = (1, 2, 3, 4)
# print(2 in my_tuple)  # Output: True

#8. +: Concatenates two or more tuples.
# my_tuple1 = (1, 2)
# my_tuple2 = (3, 4)
# print(my_tuple1 + my_tuple2)  # Output: (1, 2, 3, 4)

#9. *: Repeats the elements in a tuple a specified number of times.
# python
# Copy code
# my_tuple = (1, 2)
# print(my_tuple * 3)  # Output: (1, 2, 1, 2, 1, 2)

#10.sorted(): Returns a new sorted list from the elements in the tuple.
# my_tuple = (3, 1, 4, 2)
# print(sorted(my_tuple))  # Output: [1, 2, 3, 4]

# Note that tuples themselves are immutable, so methods that
#  would modify a tuple, like append() or remove(), are 
# not available.













