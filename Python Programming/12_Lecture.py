#FInd the Factioraial Of  a Number By Creating a Function : 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of", num, "is", result)

#Find the Maximum of three Numbers using Function :
def max_of_three(a, b, c):
    return max(a, b, c)
a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) 
c = int(input("Enter third number: "))

maximum = max_of_three(a, b, c)
print("The maximum of the three numbers is:", maximum)

# #Write  A program to access a local variable outside function
# def my_function():
#     local_var = "I am a local variable"
#     return local_var
# result = my_function()
# print(result)

# #Write a program to demonstrate the use of global variable inside a function
# global_var = "I am a global variable"
# def my_function():
#     print(global_var)
# my_function()
# print(global_var)

# #Write a program to demonstrate the use of global variable inside a function and modify it
# global_var = "I am a global variable"
# def my_function():
#     global global_var
#     global_var = "I have been modified"
#     print(global_var)
# my_function()
# print(global_var)