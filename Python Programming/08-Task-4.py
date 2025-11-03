# Assignment Problems
# 1. Write a program to input a string and check whether it is palindrome string or not
# 2. Write a Program to input a sentence and find number of alphabets, digits and special symbols in
# it.
# 3.Write a program that asks the user to enter a string. The program should
# print the following:
# (n) The total number of characters in the string
# (o) The string should repeat 10 times using ‘*’(multiplication).
# (p) The first character of the string (remember that string indices start at 0)
# (q) The first three characters of the string
# (r) The last three characters of the string
# (s)The string backwards(means reverse)
# (t) The seventh character of the string if the string is long enough and a error
# message otherwise
# (u) The string with its first and last characters removed(use slice operation)
# (v)The string in all caps
# (w) The string with every ‘a’ replaced with an ‘e’
# (x) The string with every space replace by ‘ –‘
# (y)The string with every letter replace by space

# Assignment Problems

# 1. Check if a string is palindrome
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome")

# 2. Count alphabets, digits, and special symbols
st = input("\nEnter a sentence: ")
alphabets = digits = symbols = 0
for ch in st:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    else:
        symbols += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special symbols:", symbols)

# 3. String operations
t = input("\nEnter another string: ")

print("(n) Total characters:", len(t))
print("(o) Repeated 10 times:", t * 10)
print("(p) First character:", t[0] if t else "Empty")
print("(q) First 3 characters:", t[:3])
print("(r) Last 3 characters:", t[-3:])
print("(s) Reversed:", t[::-1])

if len(t) >= 7:
    print("(t) 7th character:", t[6])
else:
    print("(t) Too short")

print("(u) Without first & last:", t[1:-1])
print("(v) All caps:", t.upper())
print("(w) Replace 'a' with 'e':", t.replace('a', 'e'))
print("(x) Replace spaces with '-':", t.replace(' ', ' - '))
print("(y) Letters replaced by space:", ''.join(' ' if c.isalpha() else c for c in t))
