# ---------STRING FUNCTIONS---------

# Some of the commonly used functions to perform operations on or 
# manipulate strings are as follows.
#  Let us assume there is a string ‘str’ as follows:
# str = 'harry'
# Now when operated on this string ‘str’, these functions
#  do the following:


# 1. len () function – This function returns the length 
# of the strings.
#  str = "harry"
#  print(len(str)) # Output: 5


# 2. String.endswith("rry") – This function_ tells whether
#  the variable string ends with the string "rry" or not.
#  If string is "harry", it returns true for "rry" since Harry ends 
# with rry.
#  str = "harry"
#  print(str.endswith("rry")) # Output: True


# 3. string.count("c") – counts the total number of occurrences of
#  any character.
#  str = "harry"
#  count = str.count("r")
#  print(count) # Output: 2


# 4. the first character of a given string.
#  str = "harry"
#  capitalized_string = str.capitalize()
#  print(capitalized_string) # Output: "Harry"


# 5. string.find(word) – This function friends a word and returns
#  the index of first occurrence of that word in the string.
#  str = "harry"
#  15
#  index = str.find("rr")
#  print(index) # Output: 

name = "harry"

print(len(name))
print(name.endswith("rry"))
print(name.startswith("ha"))
print(name.capitalize())


# note : in our working code above we wrote in different
#  way to save time(a single code be written in differnt ways)