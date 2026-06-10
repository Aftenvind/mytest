import pytest
from val import divide, get_grade


def test_divide_normal():
    """正常除法"""
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0


def test_divide_by_zero():
    """除以零必须抛出 ValueError，且消息包含'除数不能为零'"""
    with pytest.raises(ValueError, match="除数不能为零"):
        divide(10, 0)


def test_get_grade_normal():
    """正常分数返回正确等级"""
    assert get_grade(95) == "优秀"
    assert get_grade(85) == "良好"
    assert get_grade(75) == "及格"
    assert get_grade(55) == "不及格"


def test_get_grade_boundary():
    """边界值测试"""
    assert get_grade(100) == "优秀"
    assert get_grade(90) == "优秀"
    assert get_grade(89) == "良好"
    assert get_grade(60) == "及格"
    assert get_grade(59) == "不及格"
    assert get_grade(0) == "不及格"


def test_get_grade_invalid_type():
    """非数字类型必须抛出 TypeError"""
    with pytest.raises(TypeError, match="分数必须是数字"):
        get_grade("九十")


def test_get_grade_out_of_range():
    """超出范围必须抛出 ValueError"""
    with pytest.raises(ValueError, match="分数必须在0-100之间"):
        get_grade(150)

    with pytest.raises(ValueError, match="分数必须在0-100之间"):
        get_grade(-10)