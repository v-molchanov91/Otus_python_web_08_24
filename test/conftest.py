import pytest


@pytest.fixture(scope='session', autouse=True)
def create_DB():
    print('\n Start date base')

    yield

    print('\n stop date base')


@pytest.fixture(params=[(5, -7), (0, 8), (-4, -7)],
                ids=['one negative number', 'zero', 'two negative number'])
def create_negative_date_rectangle(request, create_DB):

    yield request.param


@pytest.fixture(params=[-7, 0, -4],
                ids=['negative number', 'zero', 'another negative number'])
def create_negative_date_square(request, create_DB):
    yield request.param


@pytest.fixture(params=[
    (1, 2, 3),
    (-1, 2, 3),
    (0, 2, 3),
    ('a', 2, 3),
    (3, 4, 'b'),
    (3, 4, None)
], ids=[
    'invalid_triangle_sides',
    'negative_side',
    'zero_side',
    'non_numeric_side_a',
    'non_numeric_side_c',
    'none_side_c'
])
def invalid_triangle_data(request):
    return request.param