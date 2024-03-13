from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a: int):
        super().__init__(side_a, side_a)
        if side_a <= 0:
            raise ValueError('side must be higher than 0')
        self.name = 'Square'
