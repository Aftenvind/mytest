# 成绩管理系统 - 测试练习

## 项目简介
本项目是我从编程教学转型测试开发的学习作品。
包含一个学生成绩管理系统的核心逻辑及其完整的 pytest 测试套件。

## 项目结构
- src/grade_system.py：被测代码，包含 calculate_average、get_grade、class_summary 三个函数
- tests/test_grade_system.py：测试套件，覆盖正常路径、边界值、异常路径

## 技术栈
- Python 3.x
- pytest（fixture、parametrize、异常测试）

## 如何运行
### 1. 创建虚拟环境
python -m venv env
### 2. 激活虚拟环境
Windows: env\Scripts\activate
Mac/Linux: source env/bin/activate
### 3. 安装依赖
pip install -r requirements.txt
### 4. 运行测试
python -m pytest tests/ -v

## 测试覆盖
- calculate_average：正常计算、空列表异常、非数字异常、超出范围异常
- get_grade：五个等级判定、边界值、类型异常、范围异常
- class_summary：混合成绩统计、全优/全不及格、单学生

## 学习笔记
本项目对应我12周测试开发学习计划的第一周成果。
- 第1周掌握了 pytest 核心三件套：assert / fixture / parametrize
- 下一周将学习 Selenium Web 自动化测试