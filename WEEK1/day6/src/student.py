def calculate_average(scores):
    """计算平均分，scores 为非空列表"""
    if not scores:
        raise ValueError("成绩列表不能为空")
    for s in scores:
        if not isinstance(s, (int, float)):
            raise TypeError("成绩必须为数字")
        if s < 0 or s > 100:
            raise ValueError(f"成绩必须在0-100之间，非法值：{s}")
    return sum(scores) / len(scores)


def get_grade(score):
    """根据分数返回等级"""
    if not isinstance(score, (int, float)):
        raise TypeError("分数必须是数字")
    if score < 0 or score > 100:
        raise ValueError(f"分数必须在0-100之间，你输入的是{score}")
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


def class_summary(scores):
    """输入一个班级的成绩列表，返回统计信息字典
    返回格式：{"平均分": xx, "最高分": xx, "最低分": xx, "优秀人数": xx, "不及格人数": xx}
    """
    if not scores:
        raise ValueError("成绩列表不能为空")
    
    avg = calculate_average(scores)
    highest = max(scores)
    lowest = min(scores)
    excellent = sum(1 for s in scores if s >= 90)
    fail = sum(1 for s in scores if s < 60)
    
    return {
        "平均分": avg,
        "最高分": highest,
        "最低分": lowest,
        "优秀人数": excellent,
        "不及格人数": fail,
    }   