# Define a class
class Dog:
    # __init__ is called when creating a new instance
    # self refers to the instance being created/used
    # self is like 'this' in other languages - it's how an
    # instance accesses its own attributes and methods
    
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
    
    def bark(self):
        # self must be the first parameter of instance methods
        # so Python knows which instance to operate on
        return f'{self.name} says woof!'


# Create and use objects
my_dog = Dog('Rex', 3)  # Creates new instance, calls __init__
print(my_dog.name)      # Access attribute via instance
print(my_dog.bark())    # Call method via instance