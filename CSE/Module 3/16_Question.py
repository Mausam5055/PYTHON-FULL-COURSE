#write a function using python that accepts a 2 digit number as a 
# parameter and return text in words(Basic)

def num_to_word(n):
    for a in str(n):
        if a == "1":
            print("one", end=" ")
        elif a == "2":
            print("two", end=" ")
        elif a == "3":
            print("three", end=" ")
        elif a == "4":
            print("four", end=" ")
        elif a == "5":
            print("five", end=" ")
        elif a == "6":
            print("six", end=" ")
        elif a == "7":
            print("seven", end=" ")
        elif a == "8":
            print("eight", end=" ")
        elif a == "9":
            print("nine", end=" ")
        elif a == "0":
            print("zero", end=" ")
    print("")  # Print a newline after the number words

num_to_word(int(input("Enter a number: ")))



