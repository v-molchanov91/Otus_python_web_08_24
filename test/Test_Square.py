from src.Square import Square
import pytest


@pytest.mark.parametrize(
    'side_a, area',
    [
        (4, 16),
        (3.5, 12.25)
    ],
    ids=['area_square_integer', 'area_square_float']
)
def test_area_square_positive(side_a, area):
    s = Square(side_a)
    assert s.get_area == area, f'should be {area}'


@pytest.mark.parametrize(
    'side_a, perimeter',
    [
        (6, 24),
        (7.5, 30)
    ],
    ids=['perimeter_square_integer', 'perimeter_square_float']
)
def test_perimeter_square_positive(side_a, perimeter):
    s = Square(side_a)
    assert s.get_perimeter == perimeter, f'should be {perimeter}'


def test_area_negative_square(create_negative_date_square):
    side_a = create_negative_date_square
    with pytest.raises(ValueError):
        s = Square(side_a)

