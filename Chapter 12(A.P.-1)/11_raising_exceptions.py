# We can also specify the exception to catch like below:

#             try:
#             # Code
#                    except ZeroDivisionError:
#             # Code
#                     except TypeError:
#             # Code
#                     except:
#             # Code # All other exceptions are handled here.

try:
    a = int(input("Hey,Enter a number:"))
    print(a)

except ValueError as V:    #for value errors : this line will not let the 
    print("Heyyyyy")       #entire code to crash rather it will type this 
    print(V)               #message inplace of crashing

except Exception as e:
    print(e)

print("Thank you")

#here value error is the error that we get after we put aything else 
#as an input rather than an integer/number in the above code 
#the code crashes ans shows value error