
#Old way of writing
# def case_trans(char):
#     upper_char = char.upper()

#     if char == upper_char :
#         char = char.lower()
#     else :
#         char = char.lower()

#     print(char)

# char = input("Enter the character : ")
# case_trans(char)

#New Way using islower

char = input("Enter a character: ")

if char.islower():
    print(f"The uppercase of {char} is {char.upper()}")
elif char.isupper():
    print(f"The lowercase of {char} is {char.lower()}")