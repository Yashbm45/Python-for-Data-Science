
#  *************** ************ ***************** Printing in Python
# Single Line Print
print("Hello DS")

# Multiline Print
print(
"""hello Yash
How are you""")

# Advance 
# Basic Syntax: - 	print (*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# •	*Objects: Values to print (can be multiple, separated by commas).
# •	sep: Separator between objects (default: space ' ').
# •	end: What to print at the end (default: newline '\n').\
# •	file: Where to print (default: sys.stdout).
# •	flush: Whether to forcibly flush the output (default: False).
 
print(1,2,3,4,5,sep='$\n', end='$') 
print('\n')
print('roo..')


# Progress bar
import time
for i in range (10):
    print (f"\rProgress: {i+1}/10",end="")
    time.sleep(0.5)
print("\nDone!")


"""
# *************** ************ ***************** Wildcards
print('Hello Yash... is\'n it your\'s')

# Raw Path Printing
print(r"Pandas\amazon.csv")



# *************** ************ ***************** format printing 
# 1 - string interpolation
name = "yash" 
age = 24
print(f'hello {name} your age is {age}');

# 2. - format() method - order is critical here
print('hello {} your age is {}'.format(name,age))

# 3. Old style
print('Hello %s your age is %d'%(name,age))


# Flush - Immediate Printing
import time
time.sleep(5)
print ("Starting...", end="", flush=True)
time.sleep(2) # Simulate delay
print("Done!")
"""