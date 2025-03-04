list1 = [10, 11, 12, 13, 14] 
list2 = [20, 30, 42] 

res = [j for i in [list1, list2] for j in i] 

print ("Concatenated list:\n", res)