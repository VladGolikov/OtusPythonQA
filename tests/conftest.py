import pytest
from src.rectangle import Rectangle
from src.triangle import Triangle
from src.square import Square
from src.circle import Circle


@pytest.fixture(params=[(1, 2, 2), (1.1, 1.2, 1.32)], ids=['int', 'float'])
def rectangle_data(request):
    """fixture for practise"""
    side_a, side_b, area = request.param
    yield side_a, side_b, area


@pytest.fixture()
def data_wrapper_areas():
    """fixture for areas of figures"""
    def _wrapper(data: str):
        if data == 'rectangle_integer':
            return 3, 5, 15
        if data == 'rectangle_float':
            return 3.5, 5.5, 19.25
        if data == 'integer_triangle':
            return 13, 14, 15, 84
        if data == 'float_triangle':
            return 11.5, 12.5, 13.5, 66.78659460363285
        if data == 'integer_square':
            return 5, 25
        if data == 'float_square':
            return 3.5, 12.25
        if data == 'integer_circle':
            return 5, 78.53981633974483
        if data == 'float_circle':
            return 5.5, 95.03317777109125

    yield _wrapper


@pytest.fixture()
def data_wrapper_perimeters():
    """fixtures for perimeters of figures"""
    def _wrapper(data: str):
        if data == 'rectangle_integer':
            return 3, 5, 16
        if data == 'rectangle_float':
            return 3.5, 5.5, 18
        if data == 'integer_triangle':
            return 13, 14, 15, 42
        if data == 'float_triangle':
            return 11.5, 12.5, 13.5, 37.5
        if data == 'integer_square':
            return 5, 20
        if data == 'float_square':
            return 3.5, 14
        if data == 'integer_circle':
            return 5, 31.41592653589793
        if data == 'float_circle':
            return 5.5, 34.55751918948772

    yield _wrapper


@pytest.fixture()
def data_wrapper_error():
    """fixture for raise errors"""
    def _wrapper(data: str):
        if data == 'rectangle_integer':
            return 13, -14
        if data == 'rectangle_float':
            return 13.5, -15.5
        if data == 'triangle_integer':
            return 13, -14, 15
        if data == 'triangle_float':
            return 13.5, -15.5, 18
        if data == 'triangle_sides_exists':
            return 1, 2, 111
        if data == 'integer_square':
            return -5
        if data == 'float_square':
            return -3.5
        if data == 'integer_circle':
            return -5
        if data == 'float_circle':
            return -5.5

    yield _wrapper


@pytest.fixture()
def data_wrapper_add_areas():
    """fixtures for add_areas"""
    def _wrapper(data: str):
        if data == 'square+triangle':
            s = Square(10)
            t = Triangle(13,14,15)
            return s, t, 184
        if data == 'rectangle+circle':
            r = Rectangle(3, 5)
            c = Circle(2)
            return r, c, 27.566370614359172
        if data == 'similar_figures':
            r = Rectangle(3,5)
            return r, r, 30

    yield _wrapper


@pytest.fixture()
def data_wrapper_add_area_error():
    """fixtures for raise errors in add_area"""
    def _wrapper(data: str):
        if data == 'square':
            s = Square(10)
            return s, 5
        if data == 'triangle':
            t = Triangle(13,14,15)
            return t, 5

    yield _wrapper
