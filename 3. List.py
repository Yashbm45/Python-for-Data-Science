# List - List is mutable Sequential data type in Python which are capable of storing heterogenous type of data 
# •	Mutable, ordered collection of items (can be of different types).
# •	Enclosed in square brackets [].


# ********** ********** Declaration/ Creation ********** **********
# Empty list
my_list = []

# List of integers
numbers = [1, 2, 3, 4, 5]
li = ['9a','8b','7c']

# Mixed data types
mixed = [1, "hello", 3.14, True]

# Nested list
nested = [1, [2, 3], [4, [5, 6]]]




#  ********** ********** Deletion ********** **********
# del li2



# ********** ********** Accessing Values in list ********** **********
print(numbers)
print(numbers[0])     # First element
print(numbers[-1])    # Last element



# ********** ********** Modify elements ********** ********** 
numbers[0] = 10

# ********** Add elements  ********** 
numbers.append(6)         # Add to end
numbers.insert(2, 99)     # Insert at index 2
numbers.extend(li)	      # Appends all elements from the iterable to the list.
print(numbers)

# ********** Remove elements ********** 
numbers.remove(99)        # Remove by value
numbers.pop()             # Remove last item
numbers.pop(1)            # Remove item at index 1
li.clear()           # Remove all items from list



# ********** ********** Information Methods ********** ********** 
# ********** Length of list ********** 
len = len(numbers)

# ********** Check existence ********** 
bool = 3 in numbers

# ********** Count of Elements *********
count = numbers.count(2)
print(f'Length of list : {len} \nElement exist in list : {bool} \nCount of element(2) in list : {count}')

# ********** Index of Number ***********
ind = numbers.index(4,0,)	            # Returns the first index of item x; raises error if not found.
print(ind)



# ********** **********  List Slicing ********** ********** 
# ********** Slicing ********** 
sub = numbers[1:4]    # Elements at index 1 to 3
rev = numbers[::-1]   # Reversed list



# ********** ********** ********** Looping through a List ********** ********** **********
for num in numbers:
    print(num)



# ********** ********** ********** List Comprehensions ********** ********** **********
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]





# ********** ********** ********** Useful ways ********** ********** **********
n= 0
m= 4
sub2 = numbers[n:m]
print(sub2)