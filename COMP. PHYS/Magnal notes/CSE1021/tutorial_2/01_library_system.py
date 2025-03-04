# Library Borrowing System in Python

# Predefined valid library IDs and available books
valid_ids = ["ID123", "ID456", "ID789"]
available_books = {
    "Book A": 3,  # 3 copies available
    "Book B": 2,  # 2 copies available
    "Book C": 0   # Out of stock
}

def display_books():
    print("\nAvailable books:")
    for book, stock in available_books.items():
        status = f"In stock ({stock} copies)" if stock > 0 else "Out of stock"
        print(f"- {book}: {status}")

def borrow_book():
    while True:
        display_books()
        selected_book = input("\nEnter the name of the book you want to borrow: ").strip()

        if selected_book in available_books:
            if available_books[selected_book] > 0:
                available_books[selected_book] -= 1
                print(f"\nSuccess! You borrowed '{selected_book}'.")
                break
            else:
                print(f"\nSorry, '{selected_book}' is currently out of stock. Please select another book.")
        else:
            print("\nInvalid book name. Please select a valid book.")

def library_borrowing_system():
    print("Welcome to the Library Borrowing System!\n")

    # Step 1: Input library ID
    library_id = input("Enter your library ID: ").strip()

    # Step 2: Validate library ID
    if library_id in valid_ids:
        print("\nLibrary ID validated successfully!")

        # Step 3: Display available books and borrow
        borrow_book()
    else:
        print("\nAccess denied! Invalid library ID.")

    print("\nThank you for using the Library Borrowing System!")

# Run the system
if __name__ == "__main__":
    library_borrowing_system()
