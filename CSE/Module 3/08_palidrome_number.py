#reverse a number using for and while loop(palidrome) :

#Method 1: WHILE lOOP:

n = int(input("Enter The Number: "))
i = n 
s =  0
while(n>0):
    d=n%10
    s=s*10+d
    n=n//10
if(i == s):
 print("palindrome")
else:
   print("Not Palindrome")

# A palindrome number is a number that remains the same when its digits are reversed. 
# In other words, if you read the number from left to right or right to left, it remains 
# unchanged.

# Examples of Palindrome Numbers
# ✅ 121 → Reverse is 121 (Palindrome)
# ✅ 1331 → Reverse is 1331 (Palindrome)
# ✅ 98789 → Reverse is 98789 (Palindrome)

# ❌ 123 → Reverse is 321 (Not a Palindrome)
# ❌ 1456 → Reverse is 6541 (Not a Palindrome)