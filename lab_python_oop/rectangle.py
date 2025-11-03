from lab_python_oop.geometric_shape import GeometricShape
from lab_python_oop.colour import Colour

class Rectangle(GeometricShape):
    def __init__(self, width, height, colour):
        self.width = 1
        self.height = 1
        self.colour = Colour()
        self.colour.colourproperty = colour

    FIGURE_TYPE = "Прямоугольник"
    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def sqere(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(), self.colour.colourproperty, self.width, self.height, self.sqere()
        )
