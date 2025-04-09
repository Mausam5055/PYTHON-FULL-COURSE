palindrome = []
for i in range(100, 200): # instead of i we can also write num 
    a = str(i)
    if a == a[::-1]:
        palindrome.append(i)

print(palindrome)
