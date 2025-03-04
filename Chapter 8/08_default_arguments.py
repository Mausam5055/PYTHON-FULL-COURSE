# -----DEFAULT PARAMETER VALUE------

# We can have a value as default as default argument in a
# function.If we specify name = “stranger” in the line containing
# def, this value is used when no argument is passed.

# Example:

# def greet(name = "stranger"):
# # function body
# greet() # name will be "stranger" in function body (default)
# greet("harry") # name will be "harry" in function body (passed)

def goodDay(name, ending="Thank you"):  
    print("Good Day," + name)  # this codeline can also be written as;
                                # print(f"Good Day, {name}")--- means the same
    print(ending)

goodDay("Harry")   #no ending after harry so default ending will be printed

#in above we already set a dfault ending before hand
#means if there is no ending written then the code will
#return us the defaut ending as "thank you"

#EG: If we already have an ending written than 
#"thank you" will not be printed

def goodDay(name, ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Harry", "Thanks")  #ending after harry is thanks

#after runing tyhe code thanks will be printed now rather tha 
#"thank you" since we gave an ending
