from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(
    'side_a, side_b, side_c, area',
    [
        (4, 5, 7,  9.80),
        (3.5, 4.5, 7.7, 4.14)
    ],
    ids=['area_triangle_integer', 'area_triangle_float']
)
def test_area_triangle_positive(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert pytest.approx(t.get_area(), 0.01) == area, f'should be {area}'


@pytest.mark.parametrize(
    'side_a, side_b, side_c, perimeter',
    [
        (4, 5, 7, 16),
        (3.5, 4.5, 7.7, 15.7)
    ],
    ids=['perimeter_triangle_integer', 'perimeter_triangle_float']
)
def test_perimeter_triangle_positive(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter() == perimeter, f'should be {perimeter}'


def test_negative_triangle(invalid_triangle_data):
    side_a, side_b, side_c = invalid_triangle_data
    with pytest.raises(ValueError):
        t = Triangle(side_a, side_b, side_c)
