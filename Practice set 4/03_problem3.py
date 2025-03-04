# 3. Check that a tuple type cannot be changed in python.

a = (34, 234, "Harry")

a[2] = "Larry"

#we will get a error since tuple are immutable
#so we cant modify the existing tuple