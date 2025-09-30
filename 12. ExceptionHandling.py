# 🔹 1. What is an Exception?
# --> An exception is an error that occurs during the execution of a program. When Python encounters an error, it stops the program and raises an exception.


# ***** ***** ***** 🔹 2. Common Exception Types ***** ***** ***** 
# Exception	            Description
# ZeroDivisionError	    Division by zero
# ValueError	        Invalid value (e.g., converting a letter to int)
# TypeError	            Mismatched data types
# FileNotFoundError	    File not found
# IndexError	        List index out of range
# KeyError	            Dictionary key not found
# NameError	            Variable not defined
# AttributeError	    Attribute not found

# 🔹 ***** ***** ***** 3. Basic Syntax ***** ***** ***** 
'''
try:
    # Code that may raise an exception
except SomeException:
    # Code that runs if the exception occurs
'''

# Example:
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input. Please enter a number.")




# ***** ***** ***** 🔹 4. else Block ***** ***** ***** 
# Runs only if no exception occurs in the try block.
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("That’s not a number!")
else:
    print(f"Square is {value * value}")



# ***** ***** ***** 🔹 5. finally Block ***** ***** ***** 
# Runs no matter what – used for cleanup operations.
try:
    f = open("file.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing the file (if it was opened)")
    try:
        f.close()
    except:
        pass



# ***** ***** ***** 🔹 6. Catching Multiple Exceptions ***** ***** ***** 
# You can catch multiple exceptions in one line or separately:
# Multiple except blocks
try:
    num = int("abc")
except ValueError:
    print("Value error!")
except TypeError:
    print("Type error!")


# Single except block
try:
    num = int("abc")
except (ValueError, TypeError):
    print("An error occurred.")




# ***** ***** ***** 🔹 7. Accessing Exception Details ***** ***** ***** 
# Use as keyword to get the error message.
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")





# ***** ***** ***** 🔹 8. Raising Exceptions Manually – raise ***** ***** ***** 
# You can trigger exceptions using raise.
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age is {age}")

check_age(-5)  # Raises ValueError




# ***** ***** ***** 🔹 9. Custom Exceptions ***** ***** ***** 
# Define your own exception classes by extending Exception.
class CustomError(Exception):
    pass

def test(value):
    if value == "error":
        raise CustomError("Custom error triggered!")

try:
    test("error")
except CustomError as e:
    print(e)



# ***** ***** ***** 🔹 10. Best Practices ***** ***** ***** 
# Be specific with exceptions (avoid catching all with except:).
# Always clean up resources (files, connections) with finally or with.
# Use custom exceptions to clearly define application-specific errors.
# Avoid silencing errors without logging or handling.




# ***** ***** ***** ✅ Real Example: File Reader with Exception Handling ***** ***** ***** 
filename = input("Enter filename: ")

try:
    with open(filename, "r") as f:
        content = f.read()
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("Permission denied.")
else:
    print("File content:")
    print(content)
finally:
    print("Execution complete.")


