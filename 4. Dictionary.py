
# Dictinary -  A dictionary is an unordered, mutable, and indexed collection of key-value pairs.
# Keys must be immutable (e.g., strings, numbers, tuples)
# Values can be any type
# Keys are unique


# Example dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

# ********** ********** ********** Creating a Dictionary ********** ********** ********** 
# ********** 1.Using curly braces **********
d1 = {"a": 1, "b": 2}

# ********** 2.Using dict() constructor **********
d2 = dict(a=1, b=2)

# ********** 3.Creating from list of tuples **********
d3 = dict([("a", 1), ("b", 2)])

# ********** 4.Empty dictionary **********
empty = {}

print(f'Creating list in Python \nd1 : {d1} \nd2 : {d2} \nd3 : {d3} \nEmpty : {empty}')

'''
🧩 Dictionary Methods (with Explanation + Example)
Method	                Description	Example
clear()	                Removes all items from the dictionary.	d.clear()
copy()	                Returns a shallow copy of the dictionary.	d2 = d.copy()
fromkeys(seq, value)	Creates a new dictionary from keys in seq, with all values set to value.	dict.fromkeys(['a', 'b'], 0) → {'a': 0, 'b': 0}
get(key[, default])	    Returns the value for key if present, else default.	d.get('age', 'N/A')
items()	                Returns a view of dictionary’s (key, value) pairs.	for k, v in d.items():
keys()	                Returns a view of dictionary’s keys.	list(d.keys())
pop(key[, default])	    Removes key and returns its value, or default if not found.	d.pop('name')
popitem()	            Removes and returns the last inserted (key, value) pair.	d.popitem()
setdefault(key[, default])	Returns value of key, sets it to default if not present.	d.setdefault('country', 'USA')
update([other])	        Updates the dictionary with key-value pairs from another dict or iterable.	d.update({'age': 31})
values()	            Returns a view of dictionary’s values.	list(d.values())
'''
# ********** ********** ********** Looping Through a Dictionary ********** ********** **********
for key in d1:
    print(key, d1[key])

# Or using items()
for key, value in d1.items():
    print(f"{key}: {value}")

# ********** ********** ********** Common Operations ********** ********** ********** 
# ********** Accessing values
print(d2["a"])  # Alice

# ********** Adding or modifying
d2["a"] = 31
d2["city"] ='pune'

# ********** Deleting a key
del d2["city"]

# ********** Checking if key exists
if "age" in d2:
    print("Age is present")


# ********** ********** ********** Dictionary Comprehension ********** ********** **********
# ********** ********** Squares of numbers
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


'''
# ********** ********** ********** Summary Table of All Methods ********** ********** ********** 
Method	        Use for
clear()	        Remove all items
copy()	        Shallow copy
fromkeys()	    Create new dict from keys
get()	        Safe access to value
items()	        Key-value pairs view
keys()	        Keys view
pop()	        Remove key and return value
popitem()	    Remove last inserted item
setdefault()	Get or set default for a key
update()	    Merge another dict
values()	    Values view
'''