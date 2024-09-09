from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a, side_b):
        if side_a <=0 or side_b <=0:
            raise ValueError("this is not Rectangle")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2

