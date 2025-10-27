import math
from Shape import Shape

class Triangle(Shape):
    def __init__(self, side_one, side_two, side_three):
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three
        self.perimeter = side_one + side_two + side_three
        self.area = math.sqrt(self.perimeter * (self.perimeter - side_one) * (self.perimeter - side_two) * (self.perimeter - side_three))

    def __repr__(self):
        return f'Triangle({self.side_one}, {self.side_two}, {self.side_three}, {self.perimeter}, {self.area})'