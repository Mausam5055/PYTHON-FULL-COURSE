# ---------PROJECT 2 – THE PERFECT GUESS-----

# We are going to write a program that generates a random number 
# and asks the user to guess it.
# If the player’s guess is higher than the actual number, the 
# program displays “Lower  number please”. Similarly, if the 
# user’s guess is too low, the program prints “higher 
# number please” When the user guesses the correct number, the 
# program displays the  number of guesses the player used to
#  arrive at the number.

# Hint: Use the random module

import random
n = random.randint(1, 100) #we will selelct a random number b/w 1-100
a = -1
guesses = 0                #1st guess
while(a != n):  # a! = n(a not equal to n)
    guesses +=1                       #if we cant guess the no. in 1st stage then we will go for 2nd guess...and so on 
    a = int(input("Guess the number: ")) 
    if(a >n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number Please")
        guesses +=1

print(f"You have guessed the number {n} correctly in {guesses} attempts")