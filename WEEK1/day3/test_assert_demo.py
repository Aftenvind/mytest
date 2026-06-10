def test_assert_basics():
    """各种 assert 写法练习"""

    # 1. 等于
    assert 2 + 3 == 5

    # 2. 不等于
    assert 2 + 3 != 6

    # 3. 大于/小于
    assert 10 > 5
    assert 3 < 9

    # 4. 是否为 True / False / None
    flag = True
    assert flag is True
    assert flag is not False

    result = None
    assert result is None

    # 5. 是否属于某个类型
    name = "hello"
    assert isinstance(name, str)

    number = 42
    assert isinstance(number, int)

    # 6. 字符串包含判断
    assert "ell" in "hello"
    assert "world" not in "hello"

    # 7. 列表/字典检查
    scores = [85, 92, 78]
    assert len(scores) == 3
    assert 92 in scores
    assert 100 not in scores

    student = {"name": "张三", "score": 85}
    assert "name" in student
    assert student["score"] >= 60