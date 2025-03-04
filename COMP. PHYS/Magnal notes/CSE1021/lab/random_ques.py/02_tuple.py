
tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (7, 8, 9)

# Solution 1
sol_1 = tuple_1 + tuple_2
print(sol_1)

# Solution 2 
(a, b, c, d, e) = tuple_1
f, g, h = tuple_2
sol_2 = (a, b, c, d, e, f, g, h)
print(sol_2)

# Solution 3
sol_3 = tuple_1
for i in range(len(tuple_2)):
    sol_3 = sol_3 + (tuple_2[i],)
print(sol_3)

# Solution 4
l1 = list(tuple_1)
l2 = list(tuple_2)
l1.extend(l2)
sol_4 = tuple(l1)
print(sol_4)

# Solution 5
def combined_tuple(t1, t2):
    return t1 + t2
sol_5 = combined_tuple(tuple_1, tuple_2)
print(sol_5) #try with recursive