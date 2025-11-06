# Q.1. Write a python Program to demonstrate various dictionary operations.
# Q.2.Write a python program to demonstrate various operations on tuples.

# Q.3.Write a program that uses a dictionary that contains user names and 
# passwords create by the user. The program should read the user input to enter 
# their username and password. If the username is not in the dictionary, the 
# program should indicate that the person is ‘Not a valid user’.
# If the username is in the dictionary, but the user does not enter the right 
# password, the program should say that the ‘Password is in valid’.


# SUBMITTED BY: Mausam Kar 
# REG NO: 24BAI10284
# DATE: 13-04-2024
# 1. Demonstrate various dictionary operations
def dictionary_operations():
    # Creating a dictionary
    my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    print("Original Dictionary:", my_dict)

    # Accessing elements
    print("Name:", my_dict['name'])

    # Adding an element
    my_dict['email'] = 'alice@example.com'
    print("Updated Dictionary:", my_dict)

    # Updating an element
    my_dict['age'] = 26
    print("Updated Dictionary:", my_dict)

    # Removing an element
    del my_dict['city']
    print("Updated Dictionary:", my_dict)
dictionary_operations()


# 2. Demonstrate various operations on tuples
def tuple_operations():
    # Creating a tuple
    my_tuple = (1, 2, 3, 4, 5)
    print("Original Tuple:", my_tuple)

    # Accessing elements
    print("First Element:", my_tuple[0])

    # Slicing a tuple
    print("Sliced Tuple (1 to 3):", my_tuple[1:4])

    # Concatenating tuples
    new_tuple = my_tuple + (6, 7, 8)
    print("Concatenated Tuple:", new_tuple)

    # Tuple length
    print("Length of Tuple:", len(my_tuple))
tuple_operations()

# 3. User authentication using dictionary
def user_authentication():
    # Creating a dictionary of usernames and passwords
    user_db = {
        'user1': 'password1',
        'user2': 'password2',
        'user3': 'password3'
    }
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in user_db:
        if user_db[username] == password:
            print("Login successful!")
        else:
            print("Password is incorrect.")
    else:
        print("Not a valid user.")
user_authentication()


# END OF 11_Task_7.py