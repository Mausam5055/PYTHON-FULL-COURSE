a = 5
b = 10

# Swapping using XOR
a = a ^ b
b = a ^ b
a = a ^ b

print("a =", a)  # Output: a = 10
print("b =", b)  # Output: b = 5

# Explanation:
# 1.a = a ^ b → Stores the XOR of a and b in a.

#2. b = a ^ b → Since a now holds a ^ b, doing b = a ^ b 
# gives b = (a ^ b) ^ b, which simplifies to b = a 
# (original a value).

#3. a = a ^ b → Since b now holds original a, doing 
# a = a ^ b gives a = (a ^ b) ^ a, which simplifies to 
# a = b (original b value).