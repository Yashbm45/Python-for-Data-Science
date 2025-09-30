# Iterator Protocol
class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        result = self.current
        self.current += 1
        return result

# Using iterator
for num in Counter(1, 3):
    print(num)    # 1, 2, 3

# Iterator vs Iterable
iterable = [1, 2, 3]       # Iterable
iterator = iter(iterable)  # Iterator

print(next(iterator))     # 1
print(next(iterator))     # 2