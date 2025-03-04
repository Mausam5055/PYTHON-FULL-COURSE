# What is the Fibonacci Series?
# The Fibonacci series is a sequence of numbers where each term is the sum of the two 
# preceding terms. The series starts with 0 and 1 by default.

# Mathematical Formula:
# F(n)=F(n−1)+F(n−2)

# where: 
# # F(0)=0 (First term)
# # F(1)=1 (Second term)
# # F(n)=F(n−1)+F(n−2) (For ≥2 n ≥2)



n = int(input("enter the number of terms to be printed:"))

f1 = 0
f2 = 1

print("The fibonacci series for ", n , " terms are: ")
print(f1)
for i in range(n-1):
    print(f2)  # we put the print in loop so all the values are printed one after another 
    next_term = f1 + f2
    f1 = f2
    f2  = next_term
