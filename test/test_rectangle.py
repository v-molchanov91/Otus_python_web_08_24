from src.Rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    'side_a, side_b, area',
    [
        (5, 8, 40),
        (3.5, 5.5, 19.25),
    ],
    ids=['area_integer', 'area_float']
)
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area == area, f'ara should be {area}'


@pytest.mark.slow
@pytest.mark.skip(reason='https://jira/pacs-1785')
def test_rectangle_float():
    r = Rectangle(3.5, 5.5)
    assert r.get_area == 19.25, 'area should be 19.25'


def test_rectangle_area_negative(create_negative_date_rectangle):
    side_a, side_b = create_negative_date_rectangle
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)


@pytest.mark.parametrize(
    'side_a, side_b, perimeter',
    [
        (5, 7, 24),
        (3.5, 4.5, 16)
    ],
    ids=['perimeter_integer', 'perimeter_float']
)
def test_rectangle_perimeter_positive(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.get_perimeter == perimeter, f'should be {perimeter}'


def test_rectangle_perimeter_negative(create_negative_date_rectangle):
    side_a, side_b = create_negative_date_rectangle
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
