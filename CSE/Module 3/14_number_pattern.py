#write  a python code to print the following pattern:
#   1
#   1 2 
#   1 2 3
#   1 2 3 4
#HINT: this can be done by nested loops

row = 4  #number of rows required
num = 1 
for i in range(1,row+1):  #here i is the number of rows to be printed
      for j in range(1,i+1): #inner loop for numbners in each row
            num = num +1 
            print(j,end=" ")
      print() #move to the next lineafter printing a row 
            
#notes : here end=" " keeps printing on the same line with spaces 
#between each number