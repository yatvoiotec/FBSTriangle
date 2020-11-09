from triangle import Triangle
import pytest


@pytest.mark.parametrize("point_a, point_b, point_c",
                         [
                             pytest.param([1, 1], [1, 4], [5, 1], id='positive coordinates'),
                             pytest.param([-1, -1], [-1, -4], [-5, -1], id='negative coordinates'),
                             pytest.param([0, 0], [0, 3], [4, 0], id='zero coordinates'),
                         ])
def test_triangle_exists(point_a, point_b, point_c):
    triangle = Triangle(point_a, point_b, point_c)
    assert triangle.existence() is True


@pytest.mark.parametrize("point_a, point_b, point_c",
                         [
                             pytest.param([0, 0], [0, 0], [0, 0], id='a=b=c'),
                             pytest.param([1, 1], [1, 1], [0, 0], id='a=b'),
                             pytest.param([0, 0], [1, 1], [1, 1], id='b=c'),
                             pytest.param([1, 1], [0, 0], [1, 1], id='a=c'),
                             pytest.param([1, 1], [2, 2], [3, 3], id='a b c on the same line')
                         ])
def test_triangle_not_exists(point_a, point_b, point_c):
    triangle = Triangle(point_a, point_b, point_c)
    assert triangle.existence() is False
