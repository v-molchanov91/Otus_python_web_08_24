from src.Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a):
        super().__init__(side_a, side_a)
        if side_a <= 0:
            raise ValueError("this is not Square")
        self.side_a =side_a
