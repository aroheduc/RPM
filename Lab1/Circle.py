import math
from Shape import Shape

PI = math.pi

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.perimeter = 2 * PI * radius
        self.area = PI * (radius ^ 2)

    def __repr__(self):
        return f'Circle({self.radius}, {self.diameter}, {self.perimeter}, {self.area})'