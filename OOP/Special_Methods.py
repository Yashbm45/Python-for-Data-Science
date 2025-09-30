class Point:
    # __init__: Constructor for new instances
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # __str__: Human-readable string representation
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    # __repr__: Developer-readable representation
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
    # __add__: Defines + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    # __eq__: Defines == operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Usage
p1 = Point(1, 2)
p2 = Point(3, 4)
print(str(p1))      # Calls __str__
print(repr(p1))     # Calls __repr__
print(p1 + p2)      # Calls __add__
print(p1 == p2)     # Calls __eq__