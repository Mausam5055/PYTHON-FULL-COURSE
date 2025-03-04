# Quick Quiz: Write a program to print the content of a list 
# using while loops.

l = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]

i = 0   #i=0 means "1" in the list 

while(i<len(l)): #condition: i is less than length of l
                  #(here the lenghth of l is 6(i.e from 0 to 6)
                   # 6 means upto "shubhi"   )
    print(l[i])
    i +=1          #this will print upto shubhi since i<len(l) 
                   #is the given condition for the loop

    
#NOTES : WHILE LOOP ALWAYS NEEDS A COIDTION UPTO WHICH IT IS
#        TRUE.         