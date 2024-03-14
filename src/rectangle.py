from figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a: int, side_b: int):
        super().__init__(name='Rectangle')
        if side_a <= 0 or side_b <= 0:
            raise ValueError('side_a and side_b must be higher than 0')
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)
