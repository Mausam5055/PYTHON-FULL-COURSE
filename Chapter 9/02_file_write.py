# --------WRITE FILES IN PYTHON------

# In order to write to a file, we first open it in write 
# or append mode after which, we use the python’s f.write()
# method to write to the file!

# # Open the file in write mode
# f = open("this.txt", "w")
# # Write a string to the file
# f.write("this is nice")
# # Close the file
# f.close()

st = "Hey Harry you are amazing" #st is shortform of string 

f = open("myfile.txt", "w")

f.write(st)

f.close()

#  as soon as we run this code a new file will be created 
# and the string = "Hey harry you are amazing" will be 
# saved in this txt file