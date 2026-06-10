import pytest

def is_even(n):
    """判断偶数"""
    return n % 2 == 0

@pytest.mark.parametrize("number", [2, 4, 6, 8, 10])
def test_is_even_true(number):
    assert is_even(number) is True

@pytest.mark.parametrize("number", [1, 3, 5, 7, 9])
def test_is_even_false(number):
    assert is_even(number) is False

def rectangle_area(width, height):
    """计算矩形面积"""
    if width <= 0 or height <= 0:
        raise ValueError("边长必须为正数")
    return width * height

@pytest.mark.parametrize("width, height, expected_area", [
    (3, 4, 12),
    (5, 5, 25),
    (1, 100, 100),
    (7, 8, 56),
])
def test_rectangle_area_normal(width, height, expected_area):
    assert rectangle_area(width, height) == expected_area

@pytest.mark.parametrize("width, height", [
    (-1, 4),
    (3, -2),
    (0, 5),
    (5, 0),
])
def test_rectangle_area_invalid(width, height):
    with pytest.raises(ValueError, match="边长必须为正数"):
        rectangle_area(width, height)

@pytest.fixture
def tax_rate():
    """固定税率 0.1"""
    return 0.1

@pytest.mark.parametrize("price, expected_total", [
    (100, 110.0),
    (200, 220.0),
    (50, 55.0),
])
def test_price_with_tax(price, expected_total, tax_rate):
    """计算含税价格：价格 × (1 + 税率)"""
    total = price * (1 + tax_rate)
    assert total == pytest.approx(expected_total)