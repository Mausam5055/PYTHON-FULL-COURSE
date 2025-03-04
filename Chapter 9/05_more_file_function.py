#the previous way can be done in a simplified way using 
#the help of while loop


f = open("file.txt")

line = f.readline()
while(line != ""):   #!=  ----> means "not equal to"
                     #means until any line is not eqaul
                     #to an empty string keep on printing 
                     #the lines and as soon as a empty strig
                     #comes (i.e no line) stop executing
    print(line)
    line = f.readline()

f.close()