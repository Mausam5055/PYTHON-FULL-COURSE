# INTRODUCTION TO STRINGS

# String is a data type in python.
# String is a sequence of characters enclosed in quotes.
# We can primarily write a string in these three ways.

# a ='harry' # Single quoted string
# b = "harry" # Double quoted string
# c = '''harry''' # Triple quoted string

#E.G. 1. name = "Mausam"

#NOTES: = string is immutable(i.e. we cannot edit a existing string,
# means that in the above created string named mausam we cannot edit
# by replacing any of the aplphabet to create a new name)

# STRING SLICING
# 
# A string in python can be sliced for getting a part of the strings.
# Consider the following string:

# name = "Harry"  => length of string = 5
#     (0,1,2,3,4,5)
#         or
#     (-5,-4,-3,-2,-1)
        
#  The index in a sting starts from 0 to (length -1) in Python.
#  In order to slice a string, we use the following syntax:
                 
                #  sl = name[ind_start:ind_end]
        #  here,
        #  ind_start ----- 1st index included
        #  ind_end ----last index is not included

# ------------EXAMPLE.--------

name = "Harry"
nameshort = name[0:3] # start from index 0 all the way till
                      #till 3 (excluding 3)
print(nameshort)
character1 = name[1]
print(character1)     



# NOTES :1. After we run the above code we get an output 
#         as 'har' 
        
#         2. Similarly when we run ,
#          sl[1,3] ----> returns 'ar'-->characters from 1 to 3
        
        # 3.after we write character1 = name[1] and type print
        #    we will get the character 'a '  from the name harry
        #   printed as an output






