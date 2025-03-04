# -------PROJECT 1: SNAKE, WATER, GUN GAME-------

# We all have played snake, water gun game in our childhood. 
# If you haven’t, google the rules of this game and write a 
# python program capable of playing this game with the user.

#let in the game : 1 = for snake
                #    2 = for water
                #    3 = for gun 

# Here's how you can generate a random number out of 1, -1, and 0 in Python:

# python
# Copy code
# import random

# random_number = random.choice([1, -1, 0])
# print(random_number)
# Running this code will give you a random selection from the list [1, -1, 0]

import random
computer = random.choice([1,-1,0])

youstr = input("Enter your choice: ")     #youstr = variable having string datatype
youDict = {"s":1,"w":-1,"g":0 }                #we created a dictionary
reverseDict ={1:"Snake",-1:"Water",0:"Gun"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and compute

print(f"You coose{reverseDict[you]}\nComputer choose{reverseDict[computer]}")

if(computer == you):
    print("Its a draw")
                                           #WE USED IF AND ELIF INSIDE ANOTHER IF ELSE STATEMENT
else:                                      #THIS IS CALLED A LADDER STATEMENT IN IF ELSE CONDITION
    if(computer == -1 and you == 1):       
        print("You win!")

    elif(computer == -1 and you == 0): 
        print("You loose!")    

    elif(computer == 1 and you == -1): 
        print("You loose!")  
        
    elif(computer == 1 and you == 0): 
        print("You win!")     

    elif(computer == 0 and you == -1): 
        print("You win!")  
    
    elif(computer == 0 and you == 1): 
        print("You loose!")          

    else:
        print("Something went wrong!")     