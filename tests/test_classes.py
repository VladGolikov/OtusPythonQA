from src.rectangle import Rectangle
from src.triangle import Triangle
from src.square import Square
from src.circle import Circle
from datetime import datetime
import pytest


@pytest.mark.skip(reason='because i want to practise with skipping')
def test_rectangle_skip():
    """training example"""
    r = Rectangle(3, 5)
    assert r.get_area() == 15, f'Area should be {3 * 5}'


@pytest.mark.skipif(condition=datetime.now().year == 2023, reason='practise with skip if')
def test_rectangle_skip_if():
    """training example"""
    r = Rectangle(3, 5)
    assert r.get_area() == 15, f'Area should be {3 * 5}'


@pytest.mark.homework
def test_positive_rectangle_custom_mark():
    """for practise with custom run marks"""
    r = Rectangle(3, 5)
    assert r.get_area() == 15, f'Area should be {3 * 5}'


@pytest.mark.parametrize(('side_a', 'side_b', 'area'),
                         [
                             (1, 5, 5),
                             (3.5, 6.5, 22.75)

                         ],
                         ids=['integer', 'float']
                         )
def test_rectangle_parametrize(side_a, side_b, area):
    """training example"""
    r = Rectangle(side_a, side_b)
    assert r.get_area() == area, f'Area should be {side_a * side_b}'


def test_rectangle_with_fixture_from_conftest(rectangle_data):
    """training example"""
    side_a, side_b, area = rectangle_data
    r = Rectangle(side_a, side_b)
    assert r.get_area() == area, f"Area should be {area}"


@pytest.mark.parametrize(('side_a', 'side_b'),
                         [
                             (11, -5),
                             (3.5, -6.5)
                         ],
                         ids=['integer', 'float']
                         )
def test_rectangle_raise_error(side_a, side_b):
    """example how to parametrize errors"""
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize("rectangle_types", ['rectangle_integer', "rectangle_float"])
def test_rectangle_area(data_wrapper_areas, rectangle_types):
    """my tests start from this"""
    side_a, side_b, area = data_wrapper_areas(data=rectangle_types)
    r = Rectangle(side_a, side_b)
    assert r.get_area() == area, f"Area should be {area}"


@pytest.mark.parametrize("rectangle_types", ['rectangle_integer', "rectangle_float"])
def test_rectangle_perimeter(data_wrapper_perimeters, rectangle_types):
    side_a, side_b, perimeter = data_wrapper_perimeters(data=rectangle_types)
    r = Rectangle(side_a, side_b)
    assert r.get_perimeter() == perimeter, f"Perimeter should be {perimeter}"


@pytest.mark.parametrize("rectangle", ['rectangle_integer', 'rectangle_float'])
def test_rectangle_error(data_wrapper_error, rectangle):
    side_a, side_b = data_wrapper_error(data=rectangle)
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize("triangle", ['integer_triangle', "float_triangle"])
def test_triangle_area(data_wrapper_areas, triangle):
    side_a, side_b, side_c, area = data_wrapper_areas(data=triangle)
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area() == area, f"Area should be {area}"


@pytest.mark.parametrize("triangle", ['integer_triangle', "float_triangle"])
def test_triangle_perimeter(data_wrapper_perimeters, triangle):
    side_a, side_b, side_c, perimeter = data_wrapper_perimeters(data=triangle)
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter() == perimeter, f"Perimeter should be {perimeter}"


@pytest.mark.parametrize("triangle", ['triangle_integer', 'triangle_float', 'triangle_sides_exists'])
def test_triangle_error(data_wrapper_error, triangle):
    side_a, side_b, side_c = data_wrapper_error(data=triangle)
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize("square", ['integer_square', "float_square"])
def test_square_area(data_wrapper_areas, square):
    side_a, area = data_wrapper_areas(data=square)
    s = Square(side_a)
    assert s.get_area() == area, f"Area should be {area}"


@pytest.mark.parametrize("square", ['integer_square', "float_square"])
def test_square_perimeter(data_wrapper_perimeters, square):
    side_a, perimeter = data_wrapper_perimeters(data=square)
    s = Square(side_a)
    assert s.get_perimeter() == perimeter, f"Perimeter should be {perimeter}"


@pytest.mark.parametrize("square", ['integer_square', 'float_square'])
def test_square_error(data_wrapper_error, square):
    side_a = data_wrapper_error(data=square)
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.parametrize("circle", ['integer_circle', "float_circle"])
def test_circle_area(data_wrapper_areas, circle):
    radius, area = data_wrapper_areas(data=circle)
    c = Circle(radius)
    assert c.get_area() == area, f"Area should be {area}"


@pytest.mark.parametrize("circle", ['integer_circle', "float_circle"])
def test_circle_perimeter(data_wrapper_perimeters, circle):
    radius, perimeter = data_wrapper_perimeters(data=circle)
    c = Circle(radius)
    assert c.get_perimeter() == perimeter, f"Area should be {perimeter}"

@pytest.mark.parametrize("circle", ['integer_circle', 'float_circle'])
def test_circle_error(data_wrapper_error, circle):
    radius = data_wrapper_error(data=circle)
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize("figures", ['square+triangle', 'rectangle+circle', 'similar_figures'])
def test_add_area(data_wrapper_add_areas, figures):
    figure_1, figure_2, add_area_sum = data_wrapper_add_areas(data=figures)
    assert figure_1.add_area(figure_2) == add_area_sum


@pytest.mark.parametrize("error_data", ['square', 'triangle'])
def test_add_area_raise_error(data_wrapper_add_area_error, error_data):
    figure, uncorrect_value = data_wrapper_add_area_error(data=error_data)
    with pytest.raises(ValueError):
        figure.add_area(uncorrect_value)