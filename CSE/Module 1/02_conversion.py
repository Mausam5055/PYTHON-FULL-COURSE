# In Python, binary literals are written using a prefix of 
# 0b or 0B to indicate that the number is in base-2 
# (binary). The digits allowed in binary literals are only 
# 0 and 1. Here's how it works:

a = 0b1111   # Valid: Binary representation of 15
print(a)  # Output: 15

b = 0B1010   # Valid: Binary representation of 10
print(b)  # Output: 10

a = 0b1111   # Valid: Binary representation of 15
print(oct(a))  # Output: 15

#NOTES: 

# 1.a = 0b123 is invalid because 123 contains digits other 
# than 0 and 1.
# 2.a = b111 is invalid because the prefix b is not valid in 
# Python binary literals (it should be 0b or 0B).
        #SIMILARLY,

# 3. Octal Form(Base-8):
# The allowed digits are : 0 to 7
# Literal value should be prefixed with 0o or 0O.

# Eg: a=0o123
# a=0o786


# 4. Hexa Decimal Form(Base-16):
# 1.The allowed digits are : 0 to 9, a-f 
# (both lower and upper cases are allowed)
# 2.Literal value should be prefixed with 0x or 0X

# Eg:
# a =0XFACE
# a=0XBeef
# a =0XBeer

# Note: Being a programmer we can specify literal values 
# in decimal, binary, octal and hexadecimal forms. 
# But PVM will always provide values only in decimal form.