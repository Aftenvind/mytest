import pytest
from rn import is_leap  # 你的教学代码里的函数


def test_is_leap_normal():
    """正常闰年判断"""
    assert is_leap(2000) is True   # 世纪闰年
    assert is_leap(2024) is True   # 普通闰年
    assert is_leap(2023) is False  # 非闰年


def test_is_leap_boundary():
    """边界值"""
    assert is_leap(4) is True      # 最小的普通闰年
    assert is_leap(1) is False


def test_is_leap_invalid():
    """非法输入"""
    with pytest.raises(ValueError):
        is_leap(-100)