# Give justification for following points. 
# 1.Is it possible to add a list as an element in a set? 
# 2.Is it possible to add a tuple as an element in a 
# set? 
#3.Is it possible to add a dictionary as an element in a set?

#1. ANSWER:
# ✅ 1. Is it possible to add a list as an element in a set?
# ❌ No, it is not possible.

# ✅ Justification:
# 1.Lists are mutable (changeable) — you can add, remove, or change elements in a 
# list.
# 2.Sets only allow hashable (immutable) elements.
# 3.Since lists can change, they are not hashable, and thus cannot be added to a 
# set.

my_set = set()
my_list = [1, 2, 3]
my_set.add(my_list)  # ❌ This will raise TypeError


# 2.ANSWER:
# ✅ 2. Is it possible to add a tuple as an element in a set?
# ✅ Yes, it is possible.

# ✅ Justification:
# Tuples are immutable, which means their contents cannot be changed after 
# creation.Because they are hashable, tuples can be added to a set.

# Example:

my_set = set()
my_tuple = (1, 2, 3)
my_set.add(my_tuple)  # ✅ Works fine
print(my_set)


# ✅ 3. Is it possible to add a dictionary as an element in a set?
# ❌ No, it is not possible.

# ✅ Justification:
#1. Dictionaries are mutable, as you can change their contents.
#2.Like lists, dictionaries are unhashable, so they cannot be added to a set.
# Example:
my_set = set()
my_dict = {"a": 1, "b": 2}
my_set.add(my_dict)  # ❌ This will raise TypeError
