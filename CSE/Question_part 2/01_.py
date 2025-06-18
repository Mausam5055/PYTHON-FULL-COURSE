# Write a Python program to generate a password containing 
# letter, number, and special character. The program will take
#  number of characters as input to generate the password.

import random

def generate_password(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%^&*()"
    all_chars = letters + digits + special

    password = ""
    for i in range(length):
        password += random.choice(all_chars)

    print("Password:", password)

# Example
length = int(input("Enter password length: "))
generate_password(length)
