#write a pyrhon code to check if the student is passed or not,
#take 3 inputs , and verage should be more than or equal to 40
#for passing criteria

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))

average = (a+b+c)/3

if average >= 40:
    print("You are passed")
else:
    print("You are failed")


