# -   -------WITH STATEMENT--------

# The best way to open and close the file automatically is
# the with statement.

# # Open the file in read mode using 'with', which 
# # automatically closes the file
# with open("this.txt", "r") as f:
# # Read the contents of the file
# text = f.read()
# # Print the contents
# print(text)


f = open("file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file