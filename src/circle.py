from abc import ABC
from figure import Figure
from math import pi


class Circle(Figure, ABC):

    def __init__(self, radius: int):
        super().__init__(name='Circle')
        if radius <= 0:
            raise ValueError('radius must be more than 0')
        self.radius = radius

    def get_perimeter(self):
        return 2 * pi * self.radius

    def get_area(self):
        return pi * (self.radius ** 2)
