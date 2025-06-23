palindrome = []
for i in range(100, 200):  # ✅ Yes, you can use `num` instead of `i`
    a = str(i)             # 👈 This converts the number `i` into a string
    if a == a[::-1]:       # Checks if the string is the same when reversed
        palindrome.append(i)

print(palindrome)

# num[::-1] reverses the string.

num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome")
