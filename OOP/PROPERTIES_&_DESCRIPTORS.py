class Circle:
    def __init__(self, radius):
        self._radius = radius    # Protected attribute
    
    @property                   # Getter
    def radius(self):
        return self._radius
    
    @radius.setter              # Setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Must be positive')
        self._radius = value
    
    @property                   # Computed property
    def area(self):
        return 3.14 * self._radius ** 2

# Usage
circle = Circle(5)
print(circle.radius)    # Calls getter
circle.radius = 10      # Calls setter
print(circle.area)      # Computes area