import math

class Circle:
        radius = 0

        def __init__(self, radius):
                self.radius = radius

        def get_area(self):
                area = math.pi * (self.radius ** 2)
                return area


circle_1 = Circle(5)
circle_1.get_area()

circle_2 = Circle(15)
circle_2.get_area()

circle_3 = Circle(25)
circle_3.get_area()

print(f"Area of circle 1: {circle_1.get_area()}")
print(f"Area of circle 2: {circle_2.get_area()}")
print(f"Area of circle 3: {circle_3.get_area()}")