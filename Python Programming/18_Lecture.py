# Problem 1: Rectangle Class
# Requirement: Create a class Rectangle with length and width. Create methods 
# for Area and Perimeter.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# --- Usage Example ---
# Create an object with length 10 and width 5
length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))
rect = Rectangle(length, width)


print(f"Area: {rect.calculate_area()}")
print(f"Perimeter: {rect.calculate_perimeter()}")

# Problem 2: Employee Class (Access Modifiers)
# Requirement: Create an Employee class with public, protected, and private 
# variables. Access the private bonus using a method.

# Public: Accessible everywhere (self.name).
# Protected: Prefixed with _ (self._department). Conventionally for internal use.
# Private: Prefixed with __ (self.__bonus). Cannot be accessed directly from 
# outside the class.

class Employee:
    def __init__(self, name, department, bonus):
        self.name = name             # Public variable
        self._department = department # Protected variable
        self.__bonus = bonus          # Private variable

    # Public method to access the private variable securely
    def get_bonus(self):
        return self.__bonus

# --- Usage Example ---
emp = Employee("John Doe", "IT", 5000)

print(f"Name (Public): {emp.name}")
print(f"Department (Protected): {emp._department}")

# print(emp.__bonus)  # <--- This would cause an error if uncommented!

# Correct way to access private bonus using the method
print(f"Bonus (Private, accessed via method): {emp.get_bonus()}")

# Problem 3: Account Class
# Requirement: Create an Account class with balance and account_no. Create 
# methods for Debit, Credit, and printing the balance.

class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def credit(self, amount):
        # Add money to the account
        self.balance += amount
        print(f"Credited {amount}. New Balance is updated.")

    def debit(self, amount):
        # Subtract money (check if sufficient funds exist first)
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debited {amount}. New Balance is updated.")
        else:
            print("Insufficient balance for this transaction.")

    def print_balance(self):
        print(f"Account No: {self.account_no} | Current Balance: {self.balance}")

# --- Usage Example ---
# Create account 12345 with 1000 initial balance
my_acc = Account(12345, 1000)

my_acc.credit(500)        # Add 500
my_acc.debit(200)         # Remove 200
my_acc.print_balance()    # Show final total