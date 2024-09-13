from src.Circle import Circle
import pytest


@pytest.mark.parametrize(
    'radius, area',
    [
        (15, 706.85),
        (7.5, 176.71)
    ],
    ids=['circle_area_integer', 'circle_area_float']
)
def test_area_circle_positive(radius, area):
    c = Circle(radius)
    assert pytest.approx(c.get_area, 0.01) == area, f'should be {area}'


@pytest.mark.parametrize(
    'radius, perimeter',
    [
        (7, 43.96),
        (2.2, 13.81)
    ],
    ids=['perimeter_circle_integer', 'perimeter_circle_float']
)
def test_perimeter_circle_positive(radius, perimeter):
    c = Circle(radius)
    assert pytest.approx(c.get_perimeter, 0.01) == perimeter, f'should be {perimeter}'


def test_negative_circle(create_negative_date_square):
    radius = create_negative_date_square
    with pytest.raises(ValueError):
        c = Circle(radius)
