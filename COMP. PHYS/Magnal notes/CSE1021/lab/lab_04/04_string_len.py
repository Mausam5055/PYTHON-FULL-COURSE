while True:
    user_input = input("Enter a string (or type 'Quit' to stop): ")

    if user_input.lower().strip() == 'quit':
        print("Exiting the program.")
        break  
    
    string_length = len(user_input)
    print(f"The length of the string is: {string_length}")
