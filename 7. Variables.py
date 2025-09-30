# Variables and Assignment
# 1. A variable is a named reference to a value stored in memory.
# 2. It acts as a container for data that can be accessed and modified.


x = 10       		# x is a variable storing the integer 10
name = "Alice"  	# name stores a string


# Variable Assignment - Python uses = to assign values to variables.
# Single Assignment		
x = 10
# Multiple Assignment		
x, y, z = 10, 20, 30  		# x=10, y=20, z=30
# Chained Assignment		
a = b = c = 100  		# All variables refer to the same value (100)
# Swapping Variables		
x, y = 10, 20	
x, y = y, x 	# Now x=20, y=10 (swapped)

# Checking Variable Type
# Use type() to check a variable's data type:		x = 3.14
print(type(x))  		# Output: <class 'float'>



# *********** Variable Scope *********** 
# Variables have different scopes (where they can be accessed):
# Scope	    Definition	            Example
# Local	    Inside a function	    def foo(): x = 10
# Global	Outside functions	    x = 10 (at the top level)
# Nonlocal  In nested functions	    nonlocal x (Python 3+)

x = 10  		# Global variable
def my_func():
    y = 20  # Local variable
    print(x)  # Can access global x
my_func()
# print(y)      #❌ Error (y is local to my_func)

# *********** Modifying Global Variables Inside a Function
# Use the global keyword:
def change_x ():
    global x
    x = 20  		# Modifies the global x
change_x ()
print(x)  		# Output: 20


# ************ Constants (Convention)
# Python does not enforce constants, but uppercase names are used by convention.
PI = 3.14159  		# Treated as a constant (but can still be modified)

# ************ Deleting Variables
# Use del to remove a variable:	
x = 10
del x  		# x no longer exists		
# print(x)  # ❌ Error: NameError


# Summary Table
# Concept	            Example	            Notes
# Variable Assignment	x = 10	            Stores value in x
# Multiple Assignment	x, y = 1, 2	        Assigns multiple variables at once
# Dynamic Typing	    x=10; x="Hi"	    Variables can change type
# Global Variable	    global x	        Modifies a global variable inside a function
# Constant(Convention)	PI = 3.14	        UPPER_CASE indicates a constant
# Deleting Variables	del x	            Removes x from memory
