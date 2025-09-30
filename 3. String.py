# String creation
name = 'Alice'        # Single quotes
greeting = "Hello"    # Double quotes
multiline = '''This is a
multiline string'''   # Triple quotes

# String concatenation
full_name = 'John' + ' ' + 'Doe'

# String repetition
stars = '*' * 3  # '***'

# String length
len(name)        # 5

# Access characters
first = name[0]  # 'A'
last = name[-1]  # 'e'

# Slicing
substr = name[1:3]   # 'li'
reversed = name[::-1]  # 'ecilA'


text = '  Hello, World!  '

# Case methods
text.upper()      # 'HELLO, WORLD!'
text.lower()      # 'hello, world!'
text.title()      # 'Hello, World!'
text.capitalize() # 'Hello, world!'

# Whitespace
text.strip()      # 'Hello, World!'
text.lstrip()     # 'Hello, World!  '
text.rstrip()     # '  Hello, World!'

# Search methods
text.find('World')     # 8
text.index('World')    # 8 (raises error if not found)
text.count('l')        # 3
'World' in text        # True

# Replace
text.replace('World', 'Python')  # '  Hello, Python!  '



name = 'Alice'
age = 25

# F-strings (Python 3.6+)
f'Name: {name}, Age: {age}'     # 'Name: Alice, Age: 25'
f'{name=}, {age=}'              # "name='Alice', age=25"
f'{3.14159:.2f}'                # '3.14'

# Format method
'Name: {}, Age: {}'.format(name, age)
'Name: {n}, Age: {a}'.format(n=name, a=age)


# % operator (older style)
'Name: %s, Age: %d' % (name, age)


# Common format specifiers
f'{42:08d}'     # '00000042' (padding)
f'{3.14159:8.2f}'  # '    3.14' (width.precision)
f'{42:<8d}'     # '42      ' (left align)
f'{42:>8d}'     # '      42' (right align)
f'{42:^8d}'     # '   42   ' (center)



# STRING OPERATIONS

# Splitting and joining
text = 'apple,banana,orange'
fruits = text.split(',')    # ['apple', 'banana', 'orange']
words = 'Hello World'.split()  # ['Hello', 'World']

# Join lists into string
','.join(['apple', 'banana'])  # 'apple,banana'
' '.join(['Hello', 'World'])   # 'Hello World'

# Check string properties
'hello123'.isalnum()   # True (alphanumeric)
'hello'.isalpha()      # True (alphabetic)
'123'.isdigit()        # True (digits)
'Hello'.startswith('H') # True
'World'.endswith('d')   # True


# Escape characters
print('Hello\nWorld')   # Newline
print('Tab\there')      # Tab
print('Path: C:\\Users') # Backslash