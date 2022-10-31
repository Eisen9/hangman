# Create a Class called Shape

class Shape:
    def __init__(self, num_sides, tesselates=False):
        if num_sides == 0:
            raise ValueError("Number of sides cannot be zero")
        self.num_sides = num_sides
        self.tesselates = tesselates

    def get_info(self):
        raise NotImplementedError("get_info() is not implemented")

    # TODO: CHECK if the last instuction (see line below) should be implmented here.
    # Define the __add__ magic method of the Shape class which defines how to add two instances of the Shape class together and returns a new Shape object with as many sides as the sum of the individual shapes added
    def __add__(self, other):
        return Shape(self.num_sides + other.num_sides) # create a new Shape object with as many sides as the sum of the individual shapes added




class Circle(Shape):
    def __init__(self, num_sides, tesselates=False):
        super().__init__(num_sides, tesselates)

    def get_info(self):
        return f"Circle with {self.num_sides} sides and tesselates: {self.tesselates}"

    

class Triangle(Shape):
    def __init__(self, num_sides, tesselates=False):
        super().__init__(num_sides, tesselates)

    def get_info(self):
        return f"Triangle with {self.num_sides} sides and tesselates: {self.tesselates}"

class Square(Shape):
    def __init__(self, num_sides, tesselates=False):
        super().__init__(num_sides, tesselates)

    def get_info(self):
        return f"Square with {self.num_sides} sides and tesselates: {self.tesselates}"


class Pentagon(Shape):
    def __init__(self, num_sides, tesselates=False):
        super().__init__(num_sides, tesselates)

    def get_info(self):
        return f"Pentagon with {self.num_sides} sides and tesselates: {self.tesselates}"

class Hexagon(Shape):
    def __init__(self, num_sides, tesselates=False):
        super().__init__(num_sides, tesselates)

    def get_info(self):
        return f"Hexagon with {self.num_sides} sides and tesselates: {self.tesselates}"


