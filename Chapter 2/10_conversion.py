#CONVERSION OF STRING TO FLOAT:

a = "31.2"  # a is string type datatype
b = float(a) # (b = a but the type should be float)
t = type(b) 

print(t)

#here we converted string to float so after we run the code the dtatype 'a' 
#will come as float not string (since we converted it)

# SIMILARLY......
# A number can be converted into a string and vice versa (if possible)
# There are many functions to convert one data type into another.EG.
# str(31) =>"31" # integer to string conversion
# int("32") => 32 # string to integer conversion
# float(32) => 32.0 # integer to float conversion
# … and so, on
# Here "31" is a string literal and 31 a numeric literal.