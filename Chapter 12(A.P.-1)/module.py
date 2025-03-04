def myFunc():
    print("Hello world!")

myFunc()

if __name__ == "__main__":              #this line of codes will run only in the "moduyle,py file"  but it wont run in th main.py file where it is being imorted
    # If this code is directly executed by running the file its present in
    print("We are directly running this code")
    myFunc()
    print(__name__)  

#the above 4 lines of code will not be imported in the main.py file


# ------IF __NAME__== ‘__MAIN__’ IN PYTHON ---------


# ‘__name__’ evaluates to the name of the module in python from where the program is 
# ran.
# If the module is being run directly from the command line, the ‘ __name__’ is set to 
# string “__main__”. Thus, this behaviour is used to check whether the module is run 
# directly or imported to another file