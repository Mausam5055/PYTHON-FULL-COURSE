# ---CHAPTER 7 – LOOPS IN PYTHON---

#1. Sometimes we want to repeat a set of statements in our 
# program. For instance: Print 1 to 1000

#2. Loops make it easy for a programmer to tell the computer 
# which set of instructions to repeat and how

# ---TYPES OF LOOPS IN PYTHON---

# Primarily there are two types of loops in python.
# • while loops
# • for loops

# -----FOR LOOP----

# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]
# Syntax:
# l = [1, 7, 8]
# for item in l:
# print(item) # prints 1, 7 and 8
 

#(WITHOUT USING LOOPS)

print(1)
print(2)
print(3)
print(4)
print(5)

# The same task can be done like this:(by the help of  loop)
for i in range(1, 6):
    print(i)