import math

class Circle:
        radius = 0

        def __init__(self, radius):
                self.radius = radius

        def get_area(self):
                area = math.pi * (self.radius ** 2)
                print(F"The circle's area is: {area:.2f}")


circle_1 = Circle(5)
circle_1.get_area()

circle_2 = Circle(15)
circle_2.get_area()

circle_3 = Circle(25)
circle_3.get_area()