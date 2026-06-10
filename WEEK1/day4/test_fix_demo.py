import pytest

@pytest.fixture
def student_dict():
    """返回一个字典"""
    return {"name": "张三", "age": 16, "scores": [85, 92, 78]}

@pytest.fixture
def class_names():
    """返回一个列表"""
    return ["一班", "二班", "三班"]

def test_student_name(student_dict):
    assert student_dict["name"] == "张三"

def test_student_has_scores(student_dict):
    assert len(student_dict["scores"]) == 3

def test_class_count(class_names):
    assert len(class_names) == 3

@pytest.fixture
def calculated_average():
    """fixture 不只是返回死数据，可以包含计算逻辑"""
    scores = [85, 92, 78, 60, 55]
    avg = sum(scores) / len(scores)
    return {"scores": scores, "average": avg}

def test_average_value(calculated_average):
    assert calculated_average["average"] == 74.0

def test_all_scores_present(calculated_average):
    assert len(calculated_average["scores"]) == 5

@pytest.fixture
def student_name():
    return "李四"

@pytest.fixture
def student_scores():
    return [90, 88, 92]

def test_student_info(student_name, student_scores):
    """同时使用两个 fixture"""
    assert student_name == "李四"
    assert sum(student_scores) == 270

call_count = 0  # 全局计数器，帮你观察 fixture 被调用了几次

@pytest.fixture(scope="function")  # 默认，可省略
def per_function_fixture():
    global call_count
    call_count += 1
    print(f"\nfixture 被调用了，当前次数：{call_count}")
    return [1, 2, 3]

def test_first(per_function_fixture):
    assert len(per_function_fixture) == 3

def test_second(per_function_fixture):
    assert sum(per_function_fixture) == 6

@pytest.fixture(scope="module")
def shared_data():
    print("\n这个 fixture 只执行一次")
    return {"key": "value"}

def test_use1(shared_data):
    assert "key" in shared_data

def test_use2(shared_data):
    shared_data["new_key"] = "new_value"  # 修改了数据
    assert "new_key" in shared_data

def test_use3(shared_data):
    # test_use2 的修改在这里可见，因为是同一份数据
    assert shared_data["new_key"] == "new_value"