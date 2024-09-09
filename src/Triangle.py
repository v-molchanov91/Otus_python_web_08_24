from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if not all(isinstance(x, (int, float)) for x in (side_a, side_b, side_c)):
            raise ValueError('Стороны треугольника должны быть числами')
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_c + side_b <= side_a:
            raise ValueError('Стороны не могут образовывать треугольник')
        if any(x <= 0 for x in (side_a, side_b, side_c)):
            raise ValueError('Все стороны треугольника должны быть положительными')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_area(self):
        return (1 / 2) * (self.side_a * self.side_b * self.side_c) ** 0.5

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c


