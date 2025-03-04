st = "Hey Harry you are amazing"

f = open("myfile.txt", "a")  #"a" = appending a file

f.write(st)

f.close()

#appending a file means to add something at the end of 
#that file

#after we run this code we will get a 
# line--"Hey Harry you are amazing"
#added in the file.txt and this line will keep on adding
#in the file.txt as many times we run this above code 