# ------ESCAPE SEQUENCE CHARACTERS------

# Sequence of characters after backslash 
# "\" → Escape Sequence characters
# Escape Sequence characters comprise of more than 
# one character but represent one character when used 
# within the strings.

# EXAMPLE:  /N, /t, /', // , etc..
    # here, /N = newline
    #       /t = Tab 
    #       /'  = singlequote
    #       //  = backlash

a = 'Harry is a good boy\nbut not a bad \'boy\''
print(a)


# note: 1. inside a string we cannot make two lines 
#      so for which we use newline (/n) so as to 
#      make the line separate 

#      (i.e, a = "Harry is a god boy
#                 but not a bad boy")--> this is invalid syntax

#   so the above can be written as:
#      a = "Harry is a good boy\nbut not a bad boy"
# 
# 2. to use double quote inside a string we do it as
#      "Harry is a good boy\nbut not a bad \"boy\""
#      here we wanted to put double quote in boy which we
#  cant do as --"Harry is a good boy\nbut not a bad "boy""
# as this will be a invalid syntax.so for which we use 
# escape sequence character


