# ***** ***** 1. Conditional Statements (Branching) ***** *****
# Used to execute code blocks based on conditions.

# ***** 1. If else
x = 10
if x == 5:
    print('X is 5')
elif x > 5:
    print('X is greater than 5...')
else:
    print ('X is less than 5...')
    
# ***** ***** 2. Loops (Iteration) ***** *****
# Used to repeat a block of code multiple times.

# ***** A. for loop
# Used to iterate over sequences like lists, tuples, strings, dictionaries, etc.
for i in range(5):
    print(i)

# You can also iterate over lists:
for item in ['apple', 'banana', 'cherry']:
    print(item)


# ***** B. while loop
# Executes as long as the condition is True.
count = 0
while count < 5:
    print(count)
    count += 1



# ***** ***** 3. Loop Control Statements ***** *****
# ***** A. break
# Terminates the loop immediately.
for i in range(10):
    if i == 5:
        break
    print(i)


# ***** B. continue
# Skips the current iteration and moves to the next one.
print('Continue Statement')
for i in range(5):
    if i == 2:
        continue
    print(i)


# ****** c. else with loops
# Executes if the loop completes normally (not interrupted by break).
print('Else with Loops')
for i in range(5):
    print(i)
else:
    print("Loop completed")



# ***** ***** 4. Comprehensions (Compact Loops) ***** *****
# List/set/dictionary comprehensions are concise ways to create collections.
squares = [x**2 for x in range(5)]   # [0, 1, 4, 9, 16]



# ***** *****  5. Function Calls ***** *****
# Python executes function definitions only when called.
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")



# 6. Exception Handling (Conditional Flow on Errors)
# Python can control flow based on whether an exception occurs.
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No error")
finally:
    print("Always runs")



# 7. Match Statement (Python 3.10+) — Structural Pattern Matching
# Used like a switch case in other languages.
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"



# Summary
# Control Flow Tool	        Description
# if, elif, else	        Conditional branching
# for, while	            Looping constructs
# break, continue	        Controlling loop execution
# try, except	            Error-based conditional flow
# def, return	            Function-based control transfer
# match (3.10+)	            Pattern-based branching

