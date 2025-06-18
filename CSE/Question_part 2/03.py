# Write a function that takes a sentence as input, that calculates 
# number of letters and number of digits.

def count_letters_digits(sentence):
    letters = 0
    digits = 0

    for char in sentence:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            letters += 1
        elif '0' <= char <= '9':
            digits += 1

    print("Letters:", letters)
    print("Digits:", digits)

# Example
text = input("Enter a sentence: ")
count_letters_digits(text)
