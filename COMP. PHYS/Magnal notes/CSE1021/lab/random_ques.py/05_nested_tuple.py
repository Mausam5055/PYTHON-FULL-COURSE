#Creating a Nested Tuple
nested_tuple = ((1,2),(3, 4), (5, 6), (7, 8, 9))

#Accessing Elements
first_tuple = nested_tuple[1]
print(first_tuple)
second_tuple_element = nested_tuple[3][2]
print(second_tuple_element)

#Iterating through a nested tuple
for outer in nested_tuple:
    for elements in outer:
        print(elements)

#Nested Tuple Unpacking
tuple_1,tuple_2 = nested_tuple[1], nested_tuple[3]
print(tuple_1, "\n", tuple_2)

#Slicing a nested tuple
tuple_3 = nested_tuple[2][:]
print("slice",tuple_3)

#Combining nested tuples
nested_tuple2 = ((1,2), (2,3), (3,4))
combined_tuple = nested_tuple + nested_tuple2
print(combined_tuple)

#Comparing Nested Tuple
nested_tuple1 = ((5,2), (2,3), (3,4))
nested_tuple2 = ((1,2), (2,3), (3,4))
nested_tuple3 = ((1,2), (2,3), (3,4))
print(nested_tuple1 == nested_tuple2)
print(nested_tuple3 == nested_tuple2)

#Searching in a nested tuple
ele = 2
for inner in nested_tuple:
    if ele in inner:
        print(ele,"present")

#Reversing a nested tuple
reversed_tuple = tuple(tuple(reversed(inner)) for inner in reversed(nested_tuple))
print(reversed_tuple)

#Flattening a tuple
flat_list = []
for inner in nested_tuple:
    for element in inner:
        flat_list.append(element)
flat_tuple = tuple(flat_list)
print(flat_tuple)

#mixed nested tuple
mixed_nested_tuple = (('ravi', 'rahul'), [1, 2, 3], {'subject': 'CSE'})
print(mixed_nested_tuple)

#accessing elements of mixed nested tuple
list_access = mixed_nested_tuple[1][1]
print(list_access)
dict_access = mixed_nested_tuple[2]["subject"]
print(dict_access) 


