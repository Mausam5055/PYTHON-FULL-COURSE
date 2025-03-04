# 1.Create a set my_set which contains the elements 1 to 5.

my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set = set([1, 2, 3, 4, 5, ])
print(my_set)

# 2.Create a set my_set1 which contains the mixed type of elements 1, 2.5 and Python.
my_set1 = {1, 2.5, "Python"}
print(my_set1)

my_set1 = set([1, 2.5, "Python"])
print(my_set1)

#Empty Set
s1 = set()
s1.add(5)   #addinng a single element to empty set 1

#Remove duplicate elements using update
set1 = {1, 2, 3 }
set2 = {3, 4, 5}
set1.update(set2)
print(set1)

#Remove 6 from set1 - remove()
#if the element is found, it will be removed otherwise we will get key error
# set1.remove(6)
# print(set1)

# set1 and set2 are used for every question below
#Add element 6 in set1
set1.add(6)
print(set1)

#Remove 6 and print set1
set1.remove(6)
print(set1)

#discard - remove 6 if present otherwise does nothing
set1.discard(6)
print(set1)

#Removes and returns an arbitary element
print(set1.pop())
print(set1)

#Union() - join two sets
union_set = set1.union(set2)
print(set1)
print(union_set)

#intersection - Set Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)

# Symmetric Difference
set1 = {1, 2, 3 }
set2 = {3, 4, 5}
symmetric_difference = set1.symmetric_difference(set2)
print("Symmetric difference : ", symmetric_difference)

#Set Difference
set1 = {1, 2, 3 }
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print("difference : ", difference_set)

#Subset and superset
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))
print(set2.issuperset(set1))

set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set2.issubset(set1))
print(set1.issuperset(set2))

#Check Membership
set1 = {1, 2, 3, 4}
print(2 in set1)
print(2 not in set1)
print(10 in set1)
print(10 not in set1)

#Clearing a set
set1 = {1, 2, 3, 4}
print(set1)
set1.clear()
print(set1)

#Copying a set
set1 = {1, 2, 3, 4, 5}
set2 = set1.copy()
print(set2)

#Length of a set
print(len(set1))

#isdisjoint()-Returns True if two sets have null intersection
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.isdisjoint(set2))

set1 = {5,6,7,8}
set2 = {1,2,3,4}
print(set1.isdisjoint(set2))

## all() - Returns True if all the elements are true 
set1 = {5,6,7,8}
print(all(set1))

set1 = {0,5,6,7,8}
print(all(set1))

# any() - Returns True if any of the elements are true
set1 = {5,6,7,8}
print(any(set1))
set1 = {0,5,6,7,8}
print(any(set1))

# max()
set1 = {0,5,6,7,8}
print(max(set1))

# min()
set1 = {0,5,6,7,8}
print(min(set1))

# sorted() - returns a new list, not a set.
my_set = {5, 1, 4, 3, 2}
sorted_list = sorted(my_set)
print("Sorted List:", sorted_list)

#sum
set1 = {1, 3, 5}
print(sum(set1))

# enumerate() - Returns an enumerate object that contains index and value of the set as a pair
set1 = {1, 3, 5} 
for i in enumerate(set1):	
  print(i)

# Sets in Python are unordered collections, so their elements don't have a fixed position.
# When you print or access the set, the order may be different from how you defined it.
my_set = {5, 1, 4, 3, 2}
print(my_set)
{1, 2, 3, 4, 5}
# If you need elements in a specific order, you can use sorted() - returns a new list, not a set.
my_set = {5, 1, 4, 3, 2}
sorted_list = sorted(my_set)
print("Sorted List:", sorted_list)
