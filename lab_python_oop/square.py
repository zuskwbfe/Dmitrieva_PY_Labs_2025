from lab_python_oop.rectangle import Rectangle
from lab_python_oop.colour import Colour

class Square(Rectangle):
    def __init__(self, side, colour):
        self.side = side
        self.colour = Colour()
        self.colour.colourproperty = colour

    FIGURE_TYPE = "Квадрат"
    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def sqere(self):
        return self.side ** 2

    def __repr__(self):
        return '{} {} цвета со стороной {} и площадью {}.'.format(
            Square.get_figure_type(), self.colour.colourproperty, self.side, self.sqere()
        )
