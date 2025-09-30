




# 🔟 Python Practice Tasks – OOP + Exception Handling



# ✅ 1. Bank Account Management System
# Topics: Class, Inheritance, Encapsulation, Custom Exceptions
# Task: Create a BankAccount class with attributes: account_number, balance.
# Add methods: deposit(), withdraw(), get_balance().
# Raise a custom exception InsufficientFundsError when withdrawal > balance.



# Custom Exception
class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient balance for this transaction."):
        self.message = message
        super().__init__(self.message)

# BankAccount Class
class BankAccount:
    def __init__(self, acc_num, balance=0):
        self.acc_num = acc_num
        self.__balance = balance  # Encapsulated

    def deposit(self, amt):
        if amt <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amt
        print(f"Successfully deposited {amt} to account {self.acc_num}.")

    def withdraw(self, amt):
        if amt <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amt > self.__balance:
            raise InsufficientFundsError(f"Attempted to withdraw {amt}, but only {self.__balance} available.")
        self.__balance -= amt
        print(f"Successfully withdrew {amt} from account {self.acc_num}.")

    def get_balance(self):
        return self.__balance


try:
    ro = BankAccount(1234, 1000)
    ro.deposit(500)
    print("Current Balance:", ro.get_balance())
    ro.withdraw(2000)  # This will raise InsufficientFundsError
except ValueError as ve:
    print("Value Error:", ve)
except InsufficientFundsError as ife:
    print("Custom Error:", ife)
except Exception as e:
    print("Unexpected error:", e)







# ✅ 2. Student Gradebook System
# Topics: Class, Object, List, Exception Handling
# Task: Create a Student class with attributes: name, marks (list).
# Method to calculate average, and display result.
# Raise a ValueError if marks are not between 0-100.







# ✅ 3. Library Book Manager

# Topics: Classes, Object Storage, File Handling (optional)

# Task:

# Create a Book class with title, author, and ISBN.

# Create a Library class to manage books (add_book(), remove_book(), search()).

# Handle errors like trying to remove/search a non-existent book.

# ✅ 4. E-Commerce Cart

# Topics: OOP, Class Composition, Error Handling

# Task:

# Create Product, Cart, and User classes.

# Add add_to_cart() and checkout() methods.

# Raise exceptions when:

# Adding a product that’s out of stock.

# Checking out an empty cart.

# ✅ 5. Custom Calculator with Input Validation

# Topics: Class, Exception Handling, Input Checking

# Task:

# Build a Calculator class with methods: add(), subtract(), multiply(), divide().

# Raise:

# ZeroDivisionError for divide by zero.

# TypeError if inputs aren't numbers.

# ✅ 6. File Analyzer Tool

# Topics: OOP, File Handling, Exception Handling

# Task:

# Create a FileAnalyzer class with methods to:

# Count words, characters, and lines in a file.

# Handle:

# FileNotFoundError

# PermissionError

# ✅ 7. Vehicle Rental System

# Topics: Inheritance, Polymorphism, Exception Handling

# Task:

# Create base class Vehicle, and derived classes Car, Bike.

# Method: rent(), return_vehicle()

# Raise exceptions if:

# A vehicle is rented out already.

# An invalid vehicle type is accessed.

# ✅ 8. Online Exam Portal

# Topics: OOP, List Handling, Exception Handling

# Task:

# Create a Question class with question_text, options, correct_option.

# Create an Exam class to administer questions.

# Handle:

# IndexError when user chooses an invalid option.

# Track score and show result at the end.

# ✅ 9. Contact Manager App

# Topics: OOP, List, CRUD, Error Handling

# Task:

# Contact class with name, email, phone.

# ContactManager class with methods to add, delete, and search.

# Raise exceptions if:

# Duplicate contact is added.

# Contact not found during search or delete.

# ✅ 10. Shape Area Calculator (Using Polymorphism)

# Topics: Inheritance, Polymorphism, Abstract Methods

# Task:

# Base class Shape with abstract method area().

# Derived classes: Circle, Rectangle, Triangle

# Implement area() in each and handle invalid inputs (e.g., negative values).
