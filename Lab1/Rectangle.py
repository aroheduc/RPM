from Shape import Shape

class Rectangle(Shape):
    def __init__(self, side_one, side_two):
        self.side_one = side_one
        self.side_two = side_two
        self.perimeter = side_one * 2 + side_two * 2
        self.area = side_one * side_two

    def __repr__(self):
        return f'Rectangle({self.side_one}, {self.side_two}, {self.perimeter}, {self.area})'