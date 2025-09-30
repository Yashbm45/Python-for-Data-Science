
# A tuple is an ordered, immutable collection of items. 
# Once created, you cannot change its contents (no adding, removing, or changing elements).
# Tuples are Immutable


# ********** ********** ********** Creating Tuples ********** ********** **********
# Simple tuple
t = (1, 2, 3)

# Tuple with mixed types
t2 = (1, "hello", 3.14)

# Nested tuple
nested = (1, (2, 3), [4, 5])

# Single element tuple (note the comma!)
single = (5,)  

# Using tuple() constructor
t3 = tuple([1, 2, 3])



# ********** ********** Looping Through a Tuple ********** **********
t = (10, 20, 30)
for item in t:
    print(item)


# ********** ********** Tuple Unpacking ********** **********
t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # 1 2 3


# ********** ********** With * (extended unpacking):
a, *b = (1, 2, 3, 4)
# a = 1, b = [2, 3, 4]



'''
# ********** ********** ********** When to Use Tuples? ********** ********** **********
1. When you need a fixed collection of items.
2. As keys in dictionaries (if the tuple contains only immutable elements).
3. For faster performance than lists.



t[0] = 10       # ❌ TypeError
t.append(4)     # ❌ AttributeError

# ********** Tuple Methods **********
Tuples have only two built-in methods:
Method	    Description	Example
count(x)	Returns the number of times x appears.	(1, 2, 1, 3).count(1) → 2
index(x)	Returns the first index of value x.	(1, 2, 3).index(2) → 1

# --> Unlike lists, tuples do not support methods like append, remove, or sort.


# ********** ********** Summary ********** **********
Feature	            Supported in Tuple
Immutable	        ✅ Yes
Indexable	        ✅ Yes
Iterable	        ✅ Yes
Count elements	    ✅ count()
Find index	        ✅ index()
Add/remove items	❌ No
Sorting	            ❌ No (use sorted(t) instead)

'''