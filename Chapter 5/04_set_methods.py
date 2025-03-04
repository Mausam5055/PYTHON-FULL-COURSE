# --PROPERTIES OF SETS---

# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.
# ---OPERATIONS ON SETS---

# Consider the following set:
# s = {1,8,2,3}

# 1. len(s): Returns 4, the length of the set 

# 2• s.remove(8): Updates the set s and removes 8 from s.

# 3• s.pop(): Removes an arbitrary element from the set 
# and return the element removed.

# 4• s.clear():empties the set s.

# 5• s.union({8,11}): Returns a new set with all items from 
# both sets. {1,8,2,3,11}.

# 6• s.intersection({8,11}): Return a set which contains 
# only item in both sets {8}

s = {1, 5, 32, 54,5, 5, 5, "Harry"}

print(s, type(s)) #this will print 1st s and then print type(s)

s.add(566)
print(s, type(s))
s.remove(1)
print(s, type(s))


