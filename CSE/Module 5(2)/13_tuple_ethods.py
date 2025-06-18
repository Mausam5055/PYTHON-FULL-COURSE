# Basic Tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# ✅ Concatenation: Combine two tuples using +
combined = t1 + t2
print("Concatenated Tuple:", combined)  # (1, 2, 3, 4, 5, 6)

# ✅ Membership Test: Check if a value exists in a tuple
print("Is 3 in t1?", 3 in t1)          # True
print("Is 7 not in t2?", 7 not in t2)  # True

# ✅ Logical Operators: Combine conditions
# Both must be True
print("Logical AND:", (2 in t1) and (5 in t2))  # True

# At least one should be True
print("Logical OR:", (10 in t1) or (5 in t2))   # True

# Negation
print("Logical NOT:", not (1 in t2))  # True (1 is not in t2)

# ✅ Nested Tuples: Tuples inside a tuple
nested = ((1, 2), (3, 4), (5, 6))

# Accessing nested elements
print("First pair:", nested[0])        # (1, 2)
print("Second element of second pair:", nested[1][1])  # 4

# Membership in nested tuples
print("Is (3, 4) in nested?", (3, 4) in nested)  # True
print("Is 4 in nested?", 4 in nested)            # False, 4 is inside a nested tuple
