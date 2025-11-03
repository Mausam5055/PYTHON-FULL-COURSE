#Print Number from 1 to 100 using while loop
i = 1
while i <= 100:
    print(i)
    i = i+1  

#Print Number from 100 to 1
i = 100
while i >= 1:
    print(i)
    i = i-1

#print multiplication Table of NUmber n Using While Loop
n = int(input("Enter a number to print its multiplication table: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n*i)
    i = i + 1

#Write a program to print the element of the following list
#using while Loop:
#[1,4,9,16,25,36,49,64,81,100]]
i = 1
while i <= 10:
    print(i*i)
    i = i + 1

#Search for a Number x in this tuple using while loop:
#(1,4,9,16,25,36,49,64,81,100)
numbers = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number to search in the tuple: "))
i = 0
while i < len(numbers):
    if numbers[i] == x:
        print(x, "found in the tuple at index", i)
        break
    i = i + 1
else:
    print(x, "not found in the tuple")
    