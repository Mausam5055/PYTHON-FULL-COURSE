# ---ELIF CLAUSE--

#elif in python means [else if]. An if statements can be chained together with a lot of 
#these elif statements followed by an else statement.

#         if (condition1):
#         #code
#         elif (condition2): # this ladder will stop once a condition in an 
#          if or 
#         elif is met.
#         #code
#         elif(condition3):
#         #code 
#         else:
#         #code

# IMPORTANT NOTES:
# 1. There can be any number of elif statements.
# 2. Last else is executed only if all the conditions inside elifs fail

a = int(input("Enter your age: "))

# If elif else ladder
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")    

else:
    print("You are below the age of consent")


print("End of Program") #we may not necessarily write this

#see else if statement from c++ notes 

# //NOTEs:    1.At 1st in if else statement we will write 'if'statement
# //             and then 'else if' statement and at last we write 'else'  
# //             statement


# //        2. the order must be mantained as written in the above code 


# //       3. when we run the code it will check 1st the "if" statement 
# //             and if the 'if' statement is ivalid then the code will not go 
# //             further and check the other statements


# //       4.if the 'if' statement is satisfied then it will check for  "else if"
# //           statement and "else statement"

