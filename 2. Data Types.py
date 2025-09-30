


# ************ ************ ************ 1. Numbers ************ ************ ************ ************
a= 10
b = -2
print(type(b))          # OP - <class 'int'>
print(f'a: {a}, b:{b}')
print(a-b)              # 12 because 10 - (-2) evaluated


# Numbers in Differenct formats
c = 0b1010 		    # Binary (10 in decimal)
d = 0o12    		# Octal (10 in decimal)
e = 0xA             # Hexadecimal (10 in decimal)
print(f'c:{c} d:{d} e:{e} ')


# d
# print(type(d))        - error in JS undefined here error d is not defined.



# b) Floating-Point (float)
# •	Represents real numbers (with decimal points).
# •	Can also use scientific notation.
f1 = 3.14
f2 = -2.5
f3 = 1.23e5  # 1.23 × 10⁵ = 123000.0
print(f1, " ", f2, " ", f3)



# c) Complex Numbers (complex)
# •	Represented as a + bj where a is the real part and b is the imaginary part.
c1 = 3 + 4j
c2 = complex(2, -1)  # 2 - 1j

print(c1)
print(c2)


# ************ ************ ************ 2. Boolean ************ ************ ************ ************
is_true = 1< 2
is_false = 1>2

print(is_true, is_false)

is_true1 = True
is_false1 = False


# ************ ************ ************ 1. String ************ ************ ************ ************
# IMP Point - Strings are immutable, so all methods return a new string.

# Declaration
str = "YaSh Mahamuni"
str_multi_line = '''    Hello
    Yash'''

# Deletion
str2 = 'yyy'
print(str2)
del str2
# print(str2)     # Error because string is deleted already

# String Methods - String is immutable in Python so each method return new string
'''
str.split(sep)
str.join(iterable)
str.replace(old, new)
str.find(sub)
str.count(sub)
str.startswith(prefix)
str.endswith(suffix)
str.isalpha()
str.isdigit()
str.isalnum()
'''

print(str_multi_line)
print(str.lower())
print(str.upper())
print(str.capitalize())     # Only first letter capitalize others are at lower case
print(str.title())          # each starting letter of word is capitalise other are lower case
print(str.strip())          # Remove trailing on leading spaces


#  Some Important methods which return part of string
split = str.split(' ')      # Splits into a list by separator
print(f'\'Split Mehtod\' : Split STR using as seperator \"space\" : {split}')

replace = str.replace('h','$')
print(f'\'Replace Mehtod\' : replaced h with $ {replace}')

find = str.find('a')
print(f'\'find Mehtod\' : position of a in STR is : {find}')

count = str.count('a')
print(f'\'count Mehtod\' : count of a in STR : {count}')

# Info Methods in String - Methods which provide information about String
startwith = str.startswith('a')
print(f'startswith Method : return boolean value by checking prefix : {startwith}')

endwith = str.endswith('i')
print(f'endswith Method : return boolean value by checking sufix(ending) : {endwith}')

isalpha = str.isalpha()     # Return True if the string is an alphabetic string, False otherwise. A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.
print(f'isalpha Method : return boolean value, true if string is alphabetic : {isalpha}')


# isdigit() --- Return true for only positive digit number false for everything else like 1.2, -1 
num = '1'
num2 = 'y'
num3 = '1.22'
isdigit = num.isdigit()
isdigit2 = num2.isdigit()
isdigit3 = num3.isdigit()
print(f"isdigit Method : true if string is number :- for num = \'1\' : {isdigit} \n for num2 =\'2y\' :{isdigit2} \n for num3 = \'1.22\' : {isdigit3}")

# str.isalnum() --- Return True if the string is an alpha-numeric string, False otherwise.
# A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.
print('1'.isalnum())        # - True
print('-1'.isalnum())       # - False due to negative sign
print('1.22'.isalnum())     # - False due to factorial 
print('y'.isalnum())        # - True convrting character to ascii value


# Tobe
join = str.join('$%&')
print(join)