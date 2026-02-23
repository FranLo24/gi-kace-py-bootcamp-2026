class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

# Creating three Rectangle objects
rect1 = Rectangle(4, 5)
rect2 = Rectangle(10, 2)
rect3 = Rectangle(7, 7)

print(f"Area 1: {rect1.getArea()}")
print(f"Area 2: {rect2.getArea()}")
print(f"Area 3: {rect3.getArea()}")

# Add this inside the Rectangle class
def setWidth(self, width):
        self.width = width

# Testing the change
rect1.setWidth(10)
print(f"New Area of rect1: {rect1.getArea()}") # Should now be 50