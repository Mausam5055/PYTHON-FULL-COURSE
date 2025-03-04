# The walrus operator (:=), introduced in Python 3.8, allows you to assign a 
# value to a variable as part of an expression. This can reduce code 
# duplication and make your code more concise. Here's how it helps:

# 1. Avoiding Repeated Calculations
# Before the walrus operator, you often had to perform an operation twice 
# if you needed to both use its result in an expression and store it for 
# later:

data = input("Enter some data: ")
if len(data) > 10:
    print(f"Data is too long: {len(data)} characters!")


# With the walrus operator, you can do this in one step:


if (length := len(data := input("Enter some data: "))) > 10:
    print(f"Data is too long: {length} characters!")

# Here, data := input("Enter some data: ") 
# assigns the input to data, and length := len(data) assigns the length to 
# length, both within the if condition.