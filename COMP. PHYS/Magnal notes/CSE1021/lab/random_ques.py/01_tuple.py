#1A
my_tuple = (10,20,30)
print(my_tuple)

#1B
second_element = my_tuple[1]
print(second_element)

#1C
new_tuple = (40,50)
combined_tuple = my_tuple + new_tuple
print(combined_tuple)

#1D
(a, b, c, d, e) = combined_tuple
print(a, b, c, d, e)

#1E
i = combined_tuple.index(30)   # try this using for loop
print("1E",i)

#1F
count = combined_tuple.count(20)
print(count)

#1G
my_list = list(combined_tuple)
print(my_list)

#1H
presence_40 = 40 in combined_tuple
print("Is 40 present in the tuple ? : ", presence_40)

#1I
sliced_tuple = combined_tuple[1:5]
print(sliced_tuple)

#1J
multiplied_tuple = tuple(3*x for x in my_tuple)
print(multiplied_tuple)