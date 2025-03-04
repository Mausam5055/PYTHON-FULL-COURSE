#  ----MODES OF OPENING A FILE-------


# r – open for reading
# w - open for writing 
# a - open for appending
# + - open for updating.
# ‘rb’ will open for read in binary mode.
# ‘rt’ will open for read in text mode

f=open("file.txt")
lines=f.readlines()
print(lines,type(lines))   #type(lines) will say which 
                           #kind of lines are they
f.close