#Using multiplication operator
original_tuple = (1, 2, 3)
replicated_tuple = original_tuple * 3
print(replicated_tuple)

#Convert into list, multiply, and convert back to tuple
replicated_list = list(original_tuple) * 3
replicated_tuple = tuple(replicated_list)
print(replicated_tuple)

#Using loop
replicated_tuple = ()
for i in range(4): 
    replicated_tuple += original_tuple
print(replicated_tuple)

#Using nested loops
replicated_tuple = ()
for i in range(3): 
    for item in original_tuple:
        replicated_tuple += (item,)
print(replicated_tuple)

#Using function
def replicate_tuple(original_tuple, n):
    return original_tuple * n

replicated_tuple = replicate_tuple(original_tuple, 5)
print(replicated_tuple)

#Combine multiplication and concatenation
replicated_tuple = original_tuple * 2 + (1, 2, 3)
print(replicated_tuple)
