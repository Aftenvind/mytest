def divide(a, b):
    """两数相除，除数为零时抛出异常"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def get_grade(score):
    """根据分数返回等级，非法分数抛出异常"""
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