import math
from lab_python_oop.geometric_shape import GeometricShape
from lab_python_oop.colour import Colour

class  Circle(GeometricShape):
    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = Colour()
        self.colour.colourproperty = colour

    FIGURE_TYPE = "Круг"
    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def sqere(self):
        return math.pi * self.radius * self.radius

    def __repr__(self):
        return '{} {} цвета радиусом {} и площадью {}.'.format(
            Circle.get_figure_type(), self.colour.colourproperty, self.radius, self.sqere()
        )
