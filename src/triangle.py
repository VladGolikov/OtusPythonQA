from abc import ABC
from figure import Figure


class Triangle(Figure, ABC):

    def __init__(self, side_a: int, side_b: int, side_c: int):
        super().__init__(name='Triangle')
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError('the sides of triangle must be higher than 0')
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError('rectangle with these sides not exists')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        """triangle area = (p * (p — a) * (p — b) * (p — c)) ** 1/2
         where p is a half of perimeter
         """
        p = (self.get_perimeter()) / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
