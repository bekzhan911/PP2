class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

# Example usage
square = Square(5)
print(f"Area of the square with length {square.length} is {square.area()}")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Example usage
rectangle = Rectangle(4, 6)
print(f"Area of the rectangle with length {rectangle.length} and width {rectangle.width} is {rectangle.area()}")
