# -------------EXCEPTION HANDLING IN PYTHON------------

# There are many built-in exceptions which are raised in python when 
# something goes wrong.

# Exception in python can be handled using a try statement. The code 
# that handles the exception is written in the except clause.

# try:
# # Code which might throw exception
# except Exception as e: 
# print(e)
# When the exception is handled, the code flow continues without program interruption.
# We can also specify the exception to catch like below:



#                 try:
#                     # Code
#                 except ZeroDivisionError:
#                     # Code
#                 except TypeError:
#                     #code
#                 except:
#                     # Code # All other exceptions are handled here.

# -----------RAISING EXCEPTIONS------
# We can raise custom exceptions using the ‘raise’ keyword in python.


a=int(input("Hey,Enter a Number:"))
print(a)

#here in  above if we put anything except a number as input then 
#we will see that our code will crash

#Eg. say if wu gave an input as--> "mausam" then we will ge5t
#a error(since mausam is not an integer/number) 

#but if we want that there must be no crash of code after putiing 
#anything instead of a number/integer we take the help of "try" 
# function

#our code crashes and shows "valueError"

#see how "try" function is used (in the next file)

