# #check if a number is prime or not:(number divdible by 1 and itslf)

# #Using For Loop : 
# n = int(input("Enter The Number: "))
# factors_of_n = 0  #Initial Counter for factors

# for i in range(1, n + 1):  # Loop from 1 to n
#     if n % i == 0:  #Check divisibility
#         factors_of_n = factors_of_n +1  #increment condition of the loop

# # A prime number has exactly 2 factors: 1 and itself
# if factors_of_n == 2:
#     print("The Number Is Prime")
# else:
#     print("The Number Is Not Prime")

# #Using while loop :

# n = int(input("Enter The Number: "))
# i = 1  # Start from 1
# c = 0  # Counter for factors

# while i <= n:
#     if n % i == 0:  # Check divisibility
#         c += 1
#     i += 1  # Increase i

# # A prime number has exactly 2 factors: 1 and itself
# if c == 2:
#     print("The Number Is Prime")
# else:
#     print("The Number Is Not Prime")


n = int(input("Enter the number:"))
factors_of_n =  0
for i in range(1,n+1):
       if n%i == 0:
        factors_of_n = factors_of_n+1
if factors_of_n == 2:
    print("The Number Is A prime Number") 
else :
    print("The Number is Not a prime Number")