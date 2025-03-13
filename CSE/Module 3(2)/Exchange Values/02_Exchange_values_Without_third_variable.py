#M-1(Without Operator)
a = 5
b = 10

a=a+b
b=a-b
a=a-b
print("a =", a)  # Output: a = 10
print("b =", b)  # Output: b = 5




#M-2(with Operator)
a = 5
b = 10

a, b = b, a  # Swapping values

print("a =", a)  # Output: a = 10
print("b =", b)  # Output: b = 5
