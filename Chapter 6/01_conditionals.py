# ---CHAPTER 6 – CONDITIONAL EXPRESSION---

# 1.Sometimes we want to play PUBG on our phone if the day is 
# Sunday.
# 2.Sometimes we order Ice Cream online if the day is sunny.
# 3.Sometimes we go hiking if our parents allow.

# All these are decisions which depend on a condition being met.
# In python programming too, we must be able to execute
#  instructions on a condition(s) being met.
# This is what conditionals are for!

# --IF ELSE AND ELIF IN PYTHON---
# If else and elif statements are a multiway decision taken 
# by our program due to certain conditions in our code.

# Syntax:
# if (condition1): # if condition1 is True
# print ("yes")
# elif(condition2): # if condition2 is True 
# print("no")
# else: # otherwise
# print("maybe")
 
# CODE EXAMPLE.
# a=22
# if(a>9):
# print("greater")
# else:
# print("lesser")

a = int(input("Enter your age: "))

# If else statement
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

else:
    print("You are below the age of consent")


# ---RELATIONAL OPERATORS--

# Relational Operators are used to evaluate conditions inside the if 
# statements. Some examples of relational operators are:

# 1.  ==: equals.
# 2.  > =: greater than/ equal to.
# 3.  < =: lesser than/ equal to. 

# ---LOGICAL OPERATORS---
# In python logical operators operate on conditional statements. 
# For Example:

# 1• and – true if both operands are true else false.
# 2• or – true if at least one operand is true or else false.
# 3• not – inverts true to false & false to true
