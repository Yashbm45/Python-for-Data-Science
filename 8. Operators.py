# Operators
# Operators in Python are symbols that perform operations on variables and values. 


# ***** ***** 1. Arithmetic Operators ***** *****
# Used for mathematical calculations.
a = 10
b = 5
print('Arithmetic Operators.......')
# Addition
print(f'a + b = {a + b}')
# Subtraction
print(f'a - b = {a - b}')

# Multiplication --	“*”
print(f'a * b = {a * b}')

# Division (float) -- “/”
print(f'a / b = {a / b}')  # 10 / 5 = 2.0

# Floor Division (integer) -- “ // “	-- 	10 // 3 → 3
print(f'10 // 3 = {10 // 3}')

# Modulus (remainder) -- “%”	        --	10 % 3 → 1
print(f'10 % 3 = {10 % 3}')

# Exponentiation (power) -- “**” 	    -- 	2 ** 3 → 8
print(f'2 ** 3 = {2 ** 3}')


# ***** ***** 2. Comparison (Relational) Operators ***** ***** 
# Used to compare values and return True or False.
print('Comaparision Operators.......')
# 1. Equal to 			== 
print(f'5 == 5 --> {5 == 5}')

# Not equal to			!=
print(f'5 != 5 --> {5 != 5}')

# Greater than			>
print(f'5 > 6 --> {5 > 6}')

# Less than			<
print(f'5 < 6 --> {5 < 6}')

# Greater than or equal		>=
print(f'5 >= 6 --> {5 >= 6}')

# Less than or equal		<=
print(f'5 =< 6 --> {5 <= 6}')


# 3. ***** ***** Logical Operators ***** *****
# Used to combine conditional statements.
print('Logical Operators....')

# 1. And 	 True if both operands are true
print(True and False)

# Or 	 True if at least one operand is true
print(True or False)

# Not 	 Negates the boolean value
print(not False)


# ***** ***** 4. Assignment Operators ***** *****
# Used to assign values to variables.
# 1. = 	     Assign
a = 5

# += 	     Add and assign
a+=2
print(f'a += 2 --> {a}')


# -= 	     Subtract and assign
a-=5
print(f'a -= 5 --> {a}')
'''
*= 	 Multiply and assign
/= 	 Divide and assign
//=	 Floor divide and assign
%=	 Modulus and assign
**=	 Exponent and assign 
'''

# 5. Bitwise Operators
# Used to perform operations on binary numbers.
# Bitwise AND			 5 & 3 → 1
# Bitwise OR			 5 | 3  → 1
# Bitwise XOR			 5 ^ 3 → 6
# Bitwise NOT (inverts bits)	 ~5 → -6
# Left shift			 5 << 1 → 10
# Right shift			 5 >> 1 → 2



# 6. Membership Operators
# Used to check if a value exists in a sequence (list, tuple, str, etc.).
print('Membership Operators.....')
li = [1,2,3,4,5,6]
tuple = (1,2,3,4,5)
str = 'Yash'

# 1. IN 		 True if value exists			 "a" in ["a", "b"] → True
print(f'1 in li --> {1 in li}')

# NOT IN 	     True if value does not exist	 "c" not in "abc" → False
print(f'1 not in li --> {1 not in li}')

fruits = ["apple", "banana"]
print ("apple" in fruits)      # True
print ("mango" not in fruits)  # True

# 7. ***** ***** Identity Operators ***** ***** 
# Used to check if two variables refer to the same object (memory location).
# IS		 True if both variables are the same object
# IS NOT 	 True if both variables are not the same object
print('Identity Operators.....')
x = [1, 2]
y = [1, 2]
z = x
print(x is y)      # False (different objects)
print(x is z)      # True (same object)
print(x == y)      # True (same value)




# ***** ***** 8. Operator Precedence ***** ***** 
# Python follows a specific order when evaluating expressions (similar to math).
# () --> **	-->  ~,+,- 	--> *,/,//,% -->  +, -	--> <<, >>	-->  & 	-->  ^ 	
# --> ``	--> ==, !=, >, <, >=, <=  	-->  is, is not 	--> in, not in 	-->  not -->   and, or



# ***** ***** 9. Ternary Operator (Conditional Expression) ***** ***** 
# Shortcut for if-else in a single line.
# Syntax: value_if_true if condition else value_if_false
print('Ternary Operator.....')
x = 20
y = 10
max_val = x if x > y else y     # Returns 20
print(f'max_val = x if x > y else y : {max_val}')