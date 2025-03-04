# whenever we run any code it fist runs and then we get the 
# desired result (in the terminal) and then it closes up, 
# in this case we dont get our outcome saved in our hard disk.

# The random acess memory (ram)  temporarily stores the Data 
# and then it generates some value as soon as we run our code 
# and then we get our desired outcome and then when we close our 
# terminal all our data of the code that we ran to exucute a 
# program gets lost.
#               so to save our data that we got in the terminal
# after running our code we need "FILE I/O" --that will store 
# the daata in it after the code is being executed


#       ---------CHAPTER 9 – FILE I/O----------

# The random-access memory is volatile, and all its contents 
# are lost once a program terminates.In order to persist the 
# data forever, we use files.A file is data stored in a 
# storage device. A python program can talk to the file by 
# reading content from it and writing content to it.

#         --------- TYPE OF FILES. -------

# There are 2 types of files:
# 1. Text files (.txt, .c, etc)
# 2. Binary files (.jpg, .dat, etc)
# Python has a lot of functions for reading, updating, and 
# deleting files.

#       ----OPENING A FILE-----

# Python has an open() function for opening files. 
# It takes 2 parameters: filename and mode.

# # open("filename", "mode of opening(read mode by default)")
# open("this.txt", "r")

# READING A FILE IN PYTHON
# # Open the file in read mode
# f = open("this.txt", "r")
# # Read its contents
# text = f.read()
# # Print its contents
# print(text)
# Close the file
# f.close()

f=open("file.txt", "r")  #filename , read mode(r){not necessary to write}
data=f.read()
print(data)
f.close

# -------OTHER METHODS TO READ THE FILE.--------

# We can also use f.readline() function to read one 
# full line at a time.
# 
# f.readline() # Read one line from the file

