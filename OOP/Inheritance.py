class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f'{self.name} says meow!'


class Dog(Animal):
    def speak(self):
        return f'{self.name} says woof!'


# Use different animals
animals = [Cat('Whiskers'), Dog('Rex')]

for animal in animals:
    print(animal.speak())



class Animal:
    def speak(self):
        return 'Some sound'

class Flyable:
    def fly(self):
        return 'Flying!'

class Bird(Animal, Flyable):    # Multiple inheritance
    def speak(self):
        return 'Chirp!'

# Method Resolution Order (MRO)
print(Bird.__mro__)    # Shows inheritance chain

# Diamond problem
class A:
    def method(self): return 'A'

class B(A):
    def method(self): return 'B'

class C(A):
    def method(self): return 'C'

class D(B, C):    # Python's MRO resolves conflicts
    pass

print(D().method())  # Calls B's method due to MRO