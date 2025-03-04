
# Python provides various methods to work with sets. Here’s a list of commonly used set methods, along with explanations and examples for each:

# 1. add(elem)
# Adds an element to the set.
# If the element already exists, it does nothing.
# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)  # Output: {1, 2, 3, 4}

# 2. remove(elem)
# Removes the specified element from the set.
# Raises a KeyError if the element is not found.
# my_set.remove(3)
# print(my_set)  # Output: {1, 2, 4}

# 3. discard(elem)
# Removes the specified element from the set.
# Does not raise an error if the element is not found.
# my_set.discard(5)  # Does nothing as 5 is not in the set

# 4. pop()
# Removes and returns an arbitrary element from the set.
# Raises a KeyError if the set is empty.
# elem = my_set.pop()
# print(elem)   # Output: 1 (or any other element, as sets are unordered)
# print(my_set)  # Remaining elements

# 5. clear()
# Removes all elements from the set.
# my_set.clear()
# print(my_set)  # Output: set()

# 6. union(*sets) or |
# Returns a new set with all elements from the set and all others.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1.union(set2)
# print(union_set)  # Output: {1, 2, 3, 4, 5}

# 7. intersection(*sets) or &
# Returns a new set with elements common to the 
# set and all others.
# intersection_set = set1.intersection(set2)
# print(intersection_set)  # Output: {3}

# 8. difference(*sets) or -
# Returns a new set with elements in the set that are not 
# in the others.
# difference_set = set1.difference(set2)
# print(difference_set)  # Output: {1, 2}

# 9. symmetric_difference(set) or ^
# Returns a new set with elements in either the set or the 
# other, but not both.
# sym_diff_set = set1.symmetric_difference(set2)
# print(sym_diff_set)  # Output: {1, 2, 4, 5}

# 10. issubset(set)
# Returns True if the set is a subset of another set.
# subset = {1, 2}
# print(subset.issubset(set1))  # Output: True

# 11. issuperset(set)
# Returns True if the set is a superset of another set.
# print(set1.issuperset(subset))  # Output: True

# 12. isdisjoint(set)
# Returns True if the set has no elements in common with another set.
# disjoint_set = {5, 6, 7}
# print(set1.isdisjoint(disjoint_set))  # Output: True

# 13. copy()
# Returns a shallow copy of the set.
# set_copy = set1.copy()
# print(set_copy)  # Output: {1, 2, 3}

# 14. update(*sets) or |=
# Updates the set, adding elements from all others.
# set1.update(set2)
# print(set1)  # Output: {1, 2, 3, 4, 5}

# 15. intersection_update(*sets) or &=
# Updates the set, keeping only elements found in it and all others.
# set1.intersection_update(set2)
# print(set1)  # Output: {3}

# 16. difference_update(*sets) or -=
# Updates the set, removing elements found in others.
# set1 = {1, 2, 3, 4}
# set1.difference_update(set2)
# print(set1)  # Output: {1, 2}

# 17. symmetric_difference_update(set) or ^=
# Updates the set, keeping only elements found in either set, 
# but not in both.
# set1 = {1, 2, 3}
# set1.symmetric_difference_update(set2)
# print(set1)  # Output: {1, 2, 4, 5}


# These methods give you a powerful set of tools to work with sets in Python, allowing for a wide variety of operations.