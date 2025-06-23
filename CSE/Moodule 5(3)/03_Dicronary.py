# A dictionary in Python is a built-in data type that stores key-value pairs. It's unordered, mutable, and indexed by keys, which must be unique and immutable 
# (like strings, numbers, or tuples).

# Basic example
my_dict = {
    "name": "Mausam",
    "age": 21,
    "language": "Python"
}

#accesing an elemt in dict:
print(my_dict["age"])
my_dict["language"]


#updating values: 
my_dict["city"] = "Agartala"         # Add new key-value pair
my_dict["age"] = 22                  # Update existing value


#deleting items in dictonary 
my_dict.pop("language")              # Removes 'language' key
del my_dict["city"]                  # Also removes 'city'
my_dict.clear()                      # Empties the dictionary

#dictonary Methods :

my_dict.keys()      # Returns all keys
my_dict.values()     # Returns all values
my_dict.items()      # Returns all key-value pairs


len(my_dict)
any(my_dict) #It returns True if even one key in a dictionary has a Boolean value of True.
sorted(my_dict)#It returns a sorted sequence of the keys in the dictionary.

