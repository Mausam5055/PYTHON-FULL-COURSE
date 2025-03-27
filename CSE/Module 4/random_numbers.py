import random
print(random.randrange(10))           # Returns a random number from 0 to 9
print(random.randrange(10, 20))       # Returns a random number from 10 to 19
print(random.randrange(100, 200, 2))  # Returns a random even number between 100 and 200
print(random.random())                # Returns a random float between 0 and 1
print(random.uniform(1, 10))          # Returns a random float between 1 and 10
print(random.randint(10, 20))         # Returns a random integer between 10 and 20 (both inclusive)
print(random.choice([1, 2, 3, 4, 5])) # Returns a random element from the given list
print(random.choice("VITBHOPAL"))
