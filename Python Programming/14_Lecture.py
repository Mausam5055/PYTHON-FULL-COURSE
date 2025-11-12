# Our starting list for all the examples below
my_list = [10, 5, 8, 1, 7, 5]
print("Original List:", my_list)
print("--------------------")

# a) Total items in the list
#    len() is a built-in function that gets the length
print("a) Total items:", len(my_list))

# b) Last item in the list
#    -1 is the index for the last item
print("b) Last item:", my_list[-1])

# c) Reverse the list
#    [::-1] is a special "slice" that creates a new, reversed list
print("c) Reverse:", my_list[::-1])

# d) Check if 5 is in the list
#    The 'in' keyword checks for you
if 5 in my_list:
    print("d) Yes, 5 is in the list")
else:
    print("d) No, 5 is not in the list")

# e) Count how many 5s are in the list
#    The .count() method does this for us
print("e) Count of 5s:", my_list.count(5))

# f) Remove first and last, then sort
#    This doesn't change the original 'my_list'
#    my_list[1:-1] creates a new list from the second item (index 1)
#    up to (but not including) the last item (index -1).
new_list = my_list[1:-1]
new_list.sort() # .sort() sorts the list in place
print("f) After removing first & last and sorting:", new_list)

# g) Count numbers less than 5
#    We create a counter and loop through the list
count_less_than_5 = 0
for num in my_list:
    if num < 5:
        count_less_than_5 = count_less_than_5 + 1
print("g) Numbers less than 5:", count_less_than_5)

# h) Average of all numbers
#    sum() adds all items, len() gets the count
average = sum(my_list) / len(my_list)
print("h) Average:", average)

# i) Largest and smallest number
#    max() and min() are helpful built-in functions
print("i) Largest:", max(my_list))
print("i) Smallest:", min(my_list))

# j) Second largest and second smallest
#    IMPORTANT: We make a *copy* so we don't change our original 'my_list'
sorted_list = list(my_list)
sorted_list.sort() # Sort the copy
print("j) Second largest:", sorted_list[-2]) # -2 is the second-to-last item
print("j) Second smallest:", sorted_list[1])  # 1 is the second item

# k) Count of even numbers
#    We use the % operator again
even_count = 0
for num in my_list:
    if num % 2 == 0: # If the remainder when divided by 2 is 0, it's even
        even_count = even_count + 1
print("k) Even numbers:", even_count)