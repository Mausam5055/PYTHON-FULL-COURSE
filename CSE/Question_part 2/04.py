# Write the difference between append and insert, remove and pop, list and tuple
# 
#1. append() vs insert()
# append()
# Adds an item at the end of the list.
my_list = [1,2,3,4,5]
my_list.append(5)  # Adds 5 to the end

# insert()
# Adds an item at a specific position in the list.
my_list.insert(1, 10)  # Adds 10 at index 1

# 2. remove() vs pop()
# remove()
# Removes the first occurrence of a specified value.

my_list.remove(5)  # Removes the first 5 found
# pop()
# Removes an item at a specific index (default last) and returns it.


item = my_list.pop()    # Removes and returns last item  
item = my_list.pop(2)   # Removes and returns item at index 2. 