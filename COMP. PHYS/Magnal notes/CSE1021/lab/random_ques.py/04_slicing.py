my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10)

#Extract elements using positive slicing
pos_slice = my_tuple[2:5]
print(pos_slice)

#Extract elements using negative slicing
neg_slice = my_tuple[-9:-6]
print(neg_slice)

#Slicing with step
step_slice = my_tuple[2:9:2]
print(step_slice)

#Reverse Tuple using slicing
rev_tuple = my_tuple[::-1]
print(rev_tuple)

#Slice from start to a specific index
start_specific = my_tuple[:6]
print(start_specific)

#Slice from specific index to end
specific_end = my_tuple[6:]
print(specific_end)

#Slice Entire Tuple
entire_slice = my_tuple[:]
print(entire_slice)

#Extract last n elements using slicing
n = int(input("Enter the no of last n elements: "))
lastn_slice = my_tuple[-n:]
print(lastn_slice) 

#Extract last n elements using slicing
n = int(input("Enter the no of first n elements: "))
firstn_slice = my_tuple[:n]
print(firstn_slice)

#Combining slicing with unpacking
a,b,c = my_tuple[1:4]
print(a,b,c)

#Display Odd index elements
odd_index = my_tuple[1::2]
print(odd_index)

#Display even index elements
even_index = my_tuple[::2]
print(even_index)

#Extract a subset of the reversed tuple
subset = rev_tuple[1:5]
print(subset)
