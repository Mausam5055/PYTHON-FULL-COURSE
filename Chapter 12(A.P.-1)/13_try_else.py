# -----------TRY WITH ELSE CLAUSE----------- 

# Sometimes we want to run a piece of code when try was successful.

#                 try:
#                      # Somecode
#                 except:
#                      # Somecode
#                 else:
#                      # Code # This is executed only if the try was
#                      #  successful


try:
    a = int(input("Hey, Enter a number: "))
    print(a)

    
except Exception as e:
    print(e) 


else:
    print("The input was valid")

#here if our input is valid then we will get the ouput printed
#as well as we will get the statement which is inside the else
#function printed

#but if our input is not valid then we willl get an valid error
#(our code wont crash) and also this time we will not get the 
#code inside else function printed
