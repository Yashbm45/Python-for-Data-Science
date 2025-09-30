# A set is an unordered, mutable collection of unique items.
# 1. No duplicate values allowed
# 2. Unordered (no indexing)
# 3. Mutable (you can add or remove elements)
# Useful for set operations (union, intersection, etc.)


# ********** ********** ********** 1. Creation ********** ********** **********
# Creates a set from any iterable (removes duplicates).
s = set([1, 2, 2])      # ---→ {1, 2}	
print(s)

# Creates a set using curly braces (only for non-empty sets).
s2 = {1,2,3,3,4,5,5,5,5}
print(s2)

# Creates an empty set (⚠ {} creates a dict).	
set3 = set()
print(set3)



# ********** ********** ********** 2. Deletion / Removal ********** ********** **********
# 1. remove(x)	Removes element x; raises KeyError if not found.	
s.remove(2)
# discard(x)	Removes element x if present; no error if not found.	
s.discard(2)
# pop()	Removes and returns an arbitrary element; raises KeyError if empty.	
s.pop()
# clear()	Removes all elements from the set.	
s.clear()



# ********** ********** ********** 3. Update / Manipulation ********** ********** **********
# add(x)	        Adds element x to the set.	
s.add(5)

# update(*others)	Adds all elements from other iterables.	
s.update([6, 7])

# intersection_update(*others)	        Keeps only elements present in all sets.	
s.intersection_update(s2)

# difference_update(*others)	        Removes elements found in the others.	
s.difference_update(s2)

# symmetric_difference_update(other)	Updates set to elements in either, but not both.	
s.symmetric_difference_update(s2)



# ********** ********** ********** 4. Query / Information ********** ********** **********
# len(s)	Returns number of elements in the set.	
len(s)

# in	    Checks if element exists.	
3 in s

# not in	Checks if element does not exist.	
10 not in s

# isdisjoint(other)	Returns True if no common elements.	
s.isdisjoint(s2)

# issubset(other)	Returns True if all elements of this set(s) are in other (s2).	
s.issubset(s2)

# issuperset(other)	Returns True if this set contains (s) all elements of other (s2).	
s.issuperset(s2)



# ********** ********** ********** 5. Return New Set (No change to original) ********** ********** **********
# copy()	            Returns a shallow copy of the set.	
s2 = s.copy()

# union(*others)    	Returns all unique elements from all sets.	
s.union(s2)

# intersection(*others)	Returns elements common to all sets.	
s.intersection(s2)

# difference(*others)	        Returns elements in s but not in others.	
s.difference(s2)

# symmetric_difference(other)	Returns elements in either set, but not both.	
s.symmetric_difference(s2)

# ******************** Bonus: Set Operations (Operator Shortcuts) ********************
a = {1, 2, 3}
b = {3, 4, 5}

'''
a | b     # Union → {1, 2, 3, 4, 5}
a & b     # Intersection → {3}
a - b     # Difference → {1, 2}
a ^ b     # Symmetric Difference → {1, 2, 4, 5}
'''

# Example
s = {1, 2, 3}
s.add(4)               # {1, 2, 3, 4}
s.remove(2)            # {1, 3, 4}

s2 = {3, 5}
s.union(s2)            # {1, 3, 4, 5}
s.intersection(s2)     # {3}
s.difference(s2)                # {1,4}     -- elements in set s which are not in set s2
s.symmetric_difference(s2)      # {1,4,5}   -- Diffenet elements between two sets

'''
Set Methods (with Description + Example)
Method	            Description	Example
add(x)	            Adds element x to the set.	s.add(4)
clear()	            Removes all elements.	s.clear()
copy()	            Returns a shallow copy.	s2 = s.copy()
difference(*others)	Returns elements in set s but not in others.	s.difference(s2)
difference_update(*others)	Removes elements found in others from set.	s.difference_update(s2)
discard(x)	        Removes x if present (no error if not found).	s.discard(2)
intersection(*others)	    Returns common elements.	s.intersection(s2)
intersection_update(*others)	Keeps only common elements.	s.intersection_update(s2)
isdisjoint(other)	        Returns True if sets have no elements in common.	s.isdisjoint(s2)
issubset(other)	            Returns True if set is a subset.	s.issubset(s2)
issuperset(other)	        Returns True if set is a superset.	s.issuperset(s2)
pop()	                    Removes and returns an arbitrary element.	s.pop()
remove(x)	                Removes x (raises KeyError if not found).	s.remove(2)
symmetric_difference(other)	Returns elements in either set but not both.	s.symmetric_difference(s2)
symmetric_difference_update(other)	Updates set with symmetric difference.	s.symmetric_difference_update(s2)
union(*others)	Returns all unique elements from all sets.	s.union(s2)
update(*others)	Adds all elements from others to the set.	s.update(s2)


# Summary
Feature	            Supported in Set
Mutable	            ✅
Unordered	        ✅
Unique elements	    ✅
Indexing	        ❌
Duplicates	        ❌
Iterable	        ✅
Supports Set Theory	✅
'''

# FROZENSET
# A frozenset is a built-in Python data type that represents an immutable version of a set. 
# Like regular sets, frozensets are unordered collections of unique elements, but once created, their contents cannot be changed (i.e., no adding or removing elements).

# 🔑 Key Characteristics:
# 1. Immutable: You cannot modify it after creation.
# 2. Hashable: Can be used as a key in dictionaries or stored in sets.
# 3. Elements must be hashable (like with normal sets).


# Create a regular set
s = set([1, 2, 3])

# Create a frozenset
fs = frozenset([1, 2, 3, 4])

print(fs)  # Output: frozenset({1, 2, 3, 4})

# Attempting to modify frozenset will raise an error
fs.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'

# ✅ Use Cases:
# 1. As dictionary keys or set elements
# 2. When you want a set that must remain constant (e.g., for caching, or membership tests without risk of modification)

# Difference between set and frozen set
# Feature	                set	                                    frozenset
# Mutability	            Mutable (can be changed)	            Immutable (cannot be changed)
# Hashable	                Not hashable (cannot be dict keys)	    Hashable (can be used as dict keys or set elements)
# Can Add/Remove Elements	Yes (add(), remove())	                No
# Syntax	                set([1, 2, 3])	                        frozenset([1, 2, 3])
# Use as Dictionary Key	    ❌ Not allowed	                       ✅ Allowed
# Use in Set of Sets	    ❌ Not allowed	                       ✅ Allowed
