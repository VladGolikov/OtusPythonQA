from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError('side must be higher than 0')
        super().__init__(side_a, side_a)
        self.name = 'Square'
