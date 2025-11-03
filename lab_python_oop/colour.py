class Colour:
    def __init__(self, colour = None):
        self.сolour = colour

    @property
    def colourproperty(self):
        return self.colour

    @colourproperty.setter
    def colourproperty(self, colour):
        self.colour = colour
