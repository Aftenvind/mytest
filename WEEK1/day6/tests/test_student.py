import pytest
import sys
sys.path.insert(0,'../src')
from src.student import calculate_average, get_grade, class_summary


# ==================== Fixtures ====================

@pytest.fixture
def normal_scores():
    """一组正常的成绩数据"""
    return [85, 92, 78, 60, 55]


@pytest.fixture
def all_excellent_scores():
    """全部优秀的成绩"""
    return [95, 98, 92, 90]


@pytest.fixture
def all_fail_scores():
    """全部不及格的成绩"""
    return [55, 48, 30, 59]


@pytest.fixture
def mixed_scores():
    """混合成绩，用于 class_summary 测试"""
    return [95, 85, 72, 58, 91, 60, 45, 88]
# ==================== calculate_average 测试 ====================

class TestCalculateAverage:
    """对 calculate_average 的测试集合（用类分组，清晰可读）"""

    def test_normal_scores(self, normal_scores):
        """正常成绩计算平均分"""
        avg = calculate_average(normal_scores)
        assert avg == 74.0

    @pytest.mark.parametrize("scores, expected", [
        ([100, 100, 100], 100.0),
        ([0, 0, 0], 0.0),
        ([100, 0], 50.0),
        ([75], 75.0),
        ([60, 70, 80, 90, 100], 80.0),
    ])
    def test_various_scores(self, scores, expected):
        """参数化：各种成绩组合"""
        assert calculate_average(scores) == expected

    def test_empty_list_raises_error(self):
        """空列表应抛出 ValueError"""
        with pytest.raises(ValueError, match="成绩列表不能为空"):
            calculate_average([])

    @pytest.mark.parametrize("scores", [
        [85, "92", 78],
        [None, 90],
        ["abc"],
    ])
    def test_invalid_type_raises_error(self, scores):
        """非数字类型应抛出 TypeError"""
        with pytest.raises(TypeError, match="成绩必须为数字"):
            calculate_average(scores)

    @pytest.mark.parametrize("scores", [
        [-1, 85, 90],
        [105, 80, 75],
        [60, 200],
    ])
    def test_out_of_range_raises_error(self, scores):
        """超出 0-100 范围应抛出 ValueError"""
        with pytest.raises(ValueError, match="成绩必须在0-100之间"):
            calculate_average(scores)
# ==================== get_grade 测试 ====================

class TestGetGrade:

    @pytest.mark.parametrize("score, expected_grade", [
        (100, "优秀"),
        (95, "优秀"),
        (90, "优秀"),
        (89, "良好"),
        (85, "良好"),
        (80, "良好"),
        (79, "及格"),
        (60, "及格"),
        (59, "不及格"),
        (30, "不及格"),
        (0, "不及格"),
    ])
    def test_all_boundaries(self, score, expected_grade):
        """参数化覆盖所有等级边界"""
        assert get_grade(score) == expected_grade

    def test_non_number_type(self):
        """非数字类型抛出 TypeError"""
        with pytest.raises(TypeError, match="分数必须是数字"):
            get_grade("不错")

    @pytest.mark.parametrize("score", [-1, -50, 101, 150])
    def test_out_of_range(self, score):
        """超出范围抛出 ValueError"""
        with pytest.raises(ValueError, match="分数必须在0-100之间"):
            get_grade(score)
# ==================== class_summary 测试 ====================

class TestClassSummary:

    def test_with_mixed_scores(self, mixed_scores):
        """测试混合成绩的统计信息"""
        result = class_summary(mixed_scores)
        assert result["平均分"] == 74.25
        assert result["最高分"] == 95
        assert result["最低分"] == 45
        assert result["优秀人数"] == 2   # 95, 91
        assert result["不及格人数"] == 2  # 58, 45

    def test_all_excellent(self, all_excellent_scores):
        """全部优秀时，优秀人数应等于总人数，不及格为0"""
        result = class_summary(all_excellent_scores)
        assert result["优秀人数"] == 4
        assert result["不及格人数"] == 0

    def test_all_fail(self, all_fail_scores):
        """全部不及格"""
        result = class_summary(all_fail_scores)
        assert result["优秀人数"] == 0
        assert result["不及格人数"] == 4

    def test_empty_list(self):
        """空列表抛异常"""
        with pytest.raises(ValueError, match="成绩列表不能为空"):
            class_summary([])

    def test_single_student(self):
        """只有一个学生时，各项数值应一致"""
        result = class_summary([88])
        assert result["平均分"] == 88.0
        assert result["最高分"] == 88.0
        assert result["最低分"] == 88.0
