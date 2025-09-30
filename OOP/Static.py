class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod                # Alternative constructor
    def from_string(cls, date_str):
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)
    
    @staticmethod               # Utility function
    def is_valid_date(year, month, day):
        return (1 <= month <= 12 and
                1 <= day <= 31 and
                year >= 0)

# Usage
date1 = Date(2024, 3, 21)           # Regular constructor
date2 = Date.from_string('2024-3-21')  # Class method
valid = Date.is_valid_date(2024, 3, 21)  # Static method