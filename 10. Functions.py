
# Functions in Python are reusable blocks of code that perform a specific task. They help in breaking down complex problems into smaller pieces, making code more modular, readable, and manageable.

# ***** ***** ***** 🔹 1. Defining a Function ***** ***** *****
# Syntax
def function_name(parameters):
    """Optional docstring explaining the function"""
    # function body
    return result

# Example:
def greet(name):
    """This function greets the person passed as an argument."""
    print(f"Hello, {name}!")


# ***** ***** ***** 🔹 2. Calling a Function ***** ***** *****
# You call a function by using its name followed by parentheses:
greet("Alice")


# ***** ***** ***** 🔹 3. Parameters and Arguments ***** ***** *****
# Parameters are variables listed inside the parentheses in the function definition.
# Arguments are the values you pass to those parameters.

def add(x, y):
    return x + y

result = add(10, 5)  # 10 and 5 are arguments


# ***** ***** ***** 🔹 4. Return Statement ***** ***** *****
# A function can return a value using the return keyword.
# If no return statement is used, the function returns None.
def square(n):
    return n * n

print(square(4))  # Output: 16


# ***** ***** ***** 🔹 5. Types of Functions ***** ***** ***** 
# ***** ***** ✅ Built-in Functions
# Examples: len(), type(), print(), range(), etc.

# ***** ***** ✅ User-defined Functions
# Created using the def keyword (as shown above).
def name():
    print('I am User Defined Function...')

name()




# ***** ***** ***** 🔹 6. Default Parameter Values ***** ***** ***** 
# You can assign default values to parameters:
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Hello, Guest!
greet("Emily")  # Hello, Emily!




# ***** ***** ***** 🔹 7. Keyword Arguments ***** ***** ***** 
# You can pass arguments by name, making the order irrelevant.
def divide(x, y):
    return x / y

print(divide(y=5, x=10))  # Output: 2.0




# ***** ***** ***** 🔹 8. Variable-length Arguments ***** ***** ***** 
# *args (Non-keyword variable-length arguments):    Treated as list
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # Output: 10


# **kwargs (Keyword variable-length arguments):     treated as dict
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30)



# ***** ***** ***** 🔹 9. Lambda Functions (Anonymous Functions) ***** ***** ***** 
# A short way to write simple functions.
square = lambda x: x * x
print(square(5))  # Output: 25

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]




# ***** ***** ***** 🔹 10. Nested Functions ***** ***** ***** 
# Functions defined inside another function.
def outer():
    print('Outer function top...')
    def inner():
        print("Inner function")
    inner()
    print('Outside function below inner...')

outer()



# 🔹 11. Recursion
# A function that calls itself.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(3))  # Output: 120




# ***** ***** ***** 🔹 12. Scope and Lifetime of Variables ***** ***** ***** 
# Local Scope: Variables declared inside a function.
# Global Scope: Variables declared outside all functions.
# Use global keyword to modify global variables inside functions.
x = 10

def change():
    global x
    x = 20





# Scope rules
global_var = 10

def outer():
    outer_var = 20
    def inner():
        nonlocal outer_var    # Access outer scope
        global global_var     # Access global scope
        outer_var += 1
        global_var += 1
    return inner

# Closures
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

# Function attributes
def greet(name):
    """Greet someone."""
    return f'Hello {name}!'

greet.short_desc = 'Greeting function'
print(greet.__doc__)      # Access docstring
print(greet.__name__)     # Function name